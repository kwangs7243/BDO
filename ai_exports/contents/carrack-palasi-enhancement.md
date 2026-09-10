<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 팔라시 장비 강화

## Identity

- slug: "carrack-palasi-enhancement"
- name_ko: "팔라시 장비 강화"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "노을진 파도의 블랙스톤 제작식과 팔라시 장비 +1~+10 강화 기준."
- purpose: "강화 재료, 실패 규칙, 확률·스택·아그리스·크론석 수치를 구조화한다."

## Requirements

### `carrack-palasi-enhancement.sunset-wave-stone`

- seed_key: "carrack-palasi-enhancement.sunset-wave-stone"
- kind: "item"
- requirement_level: "required"
- title: "노을진 파도의 블랙스톤 제작"
- description: "가열하기로 노을빛 산호의 정수 1개와 파도의 블랙스톤 100개를 노을진 파도의 블랙스톤 1개로 만든다."
- structured_value:

```json
{
  "inputs": {
    "노을빛 산호의 정수": 1,
    "파도의 블랙스톤": 100
  },
  "output": {
    "노을진 파도의 블랙스톤": 1
  },
  "process": "가열하기"
}
```

### `carrack-palasi-enhancement.table`

- seed_key: "carrack-palasi-enhancement.table"
- kind: "gear"
- requirement_level: "required"
- title: "+1~+10 강화 기준"
- description: "각 강화 단계의 기본 확률, 기준 스택, 기준 스택 적용 확률, 아그리스의 정수와 크론석 수치."
- structured_value:

```json
[
  {
    "agris_essence": 8,
    "base_rate_percent": 3,
    "cron_stones": 0,
    "level": 1,
    "rate_at_reference_stack_percent": 24,
    "reference_stack": 70
  },
  {
    "agris_essence": 9,
    "base_rate_percent": 2,
    "cron_stones": 290,
    "level": 2,
    "rate_at_reference_stack_percent": 22,
    "reference_stack": 100
  },
  {
    "agris_essence": 9,
    "base_rate_percent": 1.5,
    "cron_stones": 360,
    "level": 3,
    "rate_at_reference_stack_percent": 20.25,
    "reference_stack": 125
  },
  {
    "agris_essence": 11,
    "base_rate_percent": 1.25,
    "cron_stones": 380,
    "level": 4,
    "rate_at_reference_stack_percent": 17.5,
    "reference_stack": 130
  },
  {
    "agris_essence": 12,
    "base_rate_percent": 1,
    "cron_stones": 400,
    "level": 5,
    "rate_at_reference_stack_percent": 15.5,
    "reference_stack": 145
  },
  {
    "agris_essence": 14,
    "base_rate_percent": 0.85,
    "cron_stones": 420,
    "level": 6,
    "rate_at_reference_stack_percent": 13.6,
    "reference_stack": 150
  },
  {
    "agris_essence": 17,
    "base_rate_percent": 0.7,
    "cron_stones": 440,
    "level": 7,
    "rate_at_reference_stack_percent": 11.55,
    "reference_stack": 155
  },
  {
    "agris_essence": 20,
    "base_rate_percent": 0.55,
    "cron_stones": 460,
    "level": 8,
    "rate_at_reference_stack_percent": 9.63,
    "reference_stack": 165
  },
  {
    "agris_essence": 25,
    "base_rate_percent": 0.4,
    "cron_stones": 480,
    "level": 9,
    "rate_at_reference_stack_percent": 7.8,
    "reference_stack": 185
  },
  {
    "agris_essence": 30,
    "base_rate_percent": 0.25,
    "cron_stones": 540,
    "level": 10,
    "rate_at_reference_stack_percent": 6.25,
    "reference_stack": 240
  }
]
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `carrack-palasi-enhancement.rules`

- seed_key: "carrack-palasi-enhancement.rules"
- section_type: "common_mistakes"
- title: "노란색 선박 장비 강화 규칙"
- order_no: 1

#### body_markdown

강화 시 노을진 파도의 블랙스톤 1개를 사용한다. 실패하면 단계가 하락하고 내구도가 감소한다. 크론석을 사용할 수 있으며 강화 실패 시 단계 하락을 막는다.

## Related Contents

### `carrack-palasi-enhancement.relation.palasi`

- seed_key: "carrack-palasi-enhancement.relation.palasi"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "carrack-palasi-gear"
- content_name_ko: "중범선 팔라시 장비"
- content_category: "ocean_project"
- note: "팔라시 장비의 강화 규칙"
- order_no: 1
- relative_path: "../contents/carrack-palasi-gear.md"
### `carrack-palasi-enhancement.relation.rinbach`

- seed_key: "carrack-palasi-enhancement.relation.rinbach"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "노을빛 산호의 정수 획득처"
- order_no: 2
- relative_path: "../contents/rinbach-colony.md"
### `panokseon-cheongun.relation.palasi`

- seed_key: "panokseon-cheongun.relation.palasi"
- direction: "incoming"
- relation_type: "related"
- content_slug: "panokseon-cheongun"
- content_name_ko: "판옥선 청운 장비"
- content_category: "ocean_guide"
- note: "노란색 선박 장비 강화 규칙 공유"
- order_no: 2
- relative_path: "../contents/panokseon-cheongun.md"
### `rinbach-colony.relation.enhancement`

- seed_key: "rinbach-colony.relation.enhancement"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "노을진 파도의 블랙스톤 재료인 노을빛 산호의 정수"
- order_no: 2
- relative_path: "../contents/rinbach-colony.md"
### `carrack-palasi-gear.relation.enhancement`

- seed_key: "carrack-palasi-gear.relation.enhancement"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "carrack-palasi-gear"
- content_name_ko: "중범선 팔라시 장비"
- content_category: "ocean_project"
- note: "제작 후 노을진 파도의 블랙스톤으로 강화"
- order_no: 3
- relative_path: "../contents/carrack-palasi-gear.md"

## Evidence and Sources

### Current evidence

### `carrack-palasi-enhancement.evidence.sunset-wave-stone::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-enhancement.evidence.sunset-wave-stone::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-enhancement.sunset-wave-stone"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가열하기로 노을빛 산호의 정수 1개와 파도의 블랙스톤 100개를 노을진 파도의 블랙스톤 1개로 만든다."
- active: true
- is_active: true

### `carrack-palasi-enhancement.evidence.table::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-enhancement.evidence.table::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-enhancement.table"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "각 강화 단계의 기본 확률, 기준 스택, 기준 스택 적용 확률, 아그리스의 정수와 크론석 수치."
- active: true
- is_active: true

### `carrack-palasi-enhancement.evidence.rules::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-enhancement.evidence.rules::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-palasi-enhancement.rules"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "강화 시 노을진 파도의 블랙스톤 1개를 사용한다. 실패하면 단계가 하락하고 내구도가 감소한다. 크론석을 사용할 수 있으며 강화 실패 시 단계 하락을 막는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
