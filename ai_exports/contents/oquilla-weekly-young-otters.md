<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [주간] 어린 해달 상인들을 위해

## Identity

- slug: "oquilla-weekly-young-otters"
- name_ko: "[주간] 어린 해달 상인들을 위해"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "산호조각 50개와 오색빛 산호조각 5개를 전달해 심해초 줄기 45개와 홍조빛 해저단괴 15개를 받는 주간 의뢰."
- purpose: "점진 파란 장비 제작의 심해초·홍조 재료를 대량 확보한다."

## Requirements

### `oquilla-weekly-young-otters.requirement.start-npc`

- seed_key: "oquilla-weekly-young-otters.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "오킬루아의 눈 무역관리 카리오"
- structured_value: null

## Steps

### `oquilla-weekly-young-otters.step.complete-objective`

- seed_key: "oquilla-weekly-young-otters.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "산호조각 50개와 오색빛 산호조각 5개 전달"
- checkable: false

## Schedules

### `oquilla-weekly-young-otters.schedule.quest-reset`

- seed_key: "oquilla-weekly-young-otters.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 의뢰: 매주 목요일 00:00 KST 초기화"

## Rewards

### `oquilla-weekly-young-otters.reward.seaweed`

- seed_key: "oquilla-weekly-young-otters.reward.seaweed"
- name: "심해초 줄기"
- reward_type: "quest_reward"
- amount: 45.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `oquilla-weekly-young-otters.reward.oquilla-coin`

- seed_key: "oquilla-weekly-young-otters.reward.oquilla-coin"
- name: "오킬루아 기념 주화"
- reward_type: "quest_reward"
- amount: 15.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 2

### `oquilla-weekly-young-otters.reward.red-lump`

- seed_key: "oquilla-weekly-young-otters.reward.red-lump"
- name: "홍조빛 해저단괴"
- reward_type: "quest_reward"
- amount: 15.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 3

## Sections

### `oquilla-weekly-young-otters.section.removed-old-daily`

- seed_key: "oquilla-weekly-young-otters.section.removed-old-daily"
- section_type: "notes"
- title: "예전 일일 의뢰와 혼동 금지"
- order_no: 1

#### body_markdown

2025-02-05에 기존 `[일일] 어린 해달 상인들을 위해` 등 3종은 제거되고, 현재는 선착장 인근에서 주간 의뢰 형태로 제공된다.

## Related Contents

### `oquilla-weekly-young-otters.relation.carrack-advance`

- seed_key: "oquilla-weekly-young-otters.relation.carrack-advance"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/carrack-advance.md"

## Evidence and Sources

### Current evidence

### `oquilla-weekly-young-otters.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-young-otters"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 파란 장비 제작의 심해초·홍조 재료를 대량 확보한다."
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-young-otters"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "산호조각 50개와 오색빛 산호조각 5개를 전달해 심해초 줄기 45개와 홍조빛 해저단괴 15개를 받는 주간 의뢰."
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-weekly-young-otters.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-weekly-young-otters.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "oquilla-weekly-young-otters.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 오킬루아의 눈 무역관리 카리오"
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.section.removed-old-daily::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.section.removed-old-daily::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "oquilla-weekly-young-otters.section.removed-old-daily"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "예전 일일 의뢰와 혼동 금지"
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "oquilla-weekly-young-otters.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "산호조각 50개와 오색빛 산호조각 5개 전달"
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.reward.oquilla-coin::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.reward.oquilla-coin::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-young-otters.reward.oquilla-coin"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 오킬루아 기념 주화"
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.reward.red-lump::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.reward.red-lump::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-young-otters.reward.red-lump"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 홍조빛 해저단괴"
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.reward.seaweed::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.reward.seaweed::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-young-otters.reward.seaweed"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 심해초 줄기"
- active: true
- is_active: true

### `oquilla-weekly-young-otters.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "oquilla-weekly-young-otters.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "oquilla-weekly-young-otters.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰: 매주 목요일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
