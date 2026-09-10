<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 저스틴 바탈리의 모험일지

## Identity

- slug: "justin-bartali-adventure-log"
- name_ko: "저스틴 바탈리의 모험일지"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- party_type: null
- difficulty: null

## Overview

- summary: "60레벨 이후 전용 연속 의뢰로 해금해 I~XVII의 17개 진행 단위를 완료하는 현재 모험일지 책장의 독립 일지다."
- purpose: "공식 해금 의뢰, 17개 진행 단위와 집계 보상을 가문 단위 진행 상태와 함께 추적한다."

## Requirements

### `justin-bartali-adventure-log.identity`

- seed_key: "justin-bartali-adventure-log.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "현재 공식 모험일지 책장에 독립 항목으로 표시되는 가문 단위 모험일지다."
- structured_value:

```json
{
  "bookshelf_group": "저스틴 바탈리의 모험일지",
  "family_content": true,
  "journal_kind": "progression_reward",
  "knowledge_role": "fact"
}
```

### `justin-bartali-adventure-log.unlock`

- seed_key: "justin-bartali-adventure-log.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "60레벨 달성 후 '[저스틴의 모험] 집 떠난 탕아'로 시작하는 연속 의뢰를 진행하고 '[모험일지] 저스틴 바탈리의 모험일지' 의뢰를 완료하면 I~XVII의 17개 진행 단위가 있는 일지를 해금한다."
- structured_value:

```json
{
  "completion_quest": "[모험일지] 저스틴 바탈리의 모험일지",
  "entry_count": 17,
  "entry_range": "I-XVII",
  "knowledge_role": "fact",
  "minimum_level": 60,
  "starting_quest": "[저스틴의 모험] 집 떠난 탕아"
}
```

## Steps

### `justin-bartali-adventure-log.step.unlock`

- seed_key: "justin-bartali-adventure-log.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "연속 의뢰 진행"
- description: "60레벨을 달성한 뒤 집 떠난 탕아로 시작하는 저스틴의 모험 연속 의뢰를 진행한다."
- checkable: true

### `justin-bartali-adventure-log.step.open-log`

- seed_key: "justin-bartali-adventure-log.step.open-log"
- phase: "first_time"
- order_no: 2
- title: "모험일지 해금"
- description: "마지막 모험일지 의뢰를 완료하고 책장에서 I~XVII의 독립 일지가 열렸는지 확인한다."
- checkable: true

## Schedules

- None

## Rewards

### `justin-bartali-adventure-log.reward.item-collection-scroll`

- seed_key: "justin-bartali-adventure-log.reward.item-collection-scroll"
- name: "아이템 획득 증가 주문서"
- reward_type: "fixed_item"
- amount: 12.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "I, V, IX, XIII에서 각 3개"
- order_no: 1

### `justin-bartali-adventure-log.reward.florin-secret-book`

- seed_key: "justin-bartali-adventure-log.reward.florin-secret-book"
- name: "플로린 비법서"
- reward_type: "fixed_item"
- amount: 9.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "III, VII, XI에서 각 3개"
- order_no: 2

### `justin-bartali-adventure-log.reward.intermediate-titles`

- seed_key: "justin-bartali-adventure-log.reward.intermediate-titles"
- name: "중간 완료 칭호"
- reward_type: "fixed_effect"
- amount: 7.0
- min_amount: null
- max_amount: null
- unit: "종"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "고소공포증, 숨은 그림 찾기, 투견, 역마살, 이몸등장, 덜덜 떠는, 바람에 펄럭이는"
- order_no: 3

### `justin-bartali-adventure-log.reward.sealed-combat-book`

- seed_key: "justin-bartali-adventure-log.reward.sealed-combat-book"
- name: "봉인된 전투의 서"
- reward_type: "fixed_item"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "지속 기간 7일"
- order_no: 4

### `justin-bartali-adventure-log.reward.sealed-life-book`

- seed_key: "justin-bartali-adventure-log.reward.sealed-life-book"
- name: "봉인된 생활의 서"
- reward_type: "fixed_item"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "지속 기간 7일"
- order_no: 5

