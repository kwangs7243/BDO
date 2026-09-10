<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아그리스의 열기

## Identity

- slug: "agris-fever"
- name_ko: "아그리스의 열기"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "가문 공유 포인트를 소비해 특정 잡동사니 아이템 획득 수량을 늘리는 시스템이다."
- purpose: "기본·강화 최대치와 일일 회복, 적용 대상을 정확히 구분한다."

## Requirements

### `agris-fever.unlock`

- seed_key: "agris-fever.unlock"
- kind: "level"
- requirement_level: "required"
- title: "해금과 공유 범위"
- description: "56레벨부터 이용하며 포인트는 가문 단위로 공유한다."
- structured_value:

```json
{
  "family_shared": true,
  "knowledge_role": "fact",
  "minimum_level": 56
}
```

### `agris-fever.base`

- seed_key: "agris-fever.base"
- kind: "other"
- requirement_level: "required"
- title: "기본 포인트"
- description: "기본 최대 포인트는 50,000, 일일 회복은 15,000이며 매일 06:00에 회복한다."
- structured_value:

```json
{
  "daily_recovery": 15000,
  "knowledge_role": "fact",
  "max_points": 50000,
  "recovery_time": "06:00",
  "timezone": "Asia/Seoul"
}
```

### `agris-fever.enhanced`

- seed_key: "agris-fever.enhanced"
- kind: "other"
- requirement_level: "optional"
- title: "강화 완료 효과"
- description: "관련 모험일지 완료 후 최대 100,000, 일일 회복 20,000, 잡동사니 수량 증가 150%가 된다."
- structured_value:

```json
{
  "daily_recovery": 20000,
  "knowledge_role": "fact",
  "max_points": 100000,
  "trash_loot_quantity_bonus_percent": 150
}
```

### `agris-fever.scope`

- seed_key: "agris-fever.scope"
- kind: "item"
- requirement_level: "required"
- title: "적용 범위"
- description: "아그리스의 열기는 지정된 잡동사니 획득 수량에 적용되며 희귀 아이템 획득 확률을 올리지 않는다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "rare_drop_probability": false,
  "trash_loot_quantity": true
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

### `agris-fever.drop-system`

- seed_key: "agris-fever.drop-system"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "item-drop-rate-system"
- content_name_ko: "아이템 획득 확률 증가 시스템"
- content_category: "combat_pve"
- note: "아이템 획득 확률이 아니라 지정 잡동사니 수량 증가다."
- order_no: 1
- relative_path: "../contents/item-drop-rate-system.md"
### `book-of-margahan.agris`

- seed_key: "book-of-margahan.agris"
- direction: "incoming"
- relation_type: "related"
- content_slug: "book-of-margahan"
- content_name_ko: "마가한의 서"
- content_category: "progression"
- note: "마가한의 서는 아그리스의 열기를 해금하지 않고 기존 효과를 강화한다."
- order_no: 2
- relative_path: "../contents/book-of-margahan.md"
### `city-of-the-dead.agris`

- seed_key: "city-of-the-dead.agris"
- direction: "incoming"
- relation_type: "related"
- content_slug: "city-of-the-dead"
- content_name_ko: "죽은 자들의 도시"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/city-of-the-dead.md"
### `gabinya-coastal-cliff.agris`

- seed_key: "gabinya-coastal-cliff.agris"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gabinya-coastal-cliff"
- content_name_ko: "가비냐 해안 절벽"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/gabinya-coastal-cliff.md"
### `yzrahid-highlands.agris`

- seed_key: "yzrahid-highlands.agris"
- direction: "incoming"
- relation_type: "related"
- content_slug: "yzrahid-highlands"
- content_name_ko: "이스라히드 고원"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/yzrahid-highlands.md"
### `darkseekers-retreat.agris`

- seed_key: "darkseekers-retreat.agris"
- direction: "incoming"
- relation_type: "related"
- content_slug: "darkseekers-retreat"
- content_name_ko: "어둠 추종자 침소"
- content_category: "combat"
- note: null
- order_no: 3
- relative_path: "../contents/darkseekers-retreat.md"
### `hexe-sanctuary-elvia.agris`

- seed_key: "hexe-sanctuary-elvia.agris"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hexe-sanctuary-elvia"
- content_name_ko: "[엘비아] 헥세 성역"
- content_category: "combat"
- note: null
- order_no: 3
- relative_path: "../contents/hexe-sanctuary-elvia.md"
### `tungrad-ruins.agris`

- seed_key: "tungrad-ruins.agris"
- direction: "incoming"
- relation_type: "related"
- content_slug: "tungrad-ruins"
- content_name_ko: "툰그라드 유적지"
- content_category: "combat"
- note: null
- order_no: 3
- relative_path: "../contents/tungrad-ruins.md"

## Evidence and Sources

### Current evidence

### `agris-fever.claim.base::agris-fever-guide`

- evidence_seed_key: "agris-fever.claim.base::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "agris-fever.base"
- claim_key: "requirement:agris-fever.base"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `agris-fever.claim.enhanced::agris-fever-guide`

- evidence_seed_key: "agris-fever.claim.enhanced::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "agris-fever.enhanced"
- claim_key: "requirement:agris-fever.enhanced"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `agris-fever.claim.scope::agris-fever-guide`

- evidence_seed_key: "agris-fever.claim.scope::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "agris-fever.scope"
- claim_key: "requirement:agris-fever.scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `agris-fever.claim.scope::item-drop-rate-guide`

- evidence_seed_key: "agris-fever.claim.scope::item-drop-rate-guide"
- source_id: "item-drop-rate-guide"
- title: "아이템 획득 확률 증가"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=345"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "agris-fever.scope"
- claim_key: "requirement:agris-fever.scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `agris-fever.claim.unlock::agris-fever-guide`

- evidence_seed_key: "agris-fever.claim.unlock::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "agris-fever.unlock"
- claim_key: "requirement:agris-fever.unlock"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
