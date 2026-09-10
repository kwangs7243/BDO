<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 재배 현재 주기

## Identity

- slug: "farming-current-cycle"
- name_ko: "재배 현재 주기"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "2026-06-04 이후 작물의 기본 성장 시간은 온도 적합도에 따라 20·21·22시간이며 비료 아이템은 삭제됐다."
- purpose: "과거 재배 가이드의 성장시간·비료를 최신 KR Live 규칙으로 교정한다."

## Requirements

### `farming-current-cycle.growth-time`

- seed_key: "farming-current-cycle.growth-time"
- kind: "stat"
- requirement_level: "required"
- title: "온도별 성장 시간"
- description: "적합 20시간, 부적합 21시간, 매우 부적합 22시간이다."
- structured_value:

```json
{
  "suitable_hours": 20,
  "unsuitable_hours": 21,
  "very_unsuitable_hours": 22
}
```

### `farming-current-cycle.delays`

- seed_key: "farming-current-cycle.delays"
- kind: "other"
- requirement_level: "required"
- title: "성장 지연 요소"
- description: "벌레, 가지치기 필요, 새 피해 등은 실제 완료 시간을 늘릴 수 있다."
- structured_value:

```json
{
  "can_extend_completion": [
    "pests",
    "pruning_needed",
    "bird_damage"
  ]
}
```

### `farming-current-cycle.bird-damage`

- seed_key: "farming-current-cycle.bird-damage"
- kind: "stat"
- requirement_level: "required"
- title: "새 공격 건강 감소"
- description: "2026-06-10 이후 새 공격 1회당 작물 건강 감소는 약 0.25%다."
- structured_value:

```json
{
  "effective_from": "2026-06-10",
  "health_reduction_percent_approx": 0.25,
  "knowledge_role": "fact",
  "previous_percent_approx": 4.16
}
```

### `farming-current-cycle.moisture`

- seed_key: "farming-current-cycle.moisture"
- kind: "stat"
- requirement_level: "required"
- title: "수분 감소"
- description: "작물 수분 감소 속도는 개편 전의 1/5로 줄었고 물주기 기능은 유지된다."
- structured_value:

```json
{
  "rate_relative_to_previous": 0.2,
  "watering_mechanic_active": true
}
```

### `farming-current-cycle.fertilizers`

- seed_key: "farming-current-cycle.fertilizers"
- kind: "item"
- requirement_level: "required"
- title: "삭제된 비료"
- description: "성장시간 단축에 쓰던 비료 3종은 삭제됐다."
- structured_value:

```json
{
  "active_usable_item_count": 0,
  "deleted": [
    "무기질 비료",
    "부산물 비료",
    "유기질 비료"
  ],
  "knowledge_may_remain": true
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `farming-current-cycle.guide-conflict`

- seed_key: "farming-current-cycle.guide-conflict"
- section_type: "common_mistakes"
- title: "최신 패치 우선"
- order_no: 1

#### body_markdown

현재 가이드에 남은 과거 작물별 짧은 성장시간이나 비료 사용 설명을 canonical 현재 규칙으로 사용하지 않는다.

## Related Contents

### `farming-current-cycle.fences`

- seed_key: "farming-current-cycle.fences"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-fences"
- content_name_ko: "재배 울타리"
- content_category: "life"
- note: "재배 울타리"
- order_no: 1
- relative_path: "../contents/farming-fences.md"
### `farming-current-cycle.seeds`

- seed_key: "farming-current-cycle.seeds"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-seeds-harvest-breeding"
- content_name_ko: "재배 씨앗·수확·품종개량"
- content_category: "life"
- note: "씨앗·수확·품종개량"
- order_no: 2
- relative_path: "../contents/farming-seeds-harvest-breeding.md"
### `farming-current-cycle.moles`

- seed_key: "farming-current-cycle.moles"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-moles"
- content_name_ko: "재배 두더지와 슈슈"
- content_category: "life"
- note: "수확·품종개량 중 두더지"
- order_no: 3
- relative_path: "../contents/farming-moles.md"
### `farming-fences.cycle`

- seed_key: "farming-fences.cycle"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "farming-fences"
- content_name_ko: "재배 울타리"
- content_category: "life"
- note: "재배 주기의 공간"
- order_no: 1
- relative_path: "../contents/farming-fences.md"
### `farming-onboarding-strategy.current-system`

- seed_key: "farming-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/farming-onboarding-strategy.md"
### `farming-seeds-harvest-breeding.cycle`

- seed_key: "farming-seeds-harvest-breeding.cycle"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "farming-seeds-harvest-breeding"
- content_name_ko: "재배 씨앗·수확·품종개량"
- content_category: "life"
- note: "재배 주기의 심기·수확"
- order_no: 1
- relative_path: "../contents/farming-seeds-harvest-breeding.md"
### `worker-current-system.farming`

- seed_key: "worker-current-system.farming"
- direction: "incoming"
- relation_type: "related"
- content_slug: "worker-current-system"
- content_name_ko: "일꾼 현재 시스템"
- content_category: "life"
- note: "텃밭 관리에도 일꾼을 사용할 수 있다."
- order_no: 3
- relative_path: "../contents/worker-current-system.md"

## Evidence and Sources

### Current evidence

### `farming-current-cycle.summary::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-current-cycle.summary::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-current-cycle"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-06-04 재배 재정의"
- active: true
- is_active: true

### `farming-current-cycle.requirement.bird-damage::grind-profit-update-2026-06-10`

- evidence_seed_key: "farming-current-cycle.requirement.bird-damage::grind-profit-update-2026-06-10"
- source_id: "grind-profit-update-2026-06-10"
- title: "6월 10일(수) 업데이트 안내 (최종 수정 : 2026-06-11 19:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15720"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-06-10"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-current-cycle.bird-damage"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "새 공격 1회당 작물 건강 감소 약 0.25%"
- active: true
- is_active: true

### `farming-current-cycle.requirement.delays::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-current-cycle.requirement.delays::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-current-cycle.delays"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "성장 지연 요소"
- active: true
- is_active: true

### `farming-current-cycle.requirement.fertilizers::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-current-cycle.requirement.fertilizers::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-current-cycle.fertilizers"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "비료 3종 삭제"
- active: true
- is_active: true

### `farming-current-cycle.requirement.growth-time::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-current-cycle.requirement.growth-time::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-current-cycle.growth-time"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "20/21/22시간"
- active: true
- is_active: true

### `farming-current-cycle.requirement.moisture::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-current-cycle.requirement.moisture::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-current-cycle.moisture"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수분 감소율 1/5"
- active: true
- is_active: true

### Historical / inactive evidence

- None
