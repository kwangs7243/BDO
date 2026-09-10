<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아이템 획득 확률 증가 시스템

## Identity

- slug: "item-drop-rate-system"
- name_ko: "아이템 획득 확률 증가 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "아이템 획득 확률 증가와 아이템 획득 수량 증가는 서로 다른 효과다."
- purpose: "드롭 확률·수량·적용 제외 콘텐츠를 하나의 수치로 혼동하지 않는다."

## Requirements

### `item-drop-rate-system.distinction`

- seed_key: "item-drop-rate-system.distinction"
- kind: "stat"
- requirement_level: "required"
- title: "확률과 수량 구분"
- description: "아이템 획득 확률 증가와 아이템 획득 수량 증가는 별도 효과이며 콘텐츠별 적용 여부가 다를 수 있다."
- structured_value:

```json
{
  "applicability_varies_by_content": true,
  "drop_probability_separate_from_quantity": true,
  "knowledge_role": "fact"
}
```

### `item-drop-rate-system.formula`

- seed_key: "item-drop-rate-system.formula"
- kind: "stat"
- requirement_level: "required"
- title: "확률 증가 계산"
- description: "기본 획득 확률에 합산된 아이템 획득 확률 증가 배율을 적용한다."
- structured_value:

```json
{
  "formula": "base_probability * (1 + total_drop_rate_bonus_percent / 100)",
  "guaranteed_drop_overflow_not_implied": true,
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

### `agris-fever.drop-system`

- seed_key: "agris-fever.drop-system"
- direction: "incoming"
- relation_type: "related"
- content_slug: "agris-fever"
- content_name_ko: "아그리스의 열기"
- content_category: "combat_pve"
- note: "아이템 획득 확률이 아니라 지정 잡동사니 수량 증가다."
- order_no: 1
- relative_path: "../contents/agris-fever.md"
### `ecology-family-drop-bonus.system`

- seed_key: "ecology-family-drop-bonus.system"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "ecology-family-drop-bonus"
- content_name_ko: "생태 지식·가문 명성 획득 확률 보너스"
- content_category: "combat_pve"
- note: "아이템 획득 확률 증가의 상시 보너스 출처다."
- order_no: 1
- relative_path: "../contents/ecology-family-drop-bonus.md"
### `item-drop-rate-cap.system`

- seed_key: "item-drop-rate-cap.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "item-drop-rate-cap"
- content_name_ko: "아이템 획득 확률 증가 상한"
- content_category: "combat_pve"
- note: "아이템 획득 확률 증가의 상한 규칙이다."
- order_no: 1
- relative_path: "../contents/item-drop-rate-cap.md"
### `loot-scroll-system.drop-system`

- seed_key: "loot-scroll-system.drop-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "loot-scroll-system"
- content_name_ko: "아이템 획득 증가 주문서"
- content_category: "combat_pve"
- note: "획득 확률과 수량을 구분하는 대표 소비 효과다."
- order_no: 1
- relative_path: "../contents/loot-scroll-system.md"
### `grind-setup-strategy-foundation.loot`

- seed_key: "grind-setup-strategy-foundation.loot"
- direction: "incoming"
- relation_type: "related"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: "아이템 획득 확률과 수량 효과를 연결한다."
- order_no: 5
- relative_path: "../contents/grind-setup-strategy-foundation.md"

## Evidence and Sources

### Current evidence

### `item-drop-rate-system.claim.distinction::item-drop-applicability-guide`

- evidence_seed_key: "item-drop-rate-system.claim.distinction::item-drop-applicability-guide"
- source_id: "item-drop-applicability-guide"
- title: "아이템 획득 증가 효과 적용 범위"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=301"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "item-drop-rate-system.distinction"
- claim_key: "requirement:item-drop-rate-system.distinction"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `item-drop-rate-system.claim.distinction::item-drop-rate-guide`

- evidence_seed_key: "item-drop-rate-system.claim.distinction::item-drop-rate-guide"
- source_id: "item-drop-rate-guide"
- title: "아이템 획득 확률 증가"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=345"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "item-drop-rate-system.distinction"
- claim_key: "requirement:item-drop-rate-system.distinction"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `item-drop-rate-system.claim.formula::item-drop-rate-guide`

- evidence_seed_key: "item-drop-rate-system.claim.formula::item-drop-rate-guide"
- source_id: "item-drop-rate-guide"
- title: "아이템 획득 확률 증가"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=345"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "item-drop-rate-system.formula"
- claim_key: "requirement:item-drop-rate-system.formula"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
