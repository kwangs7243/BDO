from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Iterable, Mapping
from datetime import UTC, date, datetime, time
from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.config import PROJECT_ROOT, seed_dir
from app.database import Base
from app.knowledge import (
    get_knowledge_content,
    get_knowledge_project,
    get_knowledge_recipe,
    list_knowledge_materials,
)
from app.models import Content, Project, Recipe
from app.recipe_dependencies import build_recipe_dependency_index
from app.seed import import_seed
from app.schemas import (
    KnowledgeContentOut,
    KnowledgeMaterialOut,
    KnowledgeProjectOut,
    KnowledgeRecipeDependenciesOut,
    KnowledgeRecipeDependencyEdgeOut,
    KnowledgeRecipeOut,
    SourceOut,
)


GENERATED_HEADER = """<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->"""

DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "ai_exports"
STATIC_PROJECTION_TIME = datetime(2000, 1, 1, tzinfo=UTC)


def _json_value(value: object) -> str:
    if isinstance(value, (date, datetime, time)):
        value = value.isoformat()
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _fields(rows: Iterable[tuple[str, object]]) -> str:
    return "\n".join(f"- {name}: {_json_value(value)}" for name, value in rows)


def _section(lines: list[str], heading: str, blocks: list[str]) -> None:
    lines.extend(["", f"## {heading}", ""])
    if blocks:
        lines.extend(blocks)
    else:
        lines.append("- None")


def _joined_blocks(blocks: Iterable[str]) -> list[str]:
    rendered = "\n\n".join(blocks)
    return [rendered] if rendered else []


def _named_blocks(rows: Iterable[tuple[str, list[tuple[str, object]]]]) -> list[str]:
    blocks: list[str] = []
    for index, (identity, fields) in enumerate(rows):
        if index:
            blocks.append("")
        blocks.append(f"### `{identity}`")
        blocks.append("")
        blocks.append(_fields(fields))
    return blocks


def _render_requirement(requirement) -> str:
    lines = [
        f"### `{requirement.seed_key}`",
        "",
        _fields(
            [
                ("seed_key", requirement.seed_key),
                ("kind", requirement.kind),
                ("requirement_level", requirement.requirement_level),
                ("title", requirement.title),
                ("description", requirement.description),
            ]
        ),
        "- structured_value:",
    ]
    if requirement.structured_value is None:
        lines[-1] = "- structured_value: null"
    else:
        lines.extend(
            [
                "",
                "```json",
                json.dumps(
                    requirement.structured_value,
                    ensure_ascii=False,
                    sort_keys=True,
                    indent=2,
                ),
                "```",
            ]
        )
    return "\n".join(lines)


def _render_section(section) -> str:
    return "\n".join(
        [
            f"### `{section.seed_key}`",
            "",
            _fields(
                [
                    ("seed_key", section.seed_key),
                    ("section_type", section.section_type),
                    ("title", section.title),
                    ("order_no", section.order_no),
                ]
            ),
            "",
            "#### body_markdown",
            "",
            section.body_markdown,
        ]
    )


def _evidence_fields(evidence: SourceOut) -> list[tuple[str, object]]:
    return [
        ("evidence_seed_key", evidence.evidence_seed_key),
        ("source_id", evidence.id),
        ("title", evidence.title),
        ("url", evidence.url),
        ("publisher", evidence.publisher),
        ("source_type", evidence.source_type),
        ("published_at", evidence.published_at),
        ("retrieved_at", evidence.retrieved_at),
        ("region", evidence.region),
        ("entity_type", evidence.entity_type),
        ("entity_id", evidence.entity_id),
        ("claim_key", evidence.claim_key),
        ("verification_status", evidence.verification_status),
        ("last_verified_at", evidence.last_verified_at),
        ("evidence_note", evidence.evidence_note),
        ("active", evidence.active),
        ("is_active", evidence.is_active),
    ]


