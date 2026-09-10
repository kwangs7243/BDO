<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일반 자동 낚시

## Identity

- slug: "auto-fishing"
- name_ko: "일반 자동 낚시"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "물고기가 걸린 뒤 미니게임을 시작하지 않으면 기본 180초 후 자동 완료되며 감소 효과를 적용해도 최소 60초다."
- purpose: "일반 캐릭터 자동 낚시의 타이머와 감소 효과를 중범선 선원 낚시와 분리한다."

## Requirements

### `auto-fishing.timer`

- seed_key: "auto-fishing.timer"
- kind: "stat"
- requirement_level: "required"
- title: "기본·최소 시간"
- description: "일반 자동 낚시 완료 대기는 기본 180초이며 최소 60초다."
- structured_value:

```json
{
  "base_completion_seconds": 180,
  "minimum_seconds": 60
}
```

### `auto-fishing.reductions`

- seed_key: "auto-fishing.reductions"
- kind: "gear"
- requirement_level: "required"
- title: "시간 감소"
- description: "+10 발레노스 낚싯대는 25%를 줄이고 같은 효과 반려동물 여러 마리의 효과는 중첩되지 않는다."
- structured_value:

```json
{
  "balenos_rod_plus_10_percent": 25,
  "representative_pet_types": [
    "길 잃은 펭귄",
    "마못",
    "해달"
  ],
  "same_effect_pet_stacks": false
}
```

### `auto-fishing.distinct-from-sailor`

- seed_key: "auto-fishing.distinct-from-sailor"
- kind: "other"
- requirement_level: "required"
- title: "중범선 선원 낚시와 구분"
- description: "V1.6D 중범선 선원 낚시의 고정 180초 주기는 일반 자동 낚시 감소 시스템과 별도다."
- structured_value:

```json
{
  "normal_timer_reductions_apply_to_sailor_system": false,
  "same_timer_system_as_carrack_sailor_fishing": false
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

### `auto-fishing.system`

- seed_key: "auto-fishing.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "fishing-current-system"
- content_name_ko: "낚시 현재 시스템"
- content_category: "life"
- note: "일반 낚시의 자동 처리"
- order_no: 1
- relative_path: "../contents/fishing-current-system.md"
### `auto-fishing.sailor`

- seed_key: "auto-fishing.sailor"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-sailor-fishing"
- content_name_ko: "중범선 선원 낚시"
- content_category: "ocean_guide"
- note: "서로 다른 자동 낚시 mechanic"
- order_no: 2
- relative_path: "../contents/carrack-sailor-fishing.md"
### `auto-fishing.tank`

- seed_key: "auto-fishing.tank"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "mystical-fish-tank"
- content_name_ko: "심청의 신묘한 어항"
- content_category: "life"
- note: "가방 내 어항 자동 보관"
- order_no: 3
- relative_path: "../contents/mystical-fish-tank.md"
### `mystical-fish-tank.auto`

- seed_key: "mystical-fish-tank.auto"
- direction: "incoming"
- relation_type: "related"
- content_slug: "mystical-fish-tank"
- content_name_ko: "심청의 신묘한 어항"
- content_category: "life"
- note: "일반 자동 낚시 결과 보관"
- order_no: 1
- relative_path: "../contents/mystical-fish-tank.md"
### `fishing-current-system.auto`

- seed_key: "fishing-current-system.auto"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-current-system"
- content_name_ko: "낚시 현재 시스템"
- content_category: "life"
- note: "일반 자동 낚시"
- order_no: 2
- relative_path: "../contents/fishing-current-system.md"
### `fishing-onboarding-strategy.auto`

- seed_key: "fishing-onboarding-strategy.auto"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-onboarding-strategy"
- content_name_ko: "낚시 입문 전략"
- content_category: "life"
- note: "자동 낚시 시간과 방생 설정의 현재 규칙을 확인한다."
- order_no: 2
- relative_path: "../contents/fishing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `auto-fishing.summary::fishing-advanced-guide`

- evidence_seed_key: "auto-fishing.summary::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "auto-fishing"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "기본 180초·최소 60초"
- active: true
- is_active: true

### `auto-fishing.requirement.distinct-from-sailor::carrack-sailor-fishing-2025`

- evidence_seed_key: "auto-fishing.requirement.distinct-from-sailor::carrack-sailor-fishing-2025"
- source_id: "carrack-sailor-fishing-2025"
- title: "중범선 선원 자동 낚시"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13994"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "auto-fishing.distinct-from-sailor"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 자동 낚시와 선원 낚시 분리"
- active: true
- is_active: true

### `auto-fishing.requirement.distinct-from-sailor::fishing-advanced-guide`

- evidence_seed_key: "auto-fishing.requirement.distinct-from-sailor::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "auto-fishing.distinct-from-sailor"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 자동 낚시와 선원 낚시 분리"
- active: true
- is_active: true

### `auto-fishing.requirement.reductions::fishing-advanced-guide`

- evidence_seed_key: "auto-fishing.requirement.reductions::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "auto-fishing.reductions"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "발레노스 낚싯대·반려동물 중첩"
- active: true
- is_active: true

### `auto-fishing.requirement.timer::fishing-advanced-guide`

- evidence_seed_key: "auto-fishing.requirement.timer::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "auto-fishing.timer"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 자동 낚시 시간"
- active: true
- is_active: true

### Historical / inactive evidence

- None
