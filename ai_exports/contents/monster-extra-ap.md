<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 몬스터 추가 공격력

## Identity

- slug: "monster-extra-ap"
- name_ko: "몬스터 추가 공격력"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "몬스터에게만 적용되는 추가 공격력과 표기 공격력 구간 보너스를 구분한다."
- purpose: "PvE 최종 공격력 계산에 몬스터 추가 공격력을 별도 항목으로 반영한다."

## Requirements

### `monster-extra-ap.scope`

- seed_key: "monster-extra-ap.scope"
- kind: "stat"
- requirement_level: "required"
- title: "적용 대상"
- description: "몬스터 추가 공격력은 몬스터 대상 전투에 적용되는 별도 능력치다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "same_as_sheet_ap": false,
  "target": "monster"
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

### `monster-extra-ap.ap-table`

- seed_key: "monster-extra-ap.ap-table"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sheet-ap-bonus-table"
- content_name_ko: "표기 공격력 구간 보너스"
- content_category: "combat_pve"
- note: "표기 공격력 구간에 따른 몬스터 추가 공격력 표를 참조한다."
- order_no: 1
- relative_path: "../contents/sheet-ap-bonus-table.md"

## Evidence and Sources

### Current evidence

### `monster-extra-ap.claim.scope::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "monster-extra-ap.claim.scope::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "monster-extra-ap.scope"
- claim_key: "requirement:monster-extra-ap.scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `monster-extra-ap.claim.scope::combat-stat-bonus-guide`

- evidence_seed_key: "monster-extra-ap.claim.scope::combat-stat-bonus-guide"
- source_id: "combat-stat-bonus-guide"
- title: "공격력 및 방어력 구간 보너스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=416"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "monster-extra-ap.scope"
- claim_key: "requirement:monster-extra-ap.scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