def _evidence_blocks(rows: list[SourceOut]) -> list[str]:
    sorted_rows = sorted(
        rows,
        key=lambda item: (
            item.entity_type,
            item.entity_id,
            item.claim_key,
            item.evidence_seed_key or "",
            item.id,
        ),
    )
    return _named_blocks(
        (
            item.evidence_seed_key
            or f"{item.entity_type}:{item.entity_id}:{item.claim_key}:{item.id}",
            _evidence_fields(item),
        )
        for item in sorted_rows
    )


def render_content_markdown(
    content: KnowledgeContentOut,
    exported_content_slugs: set[str],
) -> str:
    """Render one canonical-only Content DTO without volatile runtime fields."""

    lines = [GENERATED_HEADER, "", f"# {content.name_ko}"]

    _section(
        lines,
        "Identity",
        [
            _fields(
                [
                    ("slug", content.slug),
                    ("name_ko", content.name_ko),
                    ("category", content.category),
                    ("status", content.status),
                    ("verification_status", content.verification_status),
                    ("last_verified_at", content.last_verified_at),
                    ("party_type", content.party_type),
                    ("difficulty", content.difficulty),
                ]
            )
        ],
    )
    _section(
        lines,
        "Overview",
        [_fields([("summary", content.summary), ("purpose", content.purpose)])],
    )
    _section(
        lines,
        "Requirements",
        _joined_blocks(_render_requirement(item) for item in content.requirements),
    )
    _section(
        lines,
        "Steps",
        _named_blocks(
            (
                item.seed_key,
                [
                    ("seed_key", item.seed_key),
                    ("phase", item.phase),
                    ("order_no", item.order_no),
                    ("title", item.title),
                    ("description", item.description),
                    ("checkable", item.checkable),
                ],
            )
            for item in content.steps
        ),
    )
    _section(
        lines,
        "Schedules",
        _named_blocks(
            (
                item.seed_key or f"{item.rule_type}:{item.recurrence_type}",
                [
                    ("seed_key", item.seed_key),
                    ("rule_type", item.rule_type),
                    ("recurrence_type", item.recurrence_type),
                    ("weekday", item.weekday),
                    ("time_local", item.time_local),
                    ("fixed_datetime", item.fixed_datetime),
                    ("timezone", item.timezone),
                    ("notes", item.notes),
                ],
            )
            for item in content.schedules
        ),
    )
    _section(
        lines,
        "Rewards",
        _named_blocks(
            (
                item.seed_key,
                [
                    ("seed_key", item.seed_key),
                    ("name", item.name),
                    ("reward_type", item.reward_type),
                    ("amount", item.amount),
                    ("min_amount", item.min_amount),
                    ("max_amount", item.max_amount),
                    ("unit", item.unit),
                    ("is_choice", item.is_choice),
                    ("choice_group", item.choice_group),
                    ("recommendation", item.recommendation),
                    ("notes", item.notes),
                    ("order_no", item.order_no),
                ],
            )
            for item in content.rewards
        ),
    )
    _section(
        lines,
        "Sections",
        _joined_blocks(_render_section(item) for item in content.sections),
    )

    relation_blocks: list[str] = []
    for relation in content.related_contents:
        fields: list[tuple[str, object]] = [
            ("seed_key", relation.seed_key),
            ("direction", relation.direction),
            ("relation_type", relation.relation_type),
            ("content_slug", relation.content_slug),
            ("content_name_ko", relation.content_name_ko),
            ("content_category", relation.content_category),
            ("note", relation.note),
            ("order_no", relation.order_no),
        ]
        if relation.content_slug in exported_content_slugs:
            fields.append(
                ("relative_path", f"../contents/{relation.content_slug}.md")
            )
        relation_blocks.extend(
            _named_blocks([(relation.seed_key, fields)])
        )
    _section(lines, "Related Contents", relation_blocks)

    current = [item for item in content.sources if item.is_active]
    historical = [item for item in content.sources if not item.is_active]
    evidence_blocks = ["### Current evidence", ""]
    evidence_blocks.extend(_evidence_blocks(current) or ["- None"])
    evidence_blocks.extend(["", "### Historical / inactive evidence", ""])
    evidence_blocks.extend(_evidence_blocks(historical) or ["- None"])
    _section(lines, "Evidence and Sources", evidence_blocks)

    return "\n".join(lines).rstrip() + "\n"


