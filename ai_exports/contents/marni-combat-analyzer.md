<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 마르니의 전투 분석기

## Identity

- slug: "marni-combat-analyzer"
- name_ko: "마르니의 전투 분석기"
- category: "system"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "2026-08-05 추가된 공식 전투 측정 도구."
- purpose: "피해량·전투 시간·DPS를 동일 세션에서 기록"

## Requirements

### `marni-combat-analyzer.current-fields`

- seed_key: "marni-combat-analyzer.current-fields"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "현재 기록 항목"
- description: "가한 피해량, 전투 시간, DPS 및 분석기가 제공하는 항목을 기록한다."
- structured_value:

```json
{
  "fields": [
    "inflicted_damage",
    "combat_time",
    "dps",
    "other_analyzer_fields"
  ],
  "future_user_measurement_candidate": true,
  "knowledge_role": "fact",
  "launched_at": "2026-08-05"
}
```

### `marni-combat-analyzer.session-context`

- seed_key: "marni-combat-analyzer.session-context"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "측정 세션 연결 원칙"
- description: "향후 스크린샷 측정은 사냥터·캐릭터·버프·잡동사니와 한 세션으로 묶어야 한다."
- structured_value:

```json
{
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "recommended_context": [
    "dps",
    "combat_duration",
    "spot",
    "character",
    "buffs",
    "trash"
  ]
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

### `marni-combat-analyzer.measurement-foundation`

- seed_key: "marni-combat-analyzer.measurement-foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-setup-strategy-foundation.md"

## Evidence and Sources

### Current evidence

### `marni-combat-analyzer.claim.current-fields::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "marni-combat-analyzer.claim.current-fields::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "marni-combat-analyzer.current-fields"
- claim_key: "requirement:current-fields"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `marni-combat-analyzer.claim.session-context::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "marni-combat-analyzer.claim.session-context::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "marni-combat-analyzer.session-context"
- claim_key: "requirement:session-context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
