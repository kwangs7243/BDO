<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 수렵 입문 전략

## Identity

- slug: "hunting-onboarding-strategy"
- name_ko: "수렵 입문 전략"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- party_type: null
- difficulty: null

## Overview

- summary: "일반 개인 수렵에서 조작과 채집 흐름을 익힌 뒤 저격 또는 협동 수렵으로 확장하는 조건부 입문 전략이다."
- purpose: "수렵 장비와 대상의 사실 목록을 반복하지 않고 처음 시작할 모드와 단계 전환 기준을 안내한다."

## Requirements

### `hunting-onboarding-strategy.mode-choice`

- seed_key: "hunting-onboarding-strategy.mode-choice"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "수렵 모드 선택"
- description: "일반 개인 수렵, 저격 수렵, 협동 수렵은 조작과 준비가 다르므로 현재 경험과 플레이 목적에 맞춰 구분한다."
- structured_value:

```json
{
  "knowledge_role": "strategy",
  "modes": [
    "individual_matchlock",
    "sniper",
    "cooperative"
  ],
  "single_default_mode": false
}
```

### `hunting-onboarding-strategy.target-context`

- seed_key: "hunting-onboarding-strategy.target-context"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "대상 선택 조건"
- description: "입문 대상은 이동 거리, 공격과 회피 조작, 장비 상태, 도축 동선과 학습 목적을 함께 보고 선택하며 사자 수렵은 익숙해진 뒤 검토할 상위 단계 사례로 둔다."
- structured_value:

```json
{
  "decision_dimensions": [
    "travel_distance",
    "combat_controls",
    "gear_state",
    "butchering_route",
    "learning_goal"
  ],
  "knowledge_role": "strategy",
  "lion_is_advanced_example": true,
  "universal_best_target": false
}
```

## Steps

### `hunting-onboarding-strategy.step.prepare-equipment`

- seed_key: "hunting-onboarding-strategy.step.prepare-equipment"
- phase: "preparation"
- order_no: 1
- title: "수렵 장비 준비"
- description: "사용할 화승총 계열 장비와 처치 후 도축에 필요한 도구를 준비한다."
- checkable: false

### `hunting-onboarding-strategy.step.learn-controls`

- seed_key: "hunting-onboarding-strategy.step.learn-controls"
- phase: "first_time"
- order_no: 2
- title: "기본 조작 익히기"
- description: "장전, 사격, 이동과 회피 흐름을 가까운 개인 수렵 대상에서 익힌다."
- checkable: false

### `hunting-onboarding-strategy.step.choose-target`

- seed_key: "hunting-onboarding-strategy.step.choose-target"
- phase: "first_time"
- order_no: 3
- title: "입문 대상 선택"
- description: "현재 장비와 조작 숙련으로 반복하기 편한 개인 수렵 대상 하나를 선택한다."
- checkable: false

### `hunting-onboarding-strategy.step.butcher`

- seed_key: "hunting-onboarding-strategy.step.butcher"
- phase: "first_time"
- order_no: 4
- title: "처치 후 도축"
- description: "처치 뒤 도축까지 완료해 수렵 경험치와 채집 흐름을 함께 확인한다."
- checkable: false

### `hunting-onboarding-strategy.step.review-progress`

- seed_key: "hunting-onboarding-strategy.step.review-progress"
- phase: "maintenance"
- order_no: 5
- title: "진행 상태 점검"
- description: "장비, 숙련도와 조작 안정성을 확인해 같은 대상을 반복할지 판단한다."
- checkable: false

### `hunting-onboarding-strategy.step.expand-mode`

- seed_key: "hunting-onboarding-strategy.step.expand-mode"
- phase: "maintenance"
- order_no: 6
- title: "다음 모드로 확장"
- description: "개인 수렵 흐름이 익숙해진 뒤 목적에 따라 저격, 협동 또는 상위 대상을 검토한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `hunting-onboarding-strategy.section.mode`

