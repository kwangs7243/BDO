<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 엠마 바탈리의 기록일지

## Identity

- slug: "emma-bartali-record-log"
- name_ko: "엠마 바탈리의 기록일지"
- category: "progression"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "올비아 아카데미 성장일지 안에서 카라자드 액세서리 동(V)~풍(VIII) 성장을 지원하는 13장의 상시 기록일지다."
- purpose: "장별 공식 선행 조건과 확정 강화·하락 방지 지원 보상을 현재 상태로 추적한다."

## Requirements

### `emma-bartali-record-log.identity`

- seed_key: "emma-bartali-record-log.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "올비아 아카데미 성장일지 그룹 안에서 동(V)부터 풍(VIII)까지 카라자드 액세서리 성장을 지원하는 13장의 독립 기록일지다."
- structured_value:

```json
{
  "bookshelf_group": "올비아 아카데미 성장일지",
  "chapter_count": 13,
  "family_content": true,
  "journal_kind": "growth_support_log",
  "knowledge_role": "fact",
  "support_range": "동(V)-풍(VIII)"
}
```

### `emma-bartali-record-log.chapter-prerequisites`

- seed_key: "emma-bartali-record-log.chapter-prerequisites"
- kind: "quest"
- requirement_level: "required"
- title: "장별 선행 조건"
- description: "13개 장은 이고르 바탈리 5권, 까마귀의 둥지·불멸의 나락·툰그라드 대사원·파푸·아침의 나라·잠식의 결계·검은 사당 동해도/황해도 진행 조건을 각각 사용한다."
- structured_value:

```json
{
  "chapter_prerequisites": {
    "1": "이고르 바탈리의 모험일지 5권 완료",
    "10": "검은 사당 황해도(파티) 불가살 도전 난이도 토벌",
    "11": "검은 사당 황해도(파티) 우투리 도전 난이도 토벌",
    "12": "검은 사당 황해도(파티) 비형랑 도전 난이도 토벌",
    "13": "1~12장 완료 후 흑정령과 대화",
    "2": "[까마귀의 둥지] 까마귀의 용병 완료",
    "3": "[승급] 광 : 불멸의 까마귀 휘장 완료",
    "4": [
      "툰그라드 대사원 완료",
      "파푸에게 주는 선물 완료"
    ],
    "5": [
      "[아침의 나라] 도깨비의 선물 완료",
      "[아침의 나라] 태백을 호령하는 자 완료"
    ],
    "6": "[엘비아] 크자카 : 잠식의 결계 V 완료",
    "7": "검은 사당 동해도(개인) 산군 구재시니 토벌",
    "8": "검은 사당 동해도(개인) 구미호 구재시니 토벌",
    "9": "검은 사당 황해도(파티) 지귀 도전 난이도 토벌"
  },
  "knowledge_role": "fact"
}
```

## Steps

### `emma-bartali-record-log.step.unlock`

- seed_key: "emma-bartali-record-log.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "올비아 아카데미 성장일지에서 확인"
- description: "메뉴의 모험일지 책장에서 올비아 아카데미 성장일지 아래 엠마 바탈리의 기록일지를 확인한다."
- checkable: true

### `emma-bartali-record-log.step.progress`

- seed_key: "emma-bartali-record-log.step.progress"
- phase: "first_time"
- order_no: 2
- title: "장별 선행 콘텐츠 완료"
- description: "각 장에 연결된 의뢰·모험일지·검은 사당 토벌 조건을 충족해 1장부터 12장까지 진행한다."
- checkable: true

### `emma-bartali-record-log.step.complete`

- seed_key: "emma-bartali-record-log.step.complete"
- phase: "reward"
- order_no: 3
- title: "13장 완료"
- description: "1~12장을 모두 완료한 뒤 흑정령과 대화해 마지막 우(VII) 확정 강화 지원 보상을 받는다."
- checkable: true

## Schedules

- None

## Rewards

### `emma-bartali-record-log.reward.valks-180`

- seed_key: "emma-bartali-record-log.reward.valks-180"
- name: "발크스의 조언 (+180)"
- reward_type: "fixed_item"
- amount: 2.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `emma-bartali-record-log.reward.ancient-hammer-pen`

- seed_key: "emma-bartali-record-log.reward.ancient-hammer-pen"
- name: "고대의 망치 - 동(V)"
- reward_type: "fixed_item"
- amount: 10.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 2

### `emma-bartali-record-log.reward.ancient-black-stone-pen`

- seed_key: "emma-bartali-record-log.reward.ancient-black-stone-pen"
- name: "고대의 블랙스톤 - 동(V)"
- reward_type: "fixed_item"
- amount: 2.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 3

### `emma-bartali-record-log.reward.dawn-essence`

- seed_key: "emma-bartali-record-log.reward.dawn-essence"
- name: "새벽의 정수"
- reward_type: "fixed_item"
- amount: 100.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 4

### `emma-bartali-record-log.reward.valks-210`

- seed_key: "emma-bartali-record-log.reward.valks-210"
- name: "발크스의 조언 (+210)"
- reward_type: "fixed_item"
- amount: 2.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 5

### `emma-bartali-record-log.reward.ancient-hammer-hex`

- seed_key: "emma-bartali-record-log.reward.ancient-hammer-hex"
- name: "고대의 망치 - 운(VI)"
- reward_type: "fixed_item"
- amount: 10.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 6

