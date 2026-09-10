<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 채집 입문 전략

## Identity

- slug: "gathering-onboarding-strategy"
- name_ko: "채집 입문 전략"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- party_type: null
- difficulty: null

## Overview

- summary: "필요한 재료와 성장 목적을 먼저 정하고 도구·동선·현재 장비를 맞춰 첫 채집 루프를 구성하는 조건부 입문 전략이다."
- purpose: "채집 사실 규칙은 기존 현재 시스템에 맡기고, 처음 시작할 때의 선택과 점검 순서를 안내한다."

## Requirements

### `gathering-onboarding-strategy.purpose-choice`

- seed_key: "gathering-onboarding-strategy.purpose-choice"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "채집 목적 선택"
- description: "요리·연금·제작·프로젝트 재료 또는 생활 경험치와 숙련도 성장 중 이번 채집의 목적을 먼저 정한다."
- structured_value:

```json
{
  "decision_dimensions": [
    "target_material",
    "crafting_or_project_need",
    "life_progression"
  ],
  "knowledge_role": "strategy",
  "single_default_goal": false
}
```

### `gathering-onboarding-strategy.route-context`

- seed_key: "gathering-onboarding-strategy.route-context"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "동선 선택 조건"
- description: "목표 재료의 개체 밀도뿐 아니라 이동 거리, 재생 흐름, 창고 접근성, 무게와 캐릭터 이동 편의를 함께 비교한다."
- structured_value:

```json
{
  "decision_dimensions": [
    "target_density",
    "travel_distance",
    "respawn_loop",
    "storage_access",
    "weight",
    "character_mobility"
  ],
  "knowledge_role": "strategy",
  "universal_best_route": false
}
```

## Steps

### `gathering-onboarding-strategy.step.choose-goal`

- seed_key: "gathering-onboarding-strategy.step.choose-goal"
- phase: "preparation"
- order_no: 1
- title: "목표 정하기"
- description: "이번 세션에서 직접 필요한 재료나 생활 성장 목적 하나를 정한다."
- checkable: false

### `gathering-onboarding-strategy.step.confirm-method`

- seed_key: "gathering-onboarding-strategy.step.confirm-method"
- phase: "preparation"
- order_no: 2
- title: "채집 방식 확인"
- description: "목표 재료를 얻는 채집 대상과 상호작용 방식을 기존 현재 시스템에서 확인한다."
- checkable: false

### `gathering-onboarding-strategy.step.prepare-tool`

- seed_key: "gathering-onboarding-strategy.step.prepare-tool"
- phase: "preparation"
- order_no: 3
- title: "도구 준비"
- description: "선택한 채집 방식에 맞는 도구와 남은 내구도를 확인한다."
- checkable: false

### `gathering-onboarding-strategy.step.review-gear`

- seed_key: "gathering-onboarding-strategy.step.review-gear"
- phase: "preparation"
- order_no: 4
- title: "장비와 기운 확인"
- description: "현재 생활 장비, 숙련도와 사용할 수 있는 기운을 확인해 세션 범위를 정한다."
- checkable: false

### `gathering-onboarding-strategy.step.choose-route`

- seed_key: "gathering-onboarding-strategy.step.choose-route"
- phase: "first_time"
- order_no: 5
- title: "첫 동선 선택"
- description: "목표 재료와 이동·창고·무게 조건에 맞는 짧은 동선 하나를 선택한다."
- checkable: false

### `gathering-onboarding-strategy.step.run-loop`

- seed_key: "gathering-onboarding-strategy.step.run-loop"
- phase: "first_time"
- order_no: 6
- title: "한 바퀴 실행"
- description: "선택한 동선을 한 바퀴 진행하며 개체 간 이동과 재생 흐름을 확인한다."
- checkable: false

### `gathering-onboarding-strategy.step.adjust`

- seed_key: "gathering-onboarding-strategy.step.adjust"
- phase: "maintenance"
- order_no: 7
- title: "병목 조정"
- description: "기운, 무게, 도구 내구도 또는 이동이 먼저 막히는지 확인하고 다음 세션의 동선을 조정한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `gathering-onboarding-strategy.section.purpose`

- seed_key: "gathering-onboarding-strategy.section.purpose"
- section_type: "strategy"
- title: "목적 기반 선택"
- order_no: 1

#### body_markdown

필요한 재료가 정해져 있다면 그 재료를 얻는 채집 방식부터 선택한다. 생활 성장 자체가 목적이라면 현재 장비와 기운으로 반복하기 편한 방식을 비교한다.

### `gathering-onboarding-strategy.section.route`

- seed_key: "gathering-onboarding-strategy.section.route"
- section_type: "strategy"
- title: "채집 동선 비교 기준"
- order_no: 2

#### body_markdown

