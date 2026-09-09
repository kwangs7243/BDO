from __future__ import annotations

from collections.abc import Mapping

from sqlalchemy.orm import Session

from app.knowledge import get_knowledge_project
from app.schemas import (
    KnowledgeProjectOut,
    ProjectCalculationMaterialOut,
    ProjectCalculationOut,
    ProjectCalculationRequest,
    ProjectCalculationSummaryOut,
)


def calculate_shortage(required_quantity: float, provided_quantity: float) -> float:
    """Return a non-negative shortage shared by local and stateless projections."""

    return max(required_quantity - provided_quantity, 0.0)


def calculate_project_requirements(
    project: KnowledgeProjectOut,
    provided_quantities: Mapping[str, float],
) -> ProjectCalculationOut:
    """Combine canonical Project rows with ephemeral caller-provided quantities."""

    canonical_keys = {material.material_key for material in project.materials}
    unknown_keys = sorted(set(provided_quantities) - canonical_keys)
    if unknown_keys:
        raise ValueError(f"Unknown project material keys: {', '.join(unknown_keys)}")

    materials: list[ProjectCalculationMaterialOut] = []
    for material in project.materials:
        provided_quantity = float(provided_quantities.get(material.material_key, 0.0))
        shortage = calculate_shortage(material.required_quantity, provided_quantity)
        materials.append(
            ProjectCalculationMaterialOut(
                project_material_seed_key=material.seed_key,
                material_key=material.material_key,
                name_ko=material.name_ko,
                unit=material.unit,
                stage_seed_key=material.stage_seed_key,
                required_quantity=material.required_quantity,
                provided_quantity=provided_quantity,
                shortage=shortage,
                satisfied=shortage == 0,
            )
        )

    satisfied_count = sum(material.satisfied for material in materials)
    requirement_count = len(materials)
    return ProjectCalculationOut(
        project_slug=project.slug,
        name_ko=project.name_ko,
        materials=materials,
        summary=ProjectCalculationSummaryOut(
            material_requirement_count=requirement_count,
            satisfied_requirement_count=satisfied_count,
            shortage_requirement_count=requirement_count - satisfied_count,
            all_requirements_satisfied=satisfied_count == requirement_count,
        ),
    )


def calculate_project(
    session: Session,
    slug: str,
    request: ProjectCalculationRequest,
) -> ProjectCalculationOut:
    """Resolve canonical knowledge and calculate without reading local user state."""

    project = get_knowledge_project(session, slug)
    if project is None:
        raise LookupError(slug)
    provided_quantities = {
        item.material_key: float(item.quantity)
        for item in request.inventory
    }
    return calculate_project_requirements(project, provided_quantities)