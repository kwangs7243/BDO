<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 2026 생산 거점 개편

## Identity

- slug: "production-node-2026-overhaul"
- name_ko: "2026 생산 거점 개편"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "2026년 6월 4일 개편 이후 거점 공헌도와 41개 생산 슬롯의 현재 산출물을 기록한다."
- purpose: "개편 전 수치가 현재값으로 노출되지 않도록 current 표와 이력을 함께 보존한다."

## Requirements

### `production-node-2026-overhaul.cp-changes`

- seed_key: "production-node-2026-overhaul.cp-changes"
- kind: "other"
- requirement_level: "required"
- title: "거점 공헌도 변경 13건"
- description: "개편 전후 공헌도 수치를 현재값과 함께 기록한다."
- structured_value:

```json
{
  "current_row_count": 13,
  "effective_date": "2026-06-04",
  "rows": [
    {
      "current_cp": 1,
      "node": "플로린 관문",
      "node_type": "exploration",
      "old_cp": 2
    },
    {
      "current_cp": 1,
      "node": "크로그달로의 자취",
      "node_type": "exploration",
      "old_cp": 2
    },
    {
      "current_cp": 1,
      "node": "폴리숲",
      "node_type": "exploration",
      "old_cp": 2
    },
    {
      "current_cp": 1,
      "node": "살라나르 못",
      "node_type": "exploration",
      "old_cp": 2
    },
    {
      "current_cp": 1,
      "node": "델리모르 농원",
      "node_type": "exploration",
      "old_cp": 2
    },
    {
      "current_cp": 1,
      "node": "티티움 계곡",
      "node_type": "exploration",
      "old_cp": 2
    },
    {
      "current_cp": 1,
      "node": "아크만",
      "node_type": "exploration",
      "old_cp": 2
    },
    {
      "current_cp": 1,
      "node": "바실리스크 소굴",
      "node_type": "exploration",
      "old_cp": 2
    },
    {
      "current_cp": 2,
      "node": "티티움 계곡 - 벌목",
      "node_type": "production",
      "old_cp": 3
    },
    {
      "current_cp": 2,
      "node": "아레하 야자숲 - 벌목1",
      "node_type": "production",
      "old_cp": 3
    },
    {
      "current_cp": 2,
      "node": "아레하 야자숲 - 벌목2",
      "node_type": "production",
      "old_cp": 3
    },
    {
      "current_cp": 1,
      "node": "라이칼 폭포 - 채집",
      "node_type": "production",
      "old_cp": 3
    },
    {
      "current_cp": 1,
      "node": "쿠니드의 쉼터 - 채집",
      "node_type": "production",
      "old_cp": 3
    }
  ]
}
```

### `production-node-2026-overhaul.production-slots`

- seed_key: "production-node-2026-overhaul.production-slots"
- kind: "other"
- requirement_level: "required"
- title: "현재 생산 슬롯 41개"
- description: "동일 거점·동일 산출물의 복수 슬롯을 별도 행으로 유지한다."
- structured_value:

