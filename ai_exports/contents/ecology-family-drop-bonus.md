<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생태 지식·가문 명성 획득 확률 보너스

## Identity

- slug: "ecology-family-drop-bonus"
- name_ko: "생태 지식·가문 명성 획득 확률 보너스"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "생태 지식 점수와 가문 명성으로 얻는 아이템 획득 확률 증가 보너스를 구조화한다."
- purpose: "점수별 생태 보너스와 가문 명성 보너스를 별도 규칙으로 계산한다."

## Requirements

### `ecology-family-drop-bonus.ecology`

- seed_key: "ecology-family-drop-bonus.ecology"
- kind: "knowledge"
- requirement_level: "required"
- title: "생태 지식 점수 보너스"
- description: "생태 지식 점수 경계에 따라 아이템 획득 확률 증가 보너스가 적용된다."
- structured_value:

```json
{
  "breakpoints": {
    "1000": 7,
    "10000": 30,
    "1500": 10,
    "2000": 12,
    "3000": 14,
    "4000": 16,
    "500": 5,
    "5000": 18,
    "6000": 20,
    "7000": 23,
    "8000": 25,
    "9000": 27
  },
  "knowledge_role": "fact",
  "unit": "percent"
}
```

### `ecology-family-drop-bonus.family-fame`

- seed_key: "ecology-family-drop-bonus.family-fame"
- kind: "stat"
- requirement_level: "required"
- title: "가문 명성 보너스"
- description: "가문 명성 7,000 이상이면 아이템 획득 확률 증가 10%가 적용된다."
- structured_value:

```json
{
  "drop_rate_bonus_percent": 10,
  "family_fame_threshold": 7000,
  "knowledge_role": "fact"
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

### `ecology-family-drop-bonus.system`

- seed_key: "ecology-family-drop-bonus.system"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "item-drop-rate-system"
- content_name_ko: "아이템 획득 확률 증가 시스템"
- content_category: "combat_pve"
- note: "아이템 획득 확률 증가의 상시 보너스 출처다."
- order_no: 1
- relative_path: "../contents/item-drop-rate-system.md"
### `account-progression-foundation.ecology`

- seed_key: "account-progression-foundation.ecology"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/account-progression-foundation.md"

## Evidence and Sources

### Current evidence

### `ecology-family-drop-bonus.claim.ecology::item-drop-benefits-history`

- evidence_seed_key: "ecology-family-drop-bonus.claim.ecology::item-drop-benefits-history"
- source_id: "item-drop-benefits-history"
- title: "아이템 획득 확률 증가 효과 변경 이력"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8461"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "ecology-family-drop-bonus.ecology"
- claim_key: "requirement:ecology-family-drop-bonus.ecology"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `ecology-family-drop-bonus.claim.family-fame::item-drop-benefits-history`

- evidence_seed_key: "ecology-family-drop-bonus.claim.family-fame::item-drop-benefits-history"
- source_id: "item-drop-benefits-history"
- title: "아이템 획득 확률 증가 효과 변경 이력"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8461"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "ecology-family-drop-bonus.family-fame"
- claim_key: "requirement:ecology-family-drop-bonus.family-fame"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
