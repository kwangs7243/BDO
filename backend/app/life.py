from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import UTC

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.content import aggregate_verification
from app.models import Content, Evidence, Project
from app.schemas import (
    LifeContentOut,
    LifeHubOut,
    LifeProgressOut,
    LifeProjectOut,
    LifeSkillDetailOut,
    LifeSkillSummaryOut,
    UserContentStateOut,
)


FOUNDATION_SLUGS = (
    "life-family-levels",
    "life-mastery-foundation",
    "life-common-gear",
    "life-accessory-progression",
    "life-mastery-tools",
    "life-artifacts-lightstones",
    "life-alchemy-stones",
    "cheongmyeong-orb",
    "energy-foundation",
)

ECONOMY_SLUGS = (
    "contribution-economy-foundation",
    "node-network-current-system",
    "production-node-current-system",
    "production-node-2026-overhaul",
    "worker-current-system",
    "worker-races-grades",
    "worker-growth-promotion",
    "worker-skills-luck",
    "worker-special-delivery",
    "worker-stamina-auto-recovery",
    "worker-market",
    "housing-life-economy",
    "worker-lodging",
    "workshop-crafting-logistics",
    "storage-current-system",
    "storage-transport",
    "magnus-remote-storage",
    "family-silver-unification",
    "royal-workshop-current-system",
    "royal-workshop-worker-effects",
)


@dataclass(frozen=True)
class LifeSkillPresentation:
    key: str
    name_ko: str
    entry_content_slug: str
    foundation_contents: tuple[str, ...] = ()
    getting_started: tuple[str, ...] = ()
    equipment: tuple[str, ...] = ()
    core_systems: tuple[str, ...] = ()
    recurring_contents: tuple[str, ...] = ()
    advanced_contents: tuple[str, ...] = ()
    related_economy: tuple[str, ...] = ()

    def section_slugs(self) -> dict[str, tuple[str, ...]]:
        return {
            "foundation_contents": self.foundation_contents,
            "getting_started": self.getting_started,
            "equipment": self.equipment,
            "core_systems": self.core_systems,
            "recurring_contents": self.recurring_contents,
            "advanced_contents": self.advanced_contents,
            "related_economy": self.related_economy,
        }

    def all_slugs(self) -> tuple[str, ...]:
        return tuple(slug for slugs in self.section_slugs().values() for slug in slugs)