def render_project_markdown(
    project: KnowledgeProjectOut,
    exported_content_slugs: set[str],
) -> str:
    """Render one canonical-only Project DTO and its stateless calculation contract."""

    lines = [GENERATED_HEADER, "", f"# {project.name_ko}"]
    _section(
        lines,
        "Identity",
        [
            _fields(
                [
                    ("slug", project.slug),
                    ("name_ko", project.name_ko),
                    ("content_slug", project.content_slug),
                    ("summary", project.summary),
                    ("active", project.active),
                ]
            )
        ],
    )
    _section(lines, "Overview", [_fields([("summary", project.summary)])])
    _section(
        lines,
        "Stages",
        _named_blocks(
            (
                stage.seed_key,
                [
                    ("seed_key", stage.seed_key),
                    ("name", stage.name),
                    ("description", stage.description),
                    ("order_no", stage.order_no),
                    ("dependencies", stage.dependencies),
                ],
            )
            for stage in project.stages
        ),
    )
    _section(
        lines,
        "Material Requirements",
        _named_blocks(
            (
                material.seed_key,
                [
                    ("seed_key", material.seed_key),
                    ("material_key", material.material_key),
                    ("name_ko", material.name_ko),
                    ("unit", material.unit),
                    ("stage_seed_key", material.stage_seed_key),
                    ("required_quantity", material.required_quantity),
                    ("notes", material.notes),
                    ("order_no", material.order_no),
                    ("source_entity_type", material.source_entity_type),
                    ("source_entity_seed_key", material.source_entity_seed_key),
                ],
            )
            for material in project.materials
        ),
    )

    acquisition_blocks: list[str] = []
    for material in project.materials:
        for source in material.sources:
            fields: list[tuple[str, object]] = [
                ("project_material_seed_key", material.seed_key),
                ("seed_key", source.seed_key),
                ("content_slug", source.content_slug),
                ("content_name_ko", source.content_name_ko),
                ("quantity_per_completion", source.quantity_per_completion),
                ("notes", source.notes),
                ("order_no", source.order_no),
            ]
            if source.content_slug in exported_content_slugs:
                fields.append(
                    ("relative_path", f"../contents/{source.content_slug}.md")
                )
            acquisition_blocks.extend(_named_blocks([(source.seed_key, fields)]))
    _section(lines, "Acquisition Sources", acquisition_blocks)

    _section(
        lines,
        "Stateless Calculation Contract",
        [
            _fields(
                [
                    ("caller_quantity", "ephemeral personal state"),
                    ("missing_quantity", 0),
                    ("local_inventory_fallback", False),
                    ("persistence", False),
                    (
                        "shortage_formula",
                        "max(required_quantity - provided_quantity, 0)",
                    ),
                ]
            )
        ],
    )
    return "\n".join(lines).rstrip() + "\n"


def _recipe_dependency_blocks(
    edges: list[KnowledgeRecipeDependencyEdgeOut],
    *,
    link_to: str,
) -> list[str]:
    blocks: list[str] = []
    for index, edge in enumerate(edges):
        if index:
            blocks.append("")
        blocks.extend(
            [
                f"#### `{edge.producer_recipe_slug} -> {edge.consumer_recipe_slug}`",
                "",
                _fields(
                    [
                        ("producer_recipe_slug", edge.producer_recipe_slug),
                        ("producer_recipe_name_ko", edge.producer_recipe_name_ko),
                        ("producer_process_type", edge.producer_process_type),
                        (
                            "producer_verification_status",
                            edge.producer_verification_status,
                        ),
                        ("consumer_recipe_slug", edge.consumer_recipe_slug),
                        ("consumer_recipe_name_ko", edge.consumer_recipe_name_ko),
                        ("consumer_process_type", edge.consumer_process_type),
                        (
                            "consumer_verification_status",
                            edge.consumer_verification_status,
                        ),
                        ("material_key", edge.material_key),
                        ("material_name_ko", edge.material_name_ko),
                        ("unit", edge.unit),
                        ("required_quantity", edge.required_quantity),
                        ("consumer_slot_seed_key", edge.consumer_slot_seed_key),
                        ("consumer_option_seed_key", edge.consumer_option_seed_key),
                        ("is_alternative", edge.is_alternative),
                        (
                            "relative_path",
                            f"../recipes/{getattr(edge, link_to)}.md",
                        ),
                    ]
                ),
            ]
        )
    return blocks or ["- None"]


