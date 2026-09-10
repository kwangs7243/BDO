<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일꾼 성장·승급·기술 변경

## Identity

- slug: "worker-growth-promotion"
- name_ko: "일꾼 성장·승급·기술 변경"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "일꾼은 최대 40레벨, 40레벨 기술 10개이며 승급 확률은 90%·70%·50%로 고정된다."
- purpose: "레벨 성장, 기술 변경과 승급을 분리한다."

## Requirements

### `worker-growth-promotion.level-skills`

- seed_key: "worker-growth-promotion.level-skills"
- kind: "level"
- requirement_level: "required"
- title: "레벨과 기술 수"
- description: "1레벨부터 기술을 보유하고 매 5레벨마다 새 기술을 배운다."
- structured_value:

```json
{
  "has_skill_from_level": 1,
  "max_level": 40,
  "new_skill_every_levels": 5,
  "total_skills_at_level_40": 10
}
```

### `worker-growth-promotion.skill-reroll`

- seed_key: "worker-growth-promotion.skill-reroll"
- kind: "other"
- requirement_level: "required"
- title: "기술 변경"
- description: "30레벨 이상이며 경험치 20%를 소모해 보유 기술 하나를 변경한다."
- structured_value:

```json
{
  "exp_cost_percent": 20,
  "minimum_exp_percent": 20,
  "minimum_level": 30,
  "repeatable_after_regaining_exp": true
}
```

### `worker-growth-promotion.promotion`

- seed_key: "worker-growth-promotion.promotion"
- kind: "other"
- requirement_level: "required"
- title: "승급 확률"
- description: "레벨 10~40에서 등급별 고정 확률을 적용한다."
- structured_value:

```json
{
  "eligible_levels": [
    10,
    40
  ],
  "multiple_workers_can_test_concurrently": true,
  "on_success": {
    "learned_skills_reset": true,
    "level_reset": true
  },
  "rows": [
    {
      "from": "일반",
      "success_percent": 90,
      "to": "숙련"
    },
    {
      "from": "숙련",
      "success_percent": 70,
      "to": "전문"
    },
    {
      "from": "전문",
      "success_percent": 50,
      "to": "장인"
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

- None

## Evidence and Sources

### Current evidence

### `worker-growth-promotion.claim.current::worker-guide`

- evidence_seed_key: "worker-growth-promotion.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-growth-promotion"
- claim_key: "requirements:worker-growth-promotion"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `worker-growth-promotion.claim.current::worker-overhaul-2023-05-24`

- evidence_seed_key: "worker-growth-promotion.claim.current::worker-overhaul-2023-05-24"
- source_id: "worker-overhaul-2023-05-24"
- title: "5월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=10369"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-05-24"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-growth-promotion"
- claim_key: "requirements:worker-growth-promotion"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
