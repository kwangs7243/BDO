<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가문 통합 은화

## Identity

- slug: "family-silver-unification"
- name_ko: "가문 통합 은화"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "가문 내 캐릭터와 모든 마을 창고의 은화는 내 은화 하나로 통합되며 통합거래소 보관 은화는 별도다."
- purpose: "구식 캐릭터별·마을별 은화 잔액 모델을 현재 통합 pool과 구분한다."

## Requirements

### `family-silver-unification.current-pool`

- seed_key: "family-silver-unification.current-pool"
- kind: "other"
- requirement_level: "required"
- title: "내 은화"
- description: "캐릭터와 마을 창고가 동일한 가문 은화 pool을 사용한다."
- structured_value:

```json
{
  "character_specific_balances": false,
  "characters_share_pool": true,
  "family_unified": true,
  "town_specific_balances": false,
  "town_storages_share_pool": true
}
```

### `family-silver-unification.market-separate`

- seed_key: "family-silver-unification.market-separate"
- kind: "other"
- requirement_level: "required"
- title: "통합거래소 은화"
- description: "거래용 창고 보관 금액은 내 은화와 별도다."
- structured_value:

```json
{
  "central_market_storage_silver_separate": true
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

### `family-silver-unification.storage`

- seed_key: "family-silver-unification.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: "창고 아이템 슬롯과 통합 은화 pool은 별도 의미다."
- order_no: 1
- relative_path: "../contents/storage-current-system.md"
### `family-convenience-unlock-foundation.family-silver`

- seed_key: "family-convenience-unlock-foundation.family-silver"
- direction: "incoming"
- relation_type: "related"
- content_slug: "family-convenience-unlock-foundation"
- content_name_ko: "가문 편의 기능 해금"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/family-convenience-unlock-foundation.md"
### `storage-current-system.silver`

- seed_key: "storage-current-system.silver"
- direction: "incoming"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: "아이템 창고와 은화 통합 pool은 별도다."
- order_no: 3
- relative_path: "../contents/storage-current-system.md"

## Evidence and Sources

### Current evidence

### `family-silver-unification.claim.current::silver-unification-history`

- evidence_seed_key: "family-silver-unification.claim.current::silver-unification-history"
- source_id: "silver-unification-history"
- title: "캐릭터 및 창고 내 보유 은화 통합"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9726"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "family-silver-unification"
- claim_key: "requirements:family-silver-unification"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `family-silver-unification.claim.legacy-character-balance::silver-unification-history`

- evidence_seed_key: "family-silver-unification.claim.legacy-character-balance::silver-unification-history"
- source_id: "silver-unification-history"
- title: "캐릭터 및 창고 내 보유 은화 통합"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9726"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "family-silver-unification"
- claim_key: "legacy:character-specific-silver-balance"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `family-silver-unification.claim.legacy-character-balance::storage-guide`

- evidence_seed_key: "family-silver-unification.claim.legacy-character-balance::storage-guide"
- source_id: "storage-guide"
- title: "창고"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=39"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "family-silver-unification"
- claim_key: "legacy:character-specific-silver-balance"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `family-silver-unification.claim.legacy-town-balance::silver-unification-history`

- evidence_seed_key: "family-silver-unification.claim.legacy-town-balance::silver-unification-history"
- source_id: "silver-unification-history"
- title: "캐릭터 및 창고 내 보유 은화 통합"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9726"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "family-silver-unification"
- claim_key: "legacy:town-specific-silver-balance"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `family-silver-unification.claim.legacy-town-balance::storage-guide`

- evidence_seed_key: "family-silver-unification.claim.legacy-town-balance::storage-guide"
- source_id: "storage-guide"
- title: "창고"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=39"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "family-silver-unification"
- claim_key: "legacy:town-specific-silver-balance"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