def render_recipe_markdown(
    recipe: KnowledgeRecipeOut,
    dependencies: KnowledgeRecipeDependenciesOut | None = None,
) -> str:
    """Render canonical slots/options without inferring yields or mixed substitutions."""
    lines = [GENERATED_HEADER, "", f"# {recipe.name_ko}"]
    _section(lines, "Identity", [_fields([
        ("slug", recipe.slug), ("process_type", recipe.process_type),
        ("summary", recipe.summary), ("verification_status", recipe.verification_status),
        ("last_verified_at", recipe.last_verified_at)])])
    _section(lines, "Result", [_fields([
        ("material_key", recipe.result_material_key),
        ("name_ko", recipe.result_material_name_ko), ("unit", recipe.result_unit)])])
    _section(lines, "Recipe Requirement", [_fields([
        ("required_skill_tier", recipe.required_skill_tier),
        ("required_skill_level", recipe.required_skill_level)])])
    blocks = []
    group_sources = {}
    for slot in recipe.ingredient_slots:
        blocks.extend([f"### {slot.label}", "", _fields([
            ("seed_key", slot.seed_key), ("order_no", slot.order_no), ("notes", slot.notes)])])
        for option in slot.options:
            blocks.extend(["", f"#### {option.seed_key}", "", _fields([
                ("target_type", option.target_type), ("required_quantity", option.required_quantity),
                ("order_no", option.order_no), ("notes", option.notes)])])
            if option.ingredient_group is None:
                blocks.append(_fields([("material_key", option.material_key),
                                       ("name_ko", option.material_name_ko), ("unit", option.unit)]))
            else:
                group = option.ingredient_group
                blocks.append(_fields([("group", group.key), ("name_ko", group.name_ko),
                                       ("verification_status", group.verification_status),
                                       ("last_verified_at", group.last_verified_at)]))
                blocks.extend(["", "Allowed current members:", ""])
                blocks.extend(f"- {m.material_key} / {m.name_ko} ({m.unit})" for m in group.members)
                group_sources[group.key] = group.sources
        blocks.append("")
    _section(lines, "Ingredient Slots", blocks)
    semantics = [
        "- Ingredient quantities are per one recipe attempt.",
        "- All active slots are required (AND).",
        "- Options inside one slot are alternatives (OR); select one allowed material.",
        "- IngredientGroup membership does not define a global quantity conversion.",
        "- required_quantity belongs to this Recipe option.",
        "- Mixed option consumption is not inferred.",
        "- Result quantity is not guaranteed by this Recipe definition.",
        "- High-quality/special multipliers and yield probabilities are not defined.",
    ]
    if recipe.process_type == "alchemy":
        semantics.extend([
            "- required_quantity is the canonical full formulation quantity for one attempt.",
            "- Reduced-input probabilistic success is not modeled.",
            "- Output quantity and special-result probability are not modeled.",
            "- Alchemy level/mastery output effects are not modeled.",
        ])
    _section(lines, "Substitution Semantics", semantics)
    dependency_lines = [
        "- Only explicit Material options create dependency edges.",
        "- IngredientGroup membership is not expanded.",
        "- Dependencies are direct only.",
        "- No recursive quantity propagation is performed.",
        "- No producer output/yield is inferred.",
        "",
        "### Upstream Producers",
        "",
    ]
    dependency_lines.extend(
        _recipe_dependency_blocks(
            dependencies.direct_upstream if dependencies is not None else [],
            link_to="producer_recipe_slug",
        )
    )
    dependency_lines.extend(["", "### Downstream Consumers", ""])
    dependency_lines.extend(
        _recipe_dependency_blocks(
            dependencies.direct_downstream if dependencies is not None else [],
            link_to="consumer_recipe_slug",
        )
    )
    _section(lines, "Direct Recipe Dependencies", dependency_lines)
    sources = [*recipe.sources, *[s for key in sorted(group_sources) for s in group_sources[key]]]
    lines.extend(["", "## Evidence and Sources", "", "### Current evidence", ""])
    lines.extend(_evidence_blocks([s for s in sources if s.is_active]) or ["- None"])
    lines.extend(["", "### Historical / inactive evidence", ""])
    lines.extend(_evidence_blocks([s for s in sources if not s.is_active]) or ["- None"])
    return "\n".join(lines).rstrip() + "\n"