- seed_key: "hunting-onboarding-strategy.section.mode"
- section_type: "strategy"
- title: "일반·저격·협동 수렵 구분"
- order_no: 1

#### body_markdown

처음에는 개인 수렵에서 화승총 조작과 도축 흐름을 함께 익힌다. 거리와 조준 중심의 플레이를 원하면 저격 수렵을, 인원과 출현 조건을 맞출 수 있으면 협동 수렵을 별도 선택지로 본다.

### `hunting-onboarding-strategy.section.progression`

- seed_key: "hunting-onboarding-strategy.section.progression"
- section_type: "strategy"
- title: "상위 대상 전환 기준"
- order_no: 2

#### body_markdown

이동과 회피, 장전 흐름이 안정되고 현재 장비로 반복이 편해진 뒤 상위 대상을 검토한다. 사자 수렵은 커뮤니티에서 다루는 상위 단계 사례이며 모든 입문자에게 같은 순서로 적용하지 않는다.

### `hunting-onboarding-strategy.section.mistakes`

- seed_key: "hunting-onboarding-strategy.section.mistakes"
- section_type: "common_mistakes"
- title: "처음 피할 실수"
- order_no: 3

#### body_markdown

처치만 하고 도축 도구를 준비하지 않거나, 일반 수렵과 저격 조작을 같은 방식으로 보거나, 과거 가이드의 장비·수정·버프 구성을 현재 고정 세팅으로 사용하지 않는다.

## Related Contents

### `hunting-onboarding-strategy.current-system`

- seed_key: "hunting-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "hunting-current-system"
- content_name_ko: "수렵 현재 시스템"
- content_category: "life"
- note: "처치와 도축 등 현재 사실 규칙은 현재 시스템에서 확인한다."
- order_no: 1
- relative_path: "../contents/hunting-current-system.md"
### `hunting-onboarding-strategy.firearms`

- seed_key: "hunting-onboarding-strategy.firearms"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "hunting-firearms"
- content_name_ko: "수렵 장비와 화승총 강화"
- content_category: "life"
- note: "일반·저격 장비 구분과 현재 장비 규칙을 확인한다."
- order_no: 2
- relative_path: "../contents/hunting-firearms.md"
### `hunting-onboarding-strategy.sniper`

- seed_key: "hunting-onboarding-strategy.sniper"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sniper-hunting"
- content_name_ko: "저격 수렵"
- content_category: "life"
- note: "저격 수렵의 별도 조작과 대상을 확인한다."
- order_no: 3
- relative_path: "../contents/sniper-hunting.md"
### `hunting-onboarding-strategy.mastery`

- seed_key: "hunting-onboarding-strategy.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "숙련도 성장과 장비 판단의 공통 기반을 확인한다."
- order_no: 4
- relative_path: "../contents/life-mastery-foundation.md"

## Evidence and Sources

### Current evidence

### `hunting-onboarding-strategy.claim.purpose::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.purpose::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "현재 시스템과 전략 책임을 분리한 목적"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.purpose::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.purpose::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "현재 시스템과 전략 책임을 분리한 목적"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.summary::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.summary::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 수렵 모드와 조건부 커뮤니티 상위 대상 사례를 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.summary::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.summary::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 수렵 모드와 조건부 커뮤니티 상위 대상 사례를 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.summary::hunting-shadow-lion-strategy-2026-06-21`

