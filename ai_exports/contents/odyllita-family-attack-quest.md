<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 오드락시아 가문 공격력 의뢰

## Identity

- slug: "odyllita-family-attack-quest"
- name_ko: "오드락시아 가문 공격력 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "오드락시아 메인 의뢰 2부 뒤 가문 공격력 1을 영구 획득하는 일회성 후속 의뢰다."
- purpose: "지역 완료와 실제 영구 능력치 수령 체크포인트를 분리해 추적한다."

## Requirements

### `odyllita-family-attack-quest.unlock`

- seed_key: "odyllita-family-attack-quest.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "어머니의 신탁"
- description: "오드락시아 메인 의뢰 2부 [하둠의 영역] 완료 뒤 [특별한 선물] 어머니의 신탁을 완료한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "persistence": "permanent",
  "prerequisite": "Odyllita part 2 - Hadum's Realm",
  "quest": "[특별한 선물] 어머니의 신탁",
  "repeatable": false,
  "scope": "family"
}
```

## Steps

### `odyllita-family-attack-quest.step.complete`

- seed_key: "odyllita-family-attack-quest.step.complete"
- phase: "reward"
- order_no: 1
- title: "가문 공격력 수령"
- description: "후속 의뢰를 완료하고 가문 공격력 1 적용을 확인한다."
- checkable: false

## Schedules

- None

## Rewards

### `odyllita-family-attack-quest.reward.family-ap`

- seed_key: "odyllita-family-attack-quest.reward.family-ap"
- name: "가문 공격력"
- reward_type: "fixed_effect"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "point"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "가문 영구 적용"
- order_no: 1

## Sections

- None

## Related Contents

### `odyllita-family-attack-quest.parent`

- seed_key: "odyllita-family-attack-quest.parent"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "permanent-family-reward-foundation"
- content_name_ko: "영구 가문 보상 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/permanent-family-reward-foundation.md"
### `odyllita-family-attack-quest.main`

- seed_key: "odyllita-family-attack-quest.main"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "main-quest-odyllita"
- content_name_ko: "오드락시아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-odyllita.md"
### `odyllita-family-attack-quest.stats`

- seed_key: "odyllita-family-attack-quest.stats"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "permanent-stat-progression"
- content_name_ko: "영구 능력치 성장"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/permanent-stat-progression.md"
### `main-quest-odyllita.family-ap`

- seed_key: "main-quest-odyllita.family-ap"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "main-quest-odyllita"
- content_name_ko: "오드락시아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/main-quest-odyllita.md"

## Evidence and Sources

### Current evidence

### `odyllita-family-attack-quest.claim.unlock::family-stat-quest-history`

- evidence_seed_key: "odyllita-family-attack-quest.claim.unlock::family-stat-quest-history"
- source_id: "family-stat-quest-history"
- title: "Kamasylvia and Odyllita Family Stat Quest History"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9723"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "odyllita-family-attack-quest.unlock"
- claim_key: "requirement:unlock"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `odyllita-family-attack-quest.claim.step::family-stat-quest-history`

- evidence_seed_key: "odyllita-family-attack-quest.claim.step::family-stat-quest-history"
- source_id: "family-stat-quest-history"
- title: "Kamasylvia and Odyllita Family Stat Quest History"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9723"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "odyllita-family-attack-quest.step.complete"
- claim_key: "step:complete"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `odyllita-family-attack-quest.claim.reward::family-stat-quest-history`

- evidence_seed_key: "odyllita-family-attack-quest.claim.reward::family-stat-quest-history"
- source_id: "family-stat-quest-history"
- title: "Kamasylvia and Odyllita Family Stat Quest History"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9723"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "odyllita-family-attack-quest.reward.family-ap"
- claim_key: "reward:family-ap"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `odyllita-family-attack-quest.claim.reward::hyperboost-progression-2026`

- evidence_seed_key: "odyllita-family-attack-quest.claim.reward::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "odyllita-family-attack-quest.reward.family-ap"
- claim_key: "reward:family-ap"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
