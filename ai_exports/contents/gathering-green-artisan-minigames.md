<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 초록 장인 채집 미니게임

## Identity

- slug: "gathering-green-artisan-minigames"
- name_ko: "초록 장인 채집 미니게임"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "뿌리 깊은 손 지식을 얻어 활성화하면 채집 중 확률적으로 미니게임이 나타나며, 성공 시 기운 10으로 한 번 채집 결과의 10배를 얻는다."
- purpose: "초록 장인 해금, 활성화, 성공·실패와 특수 아이템 예외를 구조화한다."

## Requirements

### `gathering-green-artisan-minigames.unlock`

- seed_key: "gathering-green-artisan-minigames.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "해금"
- description: "채집 전문 1 이상에서 일반 의뢰를 진행하거나 올비아 아카데미 경로로 뿌리 깊은 손 지식을 얻는다."
- structured_value:

```json
{
  "knowledge": "뿌리 깊은 손",
  "normal_quest_minimum_level": "Professional 1",
  "paths": [
    "[뿌리 깊은 손] 바다 건너의 채집꾼",
    "Olvia Academy graduation/knowledge"
  ]
}
```

### `gathering-green-artisan-minigames.activation`

- seed_key: "gathering-green-artisan-minigames.activation"
- kind: "other"
- requirement_level: "required"
- title: "활성화"
- description: "내 정보(P)의 생활 정보 상세에서 채집 뿌리 깊은 손을 활성화한다."
- structured_value:

```json
{
  "appearance": "random",
  "ui_path": [
    "내 정보(P)",
    "생활 정보",
    "자세히 보기",
    "채집",
    "뿌리 깊은 손"
  ]
}
```

### `gathering-green-artisan-minigames.result`

- seed_key: "gathering-green-artisan-minigames.result"
- kind: "stat"
- requirement_level: "required"
- title: "성공과 실패"
- description: "성공과 실패의 기운 소비 및 결과가 다르다."
- structured_value:

```json
{
  "failure": {
    "energy": 1,
    "output": "normal_one_action"
  },
  "success": {
    "energy": 10,
    "output_multiplier": 10
  }
}
```

### `gathering-green-artisan-minigames.exclusions`

- seed_key: "gathering-green-artisan-minigames.exclusions"
- kind: "item"
- requirement_level: "required"
- title: "10배 제외"
- description: "발타라의 천안과 발타라의 추억은 성공 10배 효과를 받지 않는다."
- structured_value:

```json
{
  "not_multiplied": [
    "발타라의 천안",
    "발타라의 추억"
  ]
}
```

### `gathering-green-artisan-minigames.actions`

- seed_key: "gathering-green-artisan-minigames.actions"
- kind: "other"
- requirement_level: "required"
- title: "대상 행동"
- description: "공식 가이드가 안내하는 미니게임 대상 채집 행동이다."
- structured_value:

```json
{
  "actions": [
    "호미",
    "도축",
    "무두질",
    "채광",
    "벌목",
    "수액 채취"
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

### `gathering-green-artisan-minigames.interpretation`

- seed_key: "gathering-green-artisan-minigames.interpretation"
- section_type: "common_mistakes"
- title: "10배의 범위"
- order_no: 1

#### body_markdown

성공 보상은 해당 1회 채집 결과 기준이며 발타라 특수 아이템까지 무조건 10배가 되는 규칙이 아니다.

## Related Contents

### `gathering-green-artisan-minigames.system`

- seed_key: "gathering-green-artisan-minigames.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "채집 확률 미니게임"
- order_no: 1
- relative_path: "../contents/gathering-current-system.md"

## Evidence and Sources

### Current evidence

### `gathering-green-artisan-minigames.summary::gathering-guide`

- evidence_seed_key: "gathering-green-artisan-minigames.summary::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gathering-green-artisan-minigames"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "초록 장인 구조"
- active: true
- is_active: true

### `gathering-green-artisan-minigames.requirement.actions::gathering-guide`

- evidence_seed_key: "gathering-green-artisan-minigames.requirement.actions::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-green-artisan-minigames.actions"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "미니게임 대상 행동"
- active: true
- is_active: true

### `gathering-green-artisan-minigames.requirement.activation::gathering-guide`

- evidence_seed_key: "gathering-green-artisan-minigames.requirement.activation::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-green-artisan-minigames.activation"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "활성화 UI와 확률 등장"
- active: true
- is_active: true

### `gathering-green-artisan-minigames.requirement.exclusions::gathering-guide`

- evidence_seed_key: "gathering-green-artisan-minigames.requirement.exclusions::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-green-artisan-minigames.exclusions"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "발타라 아이템 제외"
- active: true
- is_active: true

### `gathering-green-artisan-minigames.requirement.result::gathering-guide`

- evidence_seed_key: "gathering-green-artisan-minigames.requirement.result::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-green-artisan-minigames.result"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "성공·실패 기운과 결과"
- active: true
- is_active: true

### `gathering-green-artisan-minigames.requirement.unlock::gathering-guide`

- evidence_seed_key: "gathering-green-artisan-minigames.requirement.unlock::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-green-artisan-minigames.unlock"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "해금 경로와 전문 1 조건"
- active: true
- is_active: true

### Historical / inactive evidence

- None
