<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 도깨비숲

## Identity

- slug: "dokkebi-forest"
- name_ko: "도깨비숲"
- category: "combat"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "새벽의 정수·수정 성장 목적을 포함해 평가해야 하는 사냥터."
- purpose: "새벽의 정수 및 수정 성장 재료 획득"

## Requirements

### `dokkebi-forest.current-stats`

- seed_key: "dokkebi-forest.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 공격력 335, 공격력 상한 1445."
- structured_value:

```json
{
  "ap_cap": 1445,
  "knowledge_role": "fact",
  "sheet_ap_recommended": 335
}
```

### `dokkebi-forest.rework-2025`

- seed_key: "dokkebi-forest.rework-2025"
- kind: "stat"
- requirement_level: "optional"
- title: "2025 전투 개편"
- description: "몬스터 방어력 32% 조정."
- structured_value:

```json
{
  "effective_from": "2025-07-23",
  "knowledge_role": "fact",
  "monster_defense_change_percent": 32
}
```

### `dokkebi-forest.strategy-purpose`

- seed_key: "dokkebi-forest.strategy-purpose"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "성장 목적 비교"
- description: "툰그라드와 성장 재료 목적이 달라 은화만으로 순위를 정하지 않는다."
- structured_value:

```json
{
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "tags": [
    "progression_material_sensitive",
    "agris_strategy_sensitive"
  ]
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

- None

## Related Contents

### `dokkebi-forest.attack-cap`

- seed_key: "dokkebi-forest.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `dokkebi-forest.tungrad`

- seed_key: "dokkebi-forest.tungrad"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "tungrad-ruins"
- content_name_ko: "툰그라드 유적지"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/tungrad-ruins.md"

## Evidence and Sources

### Current evidence

### `dokkebi-forest.claim.current-stats::combat-system-rework-2025-07-23`

- evidence_seed_key: "dokkebi-forest.claim.current-stats::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dokkebi-forest.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `dokkebi-forest.claim.rework-2025::combat-system-rework-2025-07-23`

- evidence_seed_key: "dokkebi-forest.claim.rework-2025::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dokkebi-forest.rework-2025"
- claim_key: "requirement:rework-2025"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `dokkebi-forest.claim.strategy-purpose::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "dokkebi-forest.claim.strategy-purpose::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dokkebi-forest.strategy-purpose"
- claim_key: "requirement:strategy-purpose"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