```json
{
  "deduplicate_identical_outputs": false,
  "effective_date": "2026-06-04",
  "slot_count": 41,
  "slots": [
    {
      "cp": 1,
      "node": "늑대 언덕",
      "outputs": [
        "물푸레 나무 원목",
        "물푸레 나무 수액"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "늑대 언덕",
      "outputs": [
        "물푸레 나무 원목",
        "물푸레 나무 수액"
      ],
      "slot": "B"
    },
    {
      "cp": 1,
      "node": "테르미안 절벽",
      "outputs": [
        "구리 광석",
        "투명 수정 원석"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "노인의 다리",
      "outputs": [
        "자작 나무 원목",
        "자작 나무 수액"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "가면 올빼미의 숲",
      "outputs": [
        "철광석",
        "어둠의 가루"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "가면 올빼미의 숲",
      "outputs": [
        "철광석",
        "진흙 수정 원석"
      ],
      "slot": "B"
    },
    {
      "cp": 2,
      "node": "게르비슈 산맥",
      "outputs": [
        "측백나무 원목",
        "측백나무 널빤지",
        "측백나무 수액"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "게르비슈 산맥",
      "outputs": [
        "측백나무 원목",
        "측백나무 널빤지",
        "측백나무 수액"
      ],
      "slot": "B"
    },
    {
      "cp": 1,
      "node": "가모스의 둥지",
      "outputs": [
        "검은 수정 원석",
        "자연의 흔적"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "가모스의 둥지",
      "outputs": [
        "검은 수정 원석",
        "자연의 흔적"
      ],
      "slot": "B"
    },
    {
      "cp": 1,
      "node": "붉은늑대 부락",
      "outputs": [
        "삼나무 원목",
        "삼나무 수액"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "붉은늑대 부락",
      "outputs": [
        "삼나무 원목",
        "삼나무 수액"
      ],
      "slot": "B"
    },
    {
      "cp": 2,
      "node": "위니 산장",
      "outputs": [
        "화산갓 버섯",
        "녹색 대롱 버섯"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "위니 산장 - 발굴",
      "outputs": [
        "자연의 흔적",
        "베델로나"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "러니 산장",
      "outputs": [
        "흰갓버섯",
        "흰색꽃버섯"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "러니 산장 - 발굴",
      "outputs": [
        "자연의 흔적",
        "베델로나"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "미루목 유적지 - 발굴",
      "outputs": [
        "진흙 수정 원석",
        "자연의 흔적"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "발타라 산맥",
      "outputs": [
        "녹 광석",
        "세월의 가루"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "발타라 산맥",
      "outputs": [
        "녹 광석",
        "대지의 가루"
      ],
      "slot": "B"
    },
    {
      "cp": 1,
      "node": "낙시온",
      "outputs": [
        "닭고기",
        "달걀"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "낙시온",
      "outputs": [
        "닭고기",
        "달걀"
      ],
      "slot": "B"
    },
    {
      "cp": 2,
      "node": "라 오델",
      "outputs": [
        "가시나무 원목",
        "가시나무 수액"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "바히트 성소",
      "outputs": [
        "니켈 광석",
        "어둠의 가루"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "밤부 골짜기 - 채집",
      "outputs": [
        "프리카"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "밤부 골짜기 - 채광",
      "outputs": [
        "바나듐 광석",
        "균열의 가루",
        "푸른 수정 원석"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "순례자의 성소 - 순종",
      "outputs": [
        "금광석",
        "자연의 흔적"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "순례자의 성소 - 절제",
      "outputs": [
        "금광석",
        "자연의 흔적"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "순례자의 성소 - 분배",
      "outputs": [
        "금광석",
        "자연의 흔적"
      ],
      "slot": "A"
    },
    {
      "cp": 1,
      "node": "순례자의 성소 - 성실",
      "outputs": [
        "금광석",
        "자연의 흔적"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "필라 쿠 감옥",
      "outputs": [
        "철광석",
        "진은 광석"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "도나 바위산",
      "outputs": [
        "티타늄 광석",
        "화염의 가루",
        "보라 수정 원석"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "도나 바위산",
      "outputs": [
        "티타늄 광석",
        "화염의 가루",
        "보라 수정 원석"
      ],
      "slot": "B"
    },
    {
      "cp": 3,
      "node": "노병의 협곡",
      "outputs": [
        "딱총나무 원목",
        "딱총나무 널빤지",
        "딱총나무 수액"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "노병의 협곡",
      "outputs": [
        "아카시아 나무 원목",
        "아카시아 나무 수액",
        "핏빛나무 옹이"
      ],
      "slot": "B"
    },
    {
      "cp": 1,
      "node": "바심족 주둔지",
      "outputs": [
        "철광석",
        "어둠의 가루",
        "검은 수정 원석"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "바심족 주둔지",
      "outputs": [
        "티타늄 광석",
        "화염의 가루",
        "보라 수정 원석"
      ],
      "slot": "B"
    },
    {
      "cp": 2,
      "node": "필라 페",
      "outputs": [
        "푸른 수정 원석",
        "자연의 흔적"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "필라 페",
      "outputs": [
        "보라 수정 원석",
        "자연의 흔적"
      ],
      "slot": "B"
    },
    {
      "cp": 2,
      "node": "키슬리브 암석 지대",
      "outputs": [
        "바나듐 광석",
        "균열의 가루",
        "푸른 수정 원석"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "폐허도시 룬",
      "outputs": [
        "편백 나무 원목",
        "편백 나무 수액",
        "핏빛나무 옹이"
      ],
      "slot": "A"
    },
    {
      "cp": 2,
      "node": "폐허도시 룬",
      "outputs": [
        "편백 나무 원목",
        "편백 나무 수액",
        "핏빛나무 옹이"
      ],
      "slot": "B"
    }
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

### `production-node-2026-overhaul.current-system`

- seed_key: "production-node-2026-overhaul.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: "현재 생산 거점 시스템의 공헌도·산출물 표다."
- order_no: 1
- relative_path: "../contents/production-node-current-system.md"

## Evidence and Sources

### Current evidence

### `production-node-2026-overhaul.claim.current::farming-overhaul-2026-06-04`

- evidence_seed_key: "production-node-2026-overhaul.claim.current::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "production-node-2026-overhaul"
- claim_key: "requirements:production-node-2026-overhaul"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `production-node-2026-overhaul.claim.legacy-cp::farming-overhaul-2026-06-04`

- evidence_seed_key: "production-node-2026-overhaul.claim.legacy-cp::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "production-node-2026-overhaul"
- claim_key: "legacy:pre-2026-node-contribution-costs"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `production-node-2026-overhaul.claim.legacy-output::farming-overhaul-2026-06-04`

- evidence_seed_key: "production-node-2026-overhaul.claim.legacy-output::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "production-node-2026-overhaul"
- claim_key: "legacy:pre-2026-production-node-outputs"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