def render_material_markdown(
    material: KnowledgeMaterialOut,
    exported_content_slugs: set[str],
) -> str:
    """Render canonical Material relationships without inferring acquisition facts."""

    lines = [GENERATED_HEADER, "", f"# {material.name_ko}"]
    _section(
        lines,
        "Identity",
        [_fields([("key", material.key), ("name_ko", material.name_ko), ("unit", material.unit)])],
    )
    _section(
        lines,
        "Produced By Recipes",
        _named_blocks(
            (
                producer.recipe_slug,
                [
                    ("recipe_slug", producer.recipe_slug),
                    ("recipe_name_ko", producer.recipe_name_ko),
                    ("process_type", producer.process_type),
                    ("required_skill_tier", producer.required_skill_tier),
                    ("required_skill_level", producer.required_skill_level),
                    ("verification_status", producer.verification_status),
                    ("last_verified_at", producer.last_verified_at),
                    ("relative_path", f"../recipes/{producer.recipe_slug}.md"),
                ],
            )
            for producer in material.produced_by_recipes
        ),
    )
    _section(
        lines,
        "Explicit Recipe Usages",
        _named_blocks(
            (
                usage.option_seed_key,
                [
                    ("recipe_slug", usage.recipe_slug),
                    ("recipe_name_ko", usage.recipe_name_ko),
                    ("process_type", usage.process_type),
                    ("slot_seed_key", usage.slot_seed_key),
                    ("slot_label", usage.slot_label),
                    ("slot_order_no", usage.slot_order_no),
                    ("option_seed_key", usage.option_seed_key),
                    ("option_order_no", usage.option_order_no),
                    ("required_quantity", usage.required_quantity),
                    ("is_alternative", usage.is_alternative),
                    ("recipe_verification_status", usage.recipe_verification_status),
                    ("recipe_last_verified_at", usage.recipe_last_verified_at),
                    ("relative_path", f"../recipes/{usage.recipe_slug}.md"),
                ],
            )
            for usage in material.explicit_recipe_usages
        ),
    )
    membership_blocks: list[str] = []
    for membership in material.ingredient_group_memberships:
        membership_blocks.extend(
            _named_blocks(
                [
                    (
                        membership.member_seed_key,
                        [
                            ("group_key", membership.group_key),
                            ("group_name_ko", membership.group_name_ko),
                            ("member_seed_key", membership.member_seed_key),
                            ("member_order_no", membership.member_order_no),
                            ("group_verification_status", membership.group_verification_status),
                            ("group_last_verified_at", membership.group_last_verified_at),
                        ],
                    )
                ]
            )
        )
        membership_blocks.extend(["", "#### Evidence and Sources", ""])
        membership_blocks.extend(_evidence_blocks(membership.sources) or ["- None"])
    _section(lines, "Ingredient Group Memberships", membership_blocks)
    _section(
        lines,
        "Ingredient Group Candidate Recipe Usages",
        _named_blocks(
            (
                usage.option_seed_key,
                [
                    ("usage_semantics", usage.usage_semantics),
                    ("group_key", usage.group_key),
                    ("group_name_ko", usage.group_name_ko),
                    ("group_verification_status", usage.group_verification_status),
                    ("group_last_verified_at", usage.group_last_verified_at),
                    ("recipe_slug", usage.recipe_slug),
                    ("recipe_name_ko", usage.recipe_name_ko),
                    ("process_type", usage.process_type),
                    ("slot_seed_key", usage.slot_seed_key),
                    ("slot_label", usage.slot_label),
                    ("slot_order_no", usage.slot_order_no),
                    ("option_seed_key", usage.option_seed_key),
                    ("option_order_no", usage.option_order_no),
                    ("group_required_quantity", usage.group_required_quantity),
                    ("is_alternative", usage.is_alternative),
                    ("recipe_verification_status", usage.recipe_verification_status),
                    ("recipe_last_verified_at", usage.recipe_last_verified_at),
                    ("relative_path", f"../recipes/{usage.recipe_slug}.md"),
                ],
            )
            for usage in material.group_recipe_usages
        ),
    )
    project_blocks: list[str] = []
    for requirement in material.project_requirements:
        project_blocks.extend(
            _named_blocks(
                [
                    (
                        requirement.project_material_seed_key,
                        [
                            ("project_slug", requirement.project_slug),
                            ("project_name_ko", requirement.project_name_ko),
                            ("project_material_seed_key", requirement.project_material_seed_key),
                            ("stage_seed_key", requirement.stage_seed_key),
                            ("stage_name", requirement.stage_name),
                            ("required_quantity", requirement.required_quantity),
                            ("order_no", requirement.order_no),
                            ("notes", requirement.notes),
                            ("source_entity_type", requirement.source_entity_type),
                            ("source_entity_seed_key", requirement.source_entity_seed_key),
                            ("relative_path", f"../projects/{requirement.project_slug}.md"),
                        ],
                    )
                ]
            )
        )
        project_blocks.extend(["", "#### Scoped Acquisition Sources", ""])
        for source in requirement.sources:
            fields: list[tuple[str, object]] = [
                ("seed_key", source.seed_key),
                ("content_slug", source.content_slug),
                ("content_name_ko", source.content_name_ko),
                ("quantity_per_completion", source.quantity_per_completion),
                ("notes", source.notes),
                ("order_no", source.order_no),
            ]
            if source.content_slug in exported_content_slugs:
                fields.append(
                    ("relative_path", f"../contents/{source.content_slug}.md")
                )
            project_blocks.extend(_named_blocks([(source.seed_key, fields)]))
    _section(lines, "Project Requirements", project_blocks)
    _section(
        lines,
        "Semantics",
        [
            "- Material identity itself has no invented aggregate verification status.",
            "- Explicit Material usage and IngredientGroup candidate usage are different.",
            "- Group membership does not mean the material is mandatory.",
            "- Group required_quantity belongs to the Recipe group option.",
            "- Project acquisition sources are scoped to that ProjectMaterial requirement.",
            "- No personal inventory is included.",
            "- No market price or profitability is included.",
        ],
    )
    return "\n".join(lines).rstrip() + "\n"