- evidence_seed_key: "hunting-onboarding-strategy.claim.summary::hunting-shadow-lion-strategy-2026-06-21"
- source_id: "hunting-shadow-lion-strategy-2026-06-21"
- title: "Shadow Lion Hunting Guide 2026 Edition!"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1ubwz7j/shadow_lion_hunting_guide_2026_edition/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-06-21"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content"
- entity_id: "hunting-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 수렵 모드와 조건부 커뮤니티 상위 대상 사례를 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.mode-choice::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.mode-choice::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hunting-onboarding-strategy.mode-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "모드 선택을 조건부 STRATEGY로 분리"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.mode-choice::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.mode-choice::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hunting-onboarding-strategy.mode-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "모드 선택을 조건부 STRATEGY로 분리"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.target-context::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.target-context::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hunting-onboarding-strategy.target-context"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "사자 수렵을 보편 선택이 아닌 상위 사례로 제한"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.target-context::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.target-context::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hunting-onboarding-strategy.target-context"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "사자 수렵을 보편 선택이 아닌 상위 사례로 제한"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.target-context::hunting-shadow-lion-strategy-2026-06-21`

- evidence_seed_key: "hunting-onboarding-strategy.claim.target-context::hunting-shadow-lion-strategy-2026-06-21"
- source_id: "hunting-shadow-lion-strategy-2026-06-21"
- title: "Shadow Lion Hunting Guide 2026 Edition!"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1ubwz7j/shadow_lion_hunting_guide_2026_edition/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-06-21"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hunting-onboarding-strategy.target-context"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "사자 수렵을 보편 선택이 아닌 상위 사례로 제한"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.section-mistakes::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.section-mistakes::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "hunting-onboarding-strategy.section.mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "과거 exact 세팅을 current FACT로 사용하지 않음"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.section-mistakes::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.section-mistakes::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "hunting-onboarding-strategy.section.mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "과거 exact 세팅을 current FACT로 사용하지 않음"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.section-mode::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.section-mode::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "hunting-onboarding-strategy.section.mode"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.section-mode::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.section-mode::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "hunting-onboarding-strategy.section.mode"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.section-progression::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.section-progression::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "hunting-onboarding-strategy.section.progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "사자 계열은 advanced example이며 universal best가 아님"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.section-progression::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.section-progression::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "hunting-onboarding-strategy.section.progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "사자 계열은 advanced example이며 universal best가 아님"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.section-progression::hunting-shadow-lion-strategy-2026-06-21`

- evidence_seed_key: "hunting-onboarding-strategy.claim.section-progression::hunting-shadow-lion-strategy-2026-06-21"
- source_id: "hunting-shadow-lion-strategy-2026-06-21"
- title: "Shadow Lion Hunting Guide 2026 Edition!"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1ubwz7j/shadow_lion_hunting_guide_2026_edition/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-06-21"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_section"
- entity_id: "hunting-onboarding-strategy.section.progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "사자 계열은 advanced example이며 universal best가 아님"
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-butcher::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-butcher::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.butcher"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-choose-target::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-choose-target::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.choose-target"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-choose-target::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-choose-target::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.choose-target"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-expand-mode::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-expand-mode::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.expand-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-expand-mode::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-expand-mode::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.expand-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-expand-mode::hunting-shadow-lion-strategy-2026-06-21`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-expand-mode::hunting-shadow-lion-strategy-2026-06-21"
- source_id: "hunting-shadow-lion-strategy-2026-06-21"
- title: "Shadow Lion Hunting Guide 2026 Edition!"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1ubwz7j/shadow_lion_hunting_guide_2026_edition/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-06-21"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.expand-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-learn-controls::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-learn-controls::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.learn-controls"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-learn-controls::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-learn-controls::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.learn-controls"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-prepare-equipment::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-prepare-equipment::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.prepare-equipment"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-review-progress::hunting-guide`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-review-progress::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.review-progress"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `hunting-onboarding-strategy.claim.step-review-progress::hunting-lion-strategy-2024-10-15`

- evidence_seed_key: "hunting-onboarding-strategy.claim.step-review-progress::hunting-lion-strategy-2024-10-15"
- source_id: "hunting-lion-strategy-2024-10-15"
- title: "사자 수렵의 모든것 _검은사막"
- url: "https://blackdesertonlineyoutube.tistory.com/167"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-10-15"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "hunting-onboarding-strategy.step.review-progress"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