# This configuration controls presentation only. Names, summaries, facts, verification,
# and user state always come from canonical Content data.
LIFE_SKILLS = (
    LifeSkillPresentation(
        key="gathering",
        name_ko="채집",
        entry_content_slug="gathering-current-system",
        foundation_contents=("life-family-levels", "life-mastery-foundation", "energy-foundation"),
        getting_started=("gathering-current-system",),
        equipment=("gathering-tools", "life-common-gear", "life-mastery-tools"),
        core_systems=("life-mastery-effects", "gathering-special-drops"),
        advanced_contents=("gathering-green-artisan-minigames",),
        related_economy=("production-node-current-system",),
    ),
    LifeSkillPresentation(
        key="fishing",
        name_ko="낚시",
        entry_content_slug="fishing-current-system",
        foundation_contents=("life-family-levels", "life-mastery-foundation"),
        getting_started=("fishing-current-system",),
        equipment=("life-common-gear", "life-mastery-tools", "life-artifacts-lightstones"),
        core_systems=("auto-fishing", "fish-freshness-and-trade", "treasure-grade-fish"),
        recurring_contents=("imperial-fishing-delivery", "fishing-encyclopedia-and-weekly-contest"),
        advanced_contents=("mystical-fish-tank", "carrack-sailor-fishing"),
        related_economy=("storage-current-system", "storage-transport"),
    ),
    LifeSkillPresentation(
        key="farming",
        name_ko="재배",
        entry_content_slug="farming-current-cycle",
        foundation_contents=("life-family-levels", "life-mastery-foundation", "energy-foundation"),
        getting_started=("farming-current-cycle",),
        equipment=("farming-fences", "old-moon-seed-pouch"),
        core_systems=("farming-seeds-harvest-breeding",),
        advanced_contents=("farming-moles",),
        related_economy=("production-node-current-system", "worker-current-system"),
    ),
    LifeSkillPresentation(
        key="processing",
        name_ko="가공",
        entry_content_slug="processing-current-system",
        foundation_contents=("life-family-levels", "life-mastery-foundation"),
        getting_started=("processing-current-system",),
        equipment=("processing-stones-and-clothes", "life-common-gear", "life-mastery-tools"),
        core_systems=("mass-processing",),
        related_economy=("workshop-crafting-logistics", "storage-current-system"),
    ),
    LifeSkillPresentation(
        key="cooking",
        name_ko="요리",
        entry_content_slug="cooking-current-system",
        foundation_contents=("life-family-levels", "life-mastery-foundation"),
        getting_started=("cooking-current-system",),
        equipment=("life-common-gear", "life-mastery-tools", "life-artifacts-lightstones"),
        core_systems=("cooking-mastery-effects", "cooking-mass-production", "witch-delicacy"),
        recurring_contents=("cooking-growth-surprise-quest", "imperial-crafting-delivery-daily"),
        related_economy=("housing-life-economy", "storage-current-system"),
    ),
    LifeSkillPresentation(
        key="alchemy",
        name_ko="연금",
        entry_content_slug="alchemy-current-system",
        foundation_contents=("life-family-levels", "life-mastery-foundation"),
        getting_started=("alchemy-current-system",),
        equipment=("life-common-gear", "life-mastery-tools", "life-artifacts-lightstones"),
        core_systems=(
            "alchemy-mastery-effects",
            "alchemy-products-and-byproducts",
            "alchemy-stone-current-progression",
        ),
        recurring_contents=("alchemy-growth-surprise-quest", "alchemy-imperial-current"),
        advanced_contents=("alchemy-stone-growth", "life-alchemy-stones"),
        related_economy=("housing-life-economy", "storage-current-system"),
    ),
    LifeSkillPresentation(
        key="training",
        name_ko="조련",
        entry_content_slug="training-current-system",
        foundation_contents=("life-family-levels", "life-mastery-foundation"),
        getting_started=("training-current-system", "wild-horse-capture"),
        equipment=("life-common-gear", "life-mastery-tools", "life-artifacts-lightstones"),
        core_systems=(
            "training-mastery-effects",
            "horse-breeding-exchange",
            "horse-imperial-delivery",
            "courser-system",
        ),
        recurring_contents=("training-growth-surprise-quest", "dream-horse-material-routines"),
        advanced_contents=("dream-horse-awakening", "mythical-dream-horse"),
    ),
    LifeSkillPresentation(
        key="hunting",
        name_ko="수렵",
        entry_content_slug="hunting-current-system",
        foundation_contents=("life-family-levels", "life-mastery-foundation", "energy-foundation"),
        getting_started=("hunting-current-system",),
        equipment=("hunting-firearms", "marni-sniper-rifle", "life-common-gear"),
        core_systems=("hunting-mastery-effects", "sniper-hunting"),
        recurring_contents=("hunting-growth-surprise-quest",),
        advanced_contents=("group-hunting-whale-khalk",),
        related_economy=("cooking-current-system", "alchemy-current-system"),
    ),
    LifeSkillPresentation(
        key="sailing",
        name_ko="항해",
        entry_content_slug="carrack-types",
        foundation_contents=("life-family-levels", "life-mastery-foundation"),
        getting_started=("carrack-types", "sailor-hiring-growth"),
        equipment=(
            "ocean-consumables",
            "sailor-health-food",
            "sailor-role-slots",
            "ocean-first-mates",
            "sea-crystals",
            "carrack-chiro-gear",
            "carrack-palasi-gear",
            "carrack-palasi-enhancement",
        ),
        core_systems=("carrack-advance", "carrack-upgrade-materials"),
        recurring_contents=(
            "ocean-supply-transport-oquilla",
            "oquilla-daily-young-sea-monster-hunter",
            "oquilla-daily-black-rust-hunter",
            "oquilla-daily-candidum-hunter",
            "oquilla-daily-nineshark-hunter",
            "oquilla-weekly-black-rust-hunter",
            "oquilla-weekly-candidum-hunter",
            "oquilla-weekly-nineshark-hunter",
        ),
        advanced_contents=(
            "panokseon",
            "panokseon-haemo-byeokgye",
            "panokseon-cheongun",
            "ebenruth-nol",
            "sea-crocodile-hunting",
            "lekrashan-hunting",
            "hollow-maretta",
            "rinbach-colony",
        ),
        related_economy=("storage-current-system", "family-silver-unification"),
    ),
    LifeSkillPresentation(
        key="barter",
        name_ko="교역/물물교환",
        entry_content_slug="barter-current-system",
        foundation_contents=("life-family-levels", "life-mastery-foundation"),
        getting_started=("barter-current-system",),
        equipment=("ocean-consumables",),
        core_systems=("barter-stage-values", "barter-tier6-routes", "barter-tier7-routes"),
        recurring_contents=("ocean-iliya-daily-barter", "iliya-weekly-barter"),
        advanced_contents=("barter-route-strategy", "crow-coin-material-shop", "carrack-advance"),
        related_economy=("storage-current-system", "storage-transport", "family-silver-unification"),
    ),
)

LIFE_SKILLS_BY_KEY = {item.key: item for item in LIFE_SKILLS}


def _all_configured_slugs() -> set[str]:
    slugs = {*FOUNDATION_SLUGS, *ECONOMY_SLUGS}
    for skill in LIFE_SKILLS:
        slugs.update(skill.all_slugs())
    return slugs