### `emma-bartali-record-log.reward.ancient-black-stone-hex`

- seed_key: "emma-bartali-record-log.reward.ancient-black-stone-hex"
- name: "고대의 블랙스톤 - 운(VI)"
- reward_type: "fixed_item"
- amount: 2.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 7

### `emma-bartali-record-log.reward.ancient-black-stone-sep`

- seed_key: "emma-bartali-record-log.reward.ancient-black-stone-sep"
- name: "고대의 블랙스톤 - 우(VII)"
- reward_type: "fixed_item"
- amount: 2.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 8

## Sections

### `emma-bartali-record-log.section.known-issue`

- seed_key: "emma-bartali-record-log.section.known-issue"
- section_type: "common_mistakes"
- title: "현재 알려진 위치 표시 문제"
- order_no: 1

#### body_markdown

구미호 구재시니 처치 목표의 월드맵·미니맵 진행 위치가 아레하자 마을로 잘못 표시되는 현상이 공식 알려진 문제점에 남아 있다.

## Related Contents

### `emma-bartali-record-log.foundation`

- seed_key: "emma-bartali-record-log.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventure-log-foundation.md"
### `emma-bartali-record-log.igor`

- seed_key: "emma-bartali-record-log.igor"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "igor-bartali-adventure-log"
- content_name_ko: "이고르 바탈리의 모험일지"
- content_category: "progression"
- note: "1장 조건에 이고르 바탈리 5권 완료가 포함됨"
- order_no: 2
- relative_path: "../contents/igor-bartali-adventure-log.md"
### `emma-bartali-record-log.pit`

- seed_key: "emma-bartali-record-log.pit"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "pit-of-undying"
- content_name_ko: "불멸의 나락"
- content_category: "combat_pve"
- note: "3장 조건에 불멸의 까마귀 휘장 승급 의뢰가 포함됨"
- order_no: 3
- relative_path: "../contents/pit-of-undying.md"
### `emma-bartali-record-log.donghae`

- seed_key: "emma-bartali-record-log.donghae"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: "7~8장 동해도 개인 구재시니 토벌 조건"
- order_no: 4
- relative_path: "../contents/black-shrine-donghae-current-system.md"
### `emma-bartali-record-log.hwanghae`

- seed_key: "emma-bartali-record-log.hwanghae"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-hwanghae-current-system"
- content_name_ko: "검은사당 황해도 현재 시스템"
- content_category: "combat_pve"
- note: "9~12장 황해도 파티 도전 난이도 토벌 조건"
- order_no: 5
- relative_path: "../contents/black-shrine-hwanghae-current-system.md"

## Evidence and Sources

### Current evidence

### `emma-bartali-record-log.claim.purpose::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.purpose::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "emma-bartali-record-log"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.purpose::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.purpose::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "emma-bartali-record-log"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.summary::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.summary::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "emma-bartali-record-log"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.summary::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.summary::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "emma-bartali-record-log"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.chapter-prerequisites::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.chapter-prerequisites::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "emma-bartali-record-log.chapter-prerequisites"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "emma-bartali-record-log.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "emma-bartali-record-log.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.identity::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.identity::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "emma-bartali-record-log.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.section.known-issue::known-issues-current-2026-09-04`

- evidence_seed_key: "emma-bartali-record-log.claim.section.known-issue::known-issues-current-2026-09-04"
- source_id: "known-issues-current-2026-09-04"
- title: "알려진 문제점 (최종 수정 : 2026-09-03 17:37)"
- url: "https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=2989&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_known_issues"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "emma-bartali-record-log.section.known-issue"
- claim_key: "body"
- verification_status: "needs_review"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.step.complete::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.step.complete::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "emma-bartali-record-log.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.step.progress::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.step.progress::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "emma-bartali-record-log.step.progress"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.step.unlock::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.step.unlock::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "emma-bartali-record-log.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-black-stone-hex::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-black-stone-hex::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-black-stone-hex"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-black-stone-hex::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-black-stone-hex::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-black-stone-hex"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-black-stone-pen::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-black-stone-pen::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-black-stone-pen"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-black-stone-pen::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-black-stone-pen::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-black-stone-pen"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-black-stone-sep::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-black-stone-sep::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-black-stone-sep"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-black-stone-sep::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-black-stone-sep::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-black-stone-sep"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-hammer-hex::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-hammer-hex::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-hammer-hex"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-hammer-hex::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-hammer-hex::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-hammer-hex"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-hammer-pen::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-hammer-pen::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-hammer-pen"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.ancient-hammer-pen::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.ancient-hammer-pen::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.ancient-hammer-pen"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.dawn-essence::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.dawn-essence::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.dawn-essence"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.dawn-essence::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.dawn-essence::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.dawn-essence"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.valks-180::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.valks-180::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.valks-180"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.valks-180::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.valks-180::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.valks-180"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.valks-210::emma-bartali-log-update-2026-07-29`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.valks-210::emma-bartali-log-update-2026-07-29"
- source_id: "emma-bartali-log-update-2026-07-29"
- title: "7월 29일(수) 업데이트 안내(최종 수정 : 2026-07-31 10:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.valks-210"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `emma-bartali-record-log.claim.reward.valks-210::hyperboost-progression-2026`

- evidence_seed_key: "emma-bartali-record-log.claim.reward.valks-210::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "emma-bartali-record-log.reward.valks-210"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
