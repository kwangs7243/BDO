<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 모험일지 기반

## Identity

- slug: "adventure-log-foundation"
- name_ko: "모험일지 기반"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "2026-09-08 공식 책장 기준 10개 그룹을 구분하고, 상시·현재 일지와 이벤트 일지 및 이야기 재감상 도감을 분리해 탐색하는 기반이다."
- purpose: "일지·도감의 identity, 그룹별 해금과 가문 보상 의미를 journal 단위로 추적한다."

## Requirements

### `adventure-log-foundation.current-structure`

- seed_key: "adventure-log-foundation.current-structure"
- kind: "quest"
- requirement_level: "required"
- title: "모험일지 책장 구조"
- description: "현재 공식 책장 표에는 10개 그룹이 있으며, 이 중 이벤트 모험일지 1개와 상시·현재 그룹 9개를 구분한다."
- structured_value:

```json
{
  "event_group_count": 1,
  "groups": [
    "이고르 바탈리의 모험일지",
    "까마귀 상단의 기록일지",
    "그믐달 상단의 행동일지",
    "샤카투 상단의 수집일지",
    "이벤트 모험일지",
    "우두머리 도감 : 아침의 나라",
    "아침의 나라 이야기 도감 : 동해도/황해도 편",
    "어느 모험가의 낯선 풍경",
    "저스틴 바탈리의 모험일지",
    "올비아 아카데미 성장일지"
  ],
  "knowledge_role": "fact",
  "listed_group_count": 10,
  "non_event_group_count": 9
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

### `adventure-log-foundation.account`

- seed_key: "adventure-log-foundation.account"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `adventure-log-foundation.rewards`

- seed_key: "adventure-log-foundation.rewards"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "permanent-family-reward-foundation"
- content_name_ko: "영구 가문 보상 기반"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/permanent-family-reward-foundation.md"
### `adventurer-strange-scenery.foundation`

- seed_key: "adventurer-strange-scenery.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "adventurer-strange-scenery"
- content_name_ko: "어느 모험가의 낯선 풍경"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventurer-strange-scenery.md"
### `alustin-alchemy-journal.foundation`

- seed_key: "alustin-alchemy-journal.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "alustin-alchemy-journal"
- content_name_ko: "알루스틴의 연금일지"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/alustin-alchemy-journal.md"
### `book-of-margahan.foundation`

- seed_key: "book-of-margahan.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "book-of-margahan"
- content_name_ko: "마가한의 서"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/book-of-margahan.md"
### `caphras-record.foundation`

- seed_key: "caphras-record.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "caphras-record"
- content_name_ko: "카프라스의 기록"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/caphras-record.md"
### `deve-encyclopedia.foundation`

- seed_key: "deve-encyclopedia.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "deve-encyclopedia"
- content_name_ko: "데베의 만물사전"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/deve-encyclopedia.md"
### `dorin-morgrim-secret-journal.foundation`

- seed_key: "dorin-morgrim-secret-journal.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "dorin-morgrim-secret-journal"
- content_name_ko: "도린 모르그림의 비밀일지"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/dorin-morgrim-secret-journal.md"
### `emma-bartali-record-log.foundation`

- seed_key: "emma-bartali-record-log.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "emma-bartali-record-log"
- content_name_ko: "엠마 바탈리의 기록일지"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/emma-bartali-record-log.md"
### `fughar-success-era.foundation`

- seed_key: "fughar-success-era.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "fughar-success-era"
- content_name_ko: "푸가르의 성공시대"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/fughar-success-era.md"
### `herald-journal.foundation`

- seed_key: "herald-journal.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "herald-journal"
- content_name_ko: "외침꾼의 일지"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/herald-journal.md"
### `igor-bartali-adventure-log.foundation`

- seed_key: "igor-bartali-adventure-log.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "igor-bartali-adventure-log"
- content_name_ko: "이고르 바탈리의 모험일지"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/igor-bartali-adventure-log.md"
### `justin-bartali-adventure-log.foundation`

- seed_key: "justin-bartali-adventure-log.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "justin-bartali-adventure-log"
- content_name_ko: "저스틴 바탈리의 모험일지"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/justin-bartali-adventure-log.md"
### `lamute-gang-adventure-log.foundation`

- seed_key: "lamute-gang-adventure-log.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "lamute-gang-adventure-log"
- content_name_ko: "라뮤트 유랑단의 모험일지"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/lamute-gang-adventure-log.md"
### `morning-land-boss-codex.foundation`

- seed_key: "morning-land-boss-codex.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "morning-land-boss-codex"
- content_name_ko: "우두머리 도감 : 아침의 나라"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/morning-land-boss-codex.md"
### `morning-land-story-codex.foundation`

- seed_key: "morning-land-story-codex.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "morning-land-story-codex"
- content_name_ko: "아침의 나라 이야기 도감 : 동해도/황해도 편"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/morning-land-story-codex.md"
### `pavino-greko-miscellany.foundation`

- seed_key: "pavino-greko-miscellany.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "pavino-greko-miscellany"
- content_name_ko: "파비노 그레코의 잡학도서"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/pavino-greko-miscellany.md"
### `rulupee-travel-log.foundation`

- seed_key: "rulupee-travel-log.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "rulupee-travel-log"
- content_name_ko: "룰루피의 여행일지"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/rulupee-travel-log.md"

## Evidence and Sources

### Current evidence

### `adventure-log-foundation.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventure-log-foundation.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "adventure-log-foundation"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventure-log-foundation.claim.purpose::combat-system-rework-2025-07-23`

- evidence_seed_key: "adventure-log-foundation.claim.purpose::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "adventure-log-foundation"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventure-log-foundation.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventure-log-foundation.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "adventure-log-foundation"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventure-log-foundation.claim.current-structure::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventure-log-foundation.claim.current-structure::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "adventure-log-foundation.current-structure"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `adventure-log-foundation.claim.legacy-stat-distribution::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventure-log-foundation.claim.legacy-stat-distribution::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "adventure-log-foundation.legacy-stat-distribution"
- claim_key: "description"
- verification_status: "superseded"
- last_verified_at: "2026-09-08"
- evidence_note: "2025-07-23 이후 핵심 능력치 보상은 이고르 바탈리 모험일지로 통합됨"
- active: false
- is_active: false

### `adventure-log-foundation.claim.legacy-stat-distribution::combat-system-rework-2025-07-23`

- evidence_seed_key: "adventure-log-foundation.claim.legacy-stat-distribution::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "adventure-log-foundation.legacy-stat-distribution"
- claim_key: "description"
- verification_status: "superseded"
- last_verified_at: "2026-09-08"
- evidence_note: "2025-07-23 이후 핵심 능력치 보상은 이고르 바탈리 모험일지로 통합됨"
- active: false
- is_active: false

### `adventure-log-foundation.claim.legacy-stat-distribution::pit-weekly-2025`

- evidence_seed_key: "adventure-log-foundation.claim.legacy-stat-distribution::pit-weekly-2025"
- source_id: "pit-weekly-2025"
- title: "7월 23일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "adventure-log-foundation.legacy-stat-distribution"
- claim_key: "description"
- verification_status: "superseded"
- last_verified_at: "2026-09-08"
- evidence_note: "2025-07-23 이후 핵심 능력치 보상은 이고르 바탈리 모험일지로 통합됨"
- active: false
- is_active: false