커뮤니티 동선은 유효한 후보지만 계정 상태에 따라 결과가 달라진다. 목표 재료, 개체 밀도, 이동 거리, 재생 흐름, 창고 접근성, 무게와 캐릭터 이동 편의를 함께 확인한다.

### `gathering-onboarding-strategy.section.mistakes`

- seed_key: "gathering-onboarding-strategy.section.mistakes"
- section_type: "common_mistakes"
- title: "처음 피할 실수"
- order_no: 3

#### body_markdown

목적 없이 인기 동선만 따라가거나, 채집 대상에 맞는 도구를 확인하지 않거나, 기운·무게·내구도 병목을 무시하지 않는다. 과거 수익표는 현재 선택의 고정 기준으로 사용하지 않는다.

## Related Contents

### `gathering-onboarding-strategy.current-system`

- seed_key: "gathering-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "채집 방식과 기운 등 사실 규칙은 현재 시스템에서 확인한다."
- order_no: 1
- relative_path: "../contents/gathering-current-system.md"
### `gathering-onboarding-strategy.tools`

- seed_key: "gathering-onboarding-strategy.tools"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "gathering-tools"
- content_name_ko: "채집 도구"
- content_category: "life"
- note: "채집 대상에 맞는 도구를 준비한다."
- order_no: 2
- relative_path: "../contents/gathering-tools.md"
### `gathering-onboarding-strategy.mastery`

- seed_key: "gathering-onboarding-strategy.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "현재 숙련도와 장비 상태를 판단할 때 참고한다."
- order_no: 3
- relative_path: "../contents/life-mastery-foundation.md"
### `gathering-onboarding-strategy.energy`

- seed_key: "gathering-onboarding-strategy.energy"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "energy-foundation"
- content_name_ko: "기운 기반"
- content_category: "life"
- note: "세션 범위를 정할 때 기운 구조를 확인한다."
- order_no: 4
- relative_path: "../contents/energy-foundation.md"
### `alchemy-onboarding-strategy.gathering`

- seed_key: "alchemy-onboarding-strategy.gathering"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 6
- relative_path: "../contents/alchemy-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `gathering-onboarding-strategy.claim.purpose::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.purpose::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gathering-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "현재 시스템과 전략 책임을 분리한 목적"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.purpose::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.purpose::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gathering-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "현재 시스템과 전략 책임을 분리한 목적"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.summary::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.summary::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gathering-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 채집 규칙과 조건부 커뮤니티 동선 기준을 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.summary::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.summary::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gathering-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 채집 규칙과 조건부 커뮤니티 동선 기준을 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.purpose-choice::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.purpose-choice::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "목표에 따른 조건부 선택 전략"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.purpose-choice::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.purpose-choice::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "목표에 따른 조건부 선택 전략"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.route-context::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.route-context::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-onboarding-strategy.route-context"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "특정 동선을 보편화하지 않는 비교 기준"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.route-context::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.route-context::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-onboarding-strategy.route-context"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "특정 동선을 보편화하지 않는 비교 기준"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.section-mistakes::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.section-mistakes::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "gathering-onboarding-strategy.section.mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.section-mistakes::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.section-mistakes::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "gathering-onboarding-strategy.section.mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.section-purpose::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.section-purpose::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "gathering-onboarding-strategy.section.purpose"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 규칙 위에 목적별 선택을 구성한 STRATEGY"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.section-purpose::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.section-purpose::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "gathering-onboarding-strategy.section.purpose"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 규칙 위에 목적별 선택을 구성한 STRATEGY"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.section-route::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.section-route::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "gathering-onboarding-strategy.section.route"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "작성자 동선을 일반 사실이 아닌 비교 기준으로 제한"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.section-route::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.section-route::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "gathering-onboarding-strategy.section.route"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "작성자 동선을 일반 사실이 아닌 비교 기준으로 제한"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-adjust::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-adjust::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.adjust"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-adjust::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-adjust::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.adjust"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-choose-goal::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-choose-goal::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-choose-goal::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-choose-goal::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-choose-route::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-choose-route::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.choose-route"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "커뮤니티 동선을 조건부 후보로 사용"
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-confirm-method::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-confirm-method::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.confirm-method"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-prepare-tool::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-prepare-tool::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.prepare-tool"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-review-gear::gathering-guide`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-review-gear::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.review-gear"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `gathering-onboarding-strategy.claim.step-run-loop::gathering-location-strategy-2026-05-24`

- evidence_seed_key: "gathering-onboarding-strategy.claim.step-run-loop::gathering-location-strategy-2026-05-24"
- source_id: "gathering-location-strategy-2026-05-24"
- title: "노스토스의 별 추천 채집 장소 * 영상 및 글"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319"
- publisher: "만두집아들I검사학개론"
- source_type: "community_strategy"
- published_at: "2026-05-24"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "gathering-onboarding-strategy.step.run-loop"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
