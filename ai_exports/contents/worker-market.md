<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일꾼 거래소

## Identity

- slug: "worker-market"
- name_ko: "일꾼 거래소"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "작업 감독관을 통해 대기 중인 일꾼을 등록·고용하며 판매 정산 수수료는 30%다."
- purpose: "일꾼 거래소의 등록·구매·가격·수수료 범위를 기록한다."

## Requirements

### `worker-market.functions`

- seed_key: "worker-market.functions"
- kind: "other"
- requirement_level: "required"
- title: "거래소 기능"
- description: "대기 중인 자신의 일꾼 등록과 다른 모험가 일꾼 고용이 가능하다."
- structured_value:

```json
{
  "hire_other_adventurer_worker": true,
  "npc": "worker_supervisor",
  "register_own_worker": true,
  "remote_town_registration_supported": true,
  "seller_worker_must_be_idle": true
}
```

### `worker-market.price-fee`

- seed_key: "worker-market.price-fee"
- kind: "other"
- requirement_level: "required"
- title: "가격과 수수료"
- description: "가격 영향 요소와 판매 정산 수수료를 구분한다."
- structured_value:

```json
{
  "price_factors": [
    "grade",
    "level",
    "skills"
  ],
  "sale_fee_percent": 30
}
```

### `worker-market.unresolved-promotion`

- seed_key: "worker-market.unresolved-promotion"
- kind: "other"
- requirement_level: "optional"
- title: "구매 일꾼의 승급 기회"
- description: "장인 미만 구매 일꾼의 남은 승급 기회는 최신 공식 근거가 부족하다."
- structured_value:

```json
{
  "remaining_promotion_chances": null,
  "verification": "needs_review"
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

- None

## Evidence and Sources

### Current evidence

### `worker-market.claim.current::worker-convenience-2025-01-22`

- evidence_seed_key: "worker-market.claim.current::worker-convenience-2025-01-22"
- source_id: "worker-convenience-2025-01-22"
- title: "1월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13457"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-22"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-market"
- claim_key: "requirements:worker-market"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `worker-market.claim.current::worker-guide`

- evidence_seed_key: "worker-market.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-market"
- claim_key: "requirements:worker-market"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `worker-market.claim.promotion-unresolved::worker-guide`

- evidence_seed_key: "worker-market.claim.promotion-unresolved::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-market"
- claim_key: "requirement:worker-market.unresolved-promotion"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