def _load_content_cards(session: Session) -> dict[str, LifeContentOut]:
    slugs = _all_configured_slugs()
    contents = list(
        session.scalars(
            select(Content)
            .where(Content.slug.in_(slugs), Content.status == "active")
            .options(selectinload(Content.user_state))
            .order_by(Content.slug)
        ).all()
    )
    evidence_by_slug: dict[str, list[Evidence]] = defaultdict(list)
    if contents:
        evidence_rows = session.scalars(
            select(Evidence)
            .where(
                Evidence.entity_type == "content",
                Evidence.entity_id.in_([item.slug for item in contents]),
            )
            .order_by(Evidence.entity_id, Evidence.claim_key, Evidence.id)
        ).all()
        for evidence in evidence_rows:
            evidence_by_slug[evidence.entity_id].append(evidence)

    cards: dict[str, LifeContentOut] = {}
    for content in contents:
        state = content.user_state
        cards[content.slug] = LifeContentOut(
            slug=content.slug,
            name_ko=content.name_ko,
            category=content.category,
            subcategory=content.subcategory,
            summary=content.summary,
            verification_status=aggregate_verification(evidence_by_slug[content.slug]),
            last_verified_at=content.last_verified_at,
            user_state=UserContentStateOut(
                state=state.state if state else "not_started",
                priority=state.priority if state else None,
                note=state.note if state else None,
                updated_at=(
                    state.updated_at.replace(tzinfo=UTC)
                    if state and state.updated_at.tzinfo is None
                    else state.updated_at if state else None
                ),
            ),
        )
    return cards


def _ordered_cards(
    cards: dict[str, LifeContentOut],
    slugs: tuple[str, ...],
    seen: set[str] | None = None,
) -> list[LifeContentOut]:
    output = []
    for slug in slugs:
        if slug not in cards or (seen is not None and slug in seen):
            continue
        output.append(cards[slug])
        if seen is not None:
            seen.add(slug)
    return output


def _progress(contents: list[LifeContentOut]) -> LifeProgressOut:
    counts = Counter(item.user_state.state.value for item in contents)
    total = len(contents)
    ignored = counts["ignore"]
    return LifeProgressOut(
        total=total,
        tracked=total - ignored,
        not_started=counts["not_started"],
        foundation=counts["foundation"],
        in_progress=counts["in_progress"],
        completed=counts["completed"],
        paused=counts["paused"],
        ignored=ignored,
    )


def _skill_sections(
    skill: LifeSkillPresentation,
    cards: dict[str, LifeContentOut],
) -> dict[str, list[LifeContentOut]]:
    seen: set[str] = set()
    return {
        name: _ordered_cards(cards, slugs, seen)
        for name, slugs in skill.section_slugs().items()
    }


def _skill_summary(
    skill: LifeSkillPresentation,
    cards: dict[str, LifeContentOut],
) -> LifeSkillSummaryOut | None:
    entry = cards.get(skill.entry_content_slug)
    if entry is None:
        return None
    sections = _skill_sections(skill, cards)
    contents = [item for section in sections.values() for item in section]
    return LifeSkillSummaryOut(
        key=skill.key,
        name_ko=skill.name_ko,
        summary=entry.summary,
        verification_status=entry.verification_status,
        last_verified_at=entry.last_verified_at,
        content_count=len(contents),
        user_progress=_progress(contents),
        entry_content_slug=entry.slug,
    )


def get_life_hub(session: Session) -> LifeHubOut:
    cards = _load_content_cards(session)
    return LifeHubOut(
        foundations=_ordered_cards(cards, FOUNDATION_SLUGS),
        economy_contents=_ordered_cards(cards, ECONOMY_SLUGS),
        skills=[
            summary
            for skill in LIFE_SKILLS
            if (summary := _skill_summary(skill, cards)) is not None
        ],
    )


def get_life_skill(session: Session, key: str) -> LifeSkillDetailOut | None:
    skill = LIFE_SKILLS_BY_KEY.get(key)
    if skill is None:
        return None
    cards = _load_content_cards(session)
    summary = _skill_summary(skill, cards)
    if summary is None:
        return None
    sections = _skill_sections(skill, cards)
    content_ids = list(
        session.scalars(
            select(Content.id).where(
                Content.slug.in_({
                    item.slug
                    for section in sections.values()
                    for item in section
                })
            )
        ).all()
    )
    projects = (
        list(
            session.scalars(
                select(Project)
                .where(Project.active.is_(True), Project.content_id.in_(content_ids))
                .options(selectinload(Project.content))
                .order_by(Project.slug)
            ).all()
        )
        if content_ids
        else []
    )
    return LifeSkillDetailOut(
        **summary.model_dump(),
        **sections,
        related_projects=[
            LifeProjectOut(
                slug=project.slug,
                name_ko=project.name_ko,
                summary=project.summary,
                content_slug=project.content.slug if project.content else None,
            )
            for project in projects
        ],
    )