def _render_index(
    contents: list[KnowledgeContentOut],
    projects: list[KnowledgeProjectOut],
    recipes: list[KnowledgeRecipeOut],
    materials: list[KnowledgeMaterialOut],
) -> str:
    lines = [
        GENERATED_HEADER,
        "",
        "# BDO Companion AI Export Index",
        "",
        "This directory is generated.",
        "Do not treat it as an independent Source of Truth.",
        "Canonical source remains the BDO Companion seed/domain model.",
        "",
        "## How to use",
        "",
        "1. Search this index or the GitHub repository.",
        "2. Open the matching Content, Project, Recipe or Material page.",
        "3. Prefer current verified evidence.",
        "4. Treat strategy and measurement separately from official fact.",
        "5. For personal state, use the caller/user source rather than this export.",
        "",
        "## Contents",
        "",
        "| Name | Slug | Category | Verification | Last verified | Path |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for content in sorted(
        contents, key=lambda item: (item.category, item.name_ko, item.slug)
    ):
        path = f"contents/{content.slug}.md"
        lines.append(
            "| "
            + " | ".join(
                [
                    content.name_ko.replace("|", "\\|"),
                    f"`{content.slug}`",
                    content.category.replace("|", "\\|"),
                    content.verification_status,
                    content.last_verified_at.isoformat()
                    if content.last_verified_at
                    else "null",
                    f"[open]({path})",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Projects",
            "",
            "| Name | Slug | Path |",
            "| --- | --- | --- |",
        ]
    )
    for project in sorted(projects, key=lambda item: (item.name_ko, item.slug)):
        path = f"projects/{project.slug}.md"
        lines.append(
            f"| {project.name_ko.replace('|', '\\|')} | `{project.slug}` | [open]({path}) |"
        )
    lines.extend(["", "## Recipes", "",
                  "| Name | Slug | Process | Result | Verification | Last verified | Path |",
                  "| --- | --- | --- | --- | --- | --- | --- |"])
    for r in sorted(recipes, key=lambda r: (r.name_ko, r.slug)):
        lines.append(f"| {r.name_ko} | {r.slug} | {r.process_type} | "
                     f"{r.result_material_name_ko} | {r.verification_status} | "
                     f"{r.last_verified_at} | [open](recipes/{r.slug}.md) |")
    lines.extend(
        [
            "",
            "## Materials",
            "",
            "| Name | Key | Unit | Path |",
            "| --- | --- | --- | --- |",
        ]
    )
    for material in sorted(materials, key=lambda item: (item.name_ko, item.key)):
        lines.append(
            f"| {material.name_ko} | {material.key} | {material.unit} | "
            f"[open](materials/{material.key}.md) |"
        )
    return "\n".join(lines).rstrip() + "\n"


def _render_manifest(
    contents: list[KnowledgeContentOut],
    projects: list[KnowledgeProjectOut],
    recipes: list[KnowledgeRecipeOut],
    materials: list[KnowledgeMaterialOut],
) -> str:
    payload = {
        "schema_version": 3,
        "material_count": len(materials),
        "materials": [
            {
                "key": material.key,
                "name_ko": material.name_ko,
                "unit": material.unit,
                "path": f"materials/{material.key}.md",
            }
            for material in sorted(materials, key=lambda item: item.key)
        ],
        "recipe_count": len(recipes),
        "recipes": [
            {"slug": r.slug, "name_ko": r.name_ko, "process_type": r.process_type,
             "result_material_key": r.result_material_key,
             "verification_status": r.verification_status,
             "last_verified_at": r.last_verified_at.isoformat() if r.last_verified_at else None,
             "path": f"recipes/{r.slug}.md"}
            for r in sorted(recipes, key=lambda r: r.slug)
        ],
        "content_count": len(contents),
        "project_count": len(projects),
        "contents": [
            {
                "slug": content.slug,
                "name_ko": content.name_ko,
                "category": content.category,
                "verification_status": content.verification_status,
                "last_verified_at": (
                    content.last_verified_at.isoformat()
                    if content.last_verified_at
                    else None
                ),
                "path": f"contents/{content.slug}.md",
            }
            for content in sorted(contents, key=lambda item: item.slug)
        ],
        "projects": [
            {
                "slug": project.slug,
                "name_ko": project.name_ko,
                "path": f"projects/{project.slug}.md",
            }
            for project in sorted(projects, key=lambda item: item.slug)
        ],
    }
    return json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"


def build_ai_exports(
    session: Session,
    *,
    now: datetime = STATIC_PROJECTION_TIME,
) -> dict[str, str]:
    """Build deterministic generated artifacts from canonical domain services."""

    content_slugs = list(
        session.scalars(
            select(Content.slug)
            .where(Content.status == "active")
            .order_by(Content.slug)
        ).all()
    )
    project_slugs = list(
        session.scalars(
            select(Project.slug)
            .where(Project.active.is_(True))
            .order_by(Project.slug)
        ).all()
    )

    contents = []
    for slug in content_slugs:
        content = get_knowledge_content(session, slug, now)
        if content is None:
            raise RuntimeError(f"Canonical Content disappeared during export: {slug}")
        contents.append(content)

    projects = []
    for slug in project_slugs:
        project = get_knowledge_project(session, slug)
        if project is None:
            raise RuntimeError(f"Canonical Project disappeared during export: {slug}")
        projects.append(project)

    exported_content_slugs = set(content_slugs)
    files = {
        f"contents/{content.slug}.md": render_content_markdown(
            content, exported_content_slugs
        )
        for content in contents
    }
    files.update(
        {
            f"projects/{project.slug}.md": render_project_markdown(
                project, exported_content_slugs
            )
            for project in projects
        }
    )
    recipes = []
    for slug in session.scalars(select(Recipe.slug).where(Recipe.active.is_(True)).order_by(Recipe.slug)):
        recipe = get_knowledge_recipe(session, slug)
        if recipe is None:
            raise RuntimeError(f"Canonical Recipe disappeared during export: {slug}")
        recipes.append(recipe)
    dependency_index = build_recipe_dependency_index(recipes)
    for recipe in recipes:
        files[f"recipes/{recipe.slug}.md"] = render_recipe_markdown(
            recipe,
            dependency_index[recipe.slug],
        )
    materials = list_knowledge_materials(session)
    files.update(
        {
            f"materials/{material.key}.md": render_material_markdown(
                material,
                exported_content_slugs,
            )
            for material in materials
        }
    )
    files["INDEX.md"] = _render_index(contents, projects, recipes, materials)
    files["manifest.json"] = _render_manifest(contents, projects, recipes, materials)
    return dict(sorted(files.items()))


def build_ai_exports_from_seed(
    *,
    directory: Path | None = None,
    now: datetime = STATIC_PROJECTION_TIME,
) -> dict[str, str]:
    """Import seed into an isolated in-memory DB and build the export map."""

    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    try:
        Base.metadata.create_all(engine)
        with Session(engine, expire_on_commit=False) as session:
            import_seed(session, directory or seed_dir())
            return build_ai_exports(session, now=now)
    finally:
        engine.dispose()


def _disk_files(output_dir: Path) -> dict[str, bytes]:
    if not output_dir.exists():
        return {}
    return {
        path.relative_to(output_dir).as_posix(): path.read_bytes()
        for path in sorted(output_dir.rglob("*"))
        if path.is_file()
    }


def compare_export_tree(
    expected: Mapping[str, str],
    output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> list[str]:
    """Return deterministic changed/missing/extra diagnostics without writing."""

    actual = _disk_files(output_dir)
    expected_bytes = {
        path: content.encode("utf-8") for path, content in expected.items()
    }
    changed = sorted(
        path
        for path in expected_bytes.keys() & actual.keys()
        if expected_bytes[path] != actual[path]
    )
    missing = sorted(expected_bytes.keys() - actual.keys())
    extra = sorted(actual.keys() - expected_bytes.keys())
    return [
        *[f"changed: {path}" for path in changed],
        *[f"missing: {path}" for path in missing],
        *[f"extra: {path}" for path in extra],
    ]


def write_export_tree(
    expected: Mapping[str, str],
    output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> None:
    """Synchronize one generated tree and remove only stale files inside it."""

    output_dir.mkdir(parents=True, exist_ok=True)
    expected_paths = set(expected)
    for relative_path in sorted(_disk_files(output_dir)):
        if relative_path not in expected_paths:
            (output_dir / relative_path).unlink()

    for relative_path, content in sorted(expected.items()):
        target = output_dir / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        encoded = content.encode("utf-8")
        if not target.exists() or target.read_bytes() != encoded:
            target.write_bytes(encoded)

    for directory in sorted(
        (path for path in output_dir.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        if not any(directory.iterdir()):
            directory.rmdir()


def _run(command: str) -> int:
    expected = build_ai_exports_from_seed()
    if command == "write":
        write_export_tree(expected)
        print(
            f"AI export written: {len(expected)} files "
            f"({sum(path.startswith('contents/') for path in expected)} contents, "
            f"{sum(path.startswith('projects/') for path in expected)} projects, "
            f"{sum(path.startswith('recipes/') for path in expected)} recipes, "
            f"{sum(path.startswith('materials/') for path in expected)} materials)"
        )
        return 0

    differences = compare_export_tree(expected)
    if differences:
        print("AI export is stale:", file=sys.stderr)
        for difference in differences:
            print(difference, file=sys.stderr)
        return 1
    print(f"AI export is current: {len(expected)} files")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build deterministic canonical-only AI export artifacts."
    )
    parser.add_argument("command", choices=("write", "check"))
    args = parser.parse_args()
    raise SystemExit(_run(args.command))


if __name__ == "__main__":
    main()
