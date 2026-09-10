<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 카마실비아 가문 방어력 의뢰

## Identity

- slug: "kamasylvia-family-defense-quest"
- name_ko: "카마실비아 가문 방어력 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "카마실비아 메인 의뢰 뒤 가문 방어력 1을 영구 획득하는 일회성 후속 의뢰다."
- purpose: "지역 완료와 실제 영구 능력치 수령 체크포인트를 분리해 추적한다."

## Requirements

### `kamasylvia-family-defense-quest.unlock`

- seed_key: "kamasylvia-family-defense-quest.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "파푸에게 주는 선물"
- description: "카마실비아 메인 의뢰로 관련 지식을 얻은 뒤 [특별한 선물] 파푸에게 주는 선물을 완료한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "persistence": "permanent",
  "quest": "[특별한 선물] 파푸에게 주는 선물",
  "repeatable": false,
  "scope": "family"
}
```

## Steps

### `kamasylvia-family-defense-quest.step.complete`

- seed_key: "kamasylvia-family-defense-quest.step.complete"
- phase: "reward"
- order_no: 1
- title: "가문 방어력 수령"
- description: "후속 의뢰를 완료하고 가문 방어력 1 적용을 확인한다."
- checkable: false

## Schedules

- None

## Rewards

### `kamasylvia-family-defense-quest.reward.family-dp`

- seed_key: "kamasylvia-family-defense-quest.reward.family-dp"
- name: "가문 방어력"
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

### `kamasylvia-family-defense-quest.parent`

- seed_key: "kamasylvia-family-defense-quest.parent"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "permanent-family-reward-foundation"
- content_name_ko: "영구 가문 보상 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/permanent-family-reward-foundation.md"
### `kamasylvia-family-defense-quest.main`

- seed_key: "kamasylvia-family-defense-quest.main"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "main-quest-kamasylvia"
- content_name_ko: "카마실비아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-kamasylvia.md"
### `kamasylvia-family-defense-quest.stats`

- seed_key: "kamasylvia-family-defense-quest.stats"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "permanent-stat-progression"
- content_name_ko: "영구 능력치 성장"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/permanent-stat-progression.md"
### `main-quest-kamasylvia.family-dp`

- seed_key: "main-quest-kamasylvia.family-dp"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "main-quest-kamasylvia"
- content_name_ko: "카마실비아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/main-quest-kamasylvia.md"

## Evidence and Sources

### Current evidence

### `kamasylvia-family-defense-quest.claim.unlock::family-stat-quest-history`

- evidence_seed_key: "kamasylvia-family-defense-quest.claim.unlock::family-stat-quest-history"
- source_id: "family-stat-quest-history"
- title: "Kamasylvia and Odyllita Family Stat Quest History"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9723"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "kamasylvia-family-defense-quest.unlock"
- claim_key: "requirement:unlock"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `kamasylvia-family-defense-quest.claim.step::family-stat-quest-history`

- evidence_seed_key: "kamasylvia-family-defense-quest.claim.step::family-stat-quest-history"
- source_id: "family-stat-quest-history"
- title: "Kamasylvia and Odyllita Family Stat Quest History"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9723"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "kamasylvia-family-defense-quest.step.complete"
- claim_key: "step:complete"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `kamasylvia-family-defense-quest.claim.reward::family-stat-quest-history`

- evidence_seed_key: "kamasylvia-family-defense-quest.claim.reward::family-stat-quest-history"
- source_id: "family-stat-quest-history"
- title: "Kamasylvia and Odyllita Family Stat Quest History"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9723"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "kamasylvia-family-defense-quest.reward.family-dp"
- claim_key: "reward:family-dp"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `kamasylvia-family-defense-quest.claim.reward::hyperboost-progression-2026`

- evidence_seed_key: "kamasylvia-family-defense-quest.claim.reward::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "kamasylvia-family-defense-quest.reward.family-dp"
- claim_key: "reward:family-dp"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