### `justin-bartali-adventure-log.reward.cron-stone`

- seed_key: "justin-bartali-adventure-log.reward.cron-stone"
- name: "크론석"
- reward_type: "fixed_item"
- amount: 300.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 6

### `justin-bartali-adventure-log.reward.final-title`

- seed_key: "justin-bartali-adventure-log.reward.final-title"
- name: "칭호: 집 나간 자식"
- reward_type: "fixed_effect"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "종"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "I~XVII 최종 완료 보상"
- order_no: 7

### `justin-bartali-adventure-log.reward.warranty`

- seed_key: "justin-bartali-adventure-log.reward.warranty"
- name: "저스틴 바탈리의 보증서"
- reward_type: "fixed_item"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "I~XVII 최종 완료 보상"
- order_no: 8

## Sections

### `justin-bartali-adventure-log.section.reward-boundary`

- seed_key: "justin-bartali-adventure-log.section.reward-boundary"
- section_type: "notes"
- title: "공식 집계 보상"
- order_no: 1

#### body_markdown

공식 패치가 제시한 I~XVII의 장별 보상을 항목별 총량으로 집계했다. 장별 공략·위치·동선은 이 closure 범위에 포함하지 않는다.

## Related Contents

### `justin-bartali-adventure-log.foundation`

- seed_key: "justin-bartali-adventure-log.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventure-log-foundation.md"

## Evidence and Sources

### Current evidence

### `justin-bartali-adventure-log.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "justin-bartali-adventure-log.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "justin-bartali-adventure-log"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.purpose::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.purpose::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "justin-bartali-adventure-log"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "justin-bartali-adventure-log.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "justin-bartali-adventure-log"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.summary::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.summary::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "justin-bartali-adventure-log"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "justin-bartali-adventure-log.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "justin-bartali-adventure-log.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.identity::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.identity::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "justin-bartali-adventure-log.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "justin-bartali-adventure-log.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "justin-bartali-adventure-log.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.unlock::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.unlock::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "justin-bartali-adventure-log.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.section.reward-boundary::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.section.reward-boundary::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "justin-bartali-adventure-log.section.reward-boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.step.open-log::adventure-log-bookshelf-guide`

- evidence_seed_key: "justin-bartali-adventure-log.claim.step.open-log::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "justin-bartali-adventure-log.step.open-log"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.step.open-log::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.step.open-log::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "justin-bartali-adventure-log.step.open-log"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "justin-bartali-adventure-log.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "justin-bartali-adventure-log.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.step.unlock::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.step.unlock::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "justin-bartali-adventure-log.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.reward.cron-stone::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.reward.cron-stone::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "justin-bartali-adventure-log.reward.cron-stone"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.reward.final-title::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.reward.final-title::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "justin-bartali-adventure-log.reward.final-title"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.reward.florin-secret-book::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.reward.florin-secret-book::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "justin-bartali-adventure-log.reward.florin-secret-book"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.reward.intermediate-titles::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.reward.intermediate-titles::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "justin-bartali-adventure-log.reward.intermediate-titles"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.reward.item-collection-scroll::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.reward.item-collection-scroll::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "justin-bartali-adventure-log.reward.item-collection-scroll"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.reward.sealed-combat-book::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.reward.sealed-combat-book::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "justin-bartali-adventure-log.reward.sealed-combat-book"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.reward.sealed-life-book::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.reward.sealed-life-book::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "justin-bartali-adventure-log.reward.sealed-life-book"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### `justin-bartali-adventure-log.claim.reward.warranty::justin-bartali-log-update-2025-11-19`

- evidence_seed_key: "justin-bartali-adventure-log.claim.reward.warranty::justin-bartali-log-update-2025-11-19"
- source_id: "justin-bartali-log-update-2025-11-19"
- title: "11월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14803"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-11-19"
- retrieved_at: "2026-09-09T01:04:30+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "justin-bartali-adventure-log.reward.warranty"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
