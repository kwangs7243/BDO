<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 낚시 입문 전략

## Identity

- slug: "fishing-onboarding-strategy"
- name_ko: "낚시 입문 전략"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- party_type: null
- difficulty: null

## Overview

- summary: "자동·직접 조작·주간 대회 목적을 구분하고 가방, 낚싯대 내구도, 방생 설정과 처분 경로를 맞추는 조건부 입문 전략이다."
- purpose: "낚시 수치와 시스템 사실은 기존 콘텐츠에 맡기고 첫 세션의 모드 선택과 준비 순서를 안내한다."

## Requirements

### `fishing-onboarding-strategy.mode-choice`

- seed_key: "fishing-onboarding-strategy.mode-choice"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "낚시 목적과 모드 선택"
- description: "자리를 비우는 자동 낚시, 직접 조작하는 낚시, 별도 준비가 필요한 주간 낚시 대회를 서로 다른 목적으로 구분한다."
- structured_value:

```json
{
  "knowledge_role": "strategy",
  "modes": [
    "afk",
    "active",
    "weekly_contest"
  ],
  "single_default_mode": false,
  "weekly_rotating_target_static": false
}
```

### `fishing-onboarding-strategy.session-bottlenecks`

- seed_key: "fishing-onboarding-strategy.session-bottlenecks"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "세션 병목 확인"
- description: "세션 길이에 맞춰 가방 여유, 낚싯대 내구도, 자동 낚시 시간 감소, 방생 기준과 물고기 처분 경로를 함께 점검한다."
- structured_value:

```json
{
  "decision_dimensions": [
    "session_duration",
    "inventory_space",
    "rod_durability",
    "auto_fishing_time",
    "discard_setting",
    "disposal_route"
  ],
  "dynamic_profit_included": false,
  "knowledge_role": "strategy"
}
```

## Steps

### `fishing-onboarding-strategy.step.choose-mode`

- seed_key: "fishing-onboarding-strategy.step.choose-mode"
- phase: "preparation"
- order_no: 1
- title: "낚시 목적 선택"
- description: "자동, 직접 조작 또는 주간 대회 중 이번 세션의 목적을 먼저 정한다."
- checkable: false

### `fishing-onboarding-strategy.step.prepare-rod`

- seed_key: "fishing-onboarding-strategy.step.prepare-rod"
- phase: "preparation"
- order_no: 2
- title: "낚싯대 준비"
- description: "선택한 방식에 사용할 낚싯대와 남은 내구도를 확인한다."
- checkable: false

### `fishing-onboarding-strategy.step.check-potential`

- seed_key: "fishing-onboarding-strategy.step.check-potential"
- phase: "preparation"
- order_no: 3
- title: "낚시 잠재력 확인"
- description: "현재 낚시 잠재력과 적용 중인 장비·효과를 기존 현재 시스템에서 확인한다."
- checkable: false

### `fishing-onboarding-strategy.step.configure-discard`

- seed_key: "fishing-onboarding-strategy.step.configure-discard"
- phase: "preparation"
- order_no: 4
- title: "방생 기준 설정"
- description: "세션 길이와 가방 여유에 맞춰 자동 낚시 방생 기준을 확인한다."
- checkable: false

### `fishing-onboarding-strategy.step.reserve-inventory`

- seed_key: "fishing-onboarding-strategy.step.reserve-inventory"
- phase: "preparation"
- order_no: 5
- title: "가방 여유 확보"
- description: "예상 세션 동안 잡은 물고기를 담을 수 있도록 가방 공간을 비운다."
- checkable: false

### `fishing-onboarding-strategy.step.run-session`

- seed_key: "fishing-onboarding-strategy.step.run-session"
- phase: "first_time"
- order_no: 6
- title: "첫 세션 실행"
- description: "짧은 세션을 실행해 가방과 내구도 중 어느 쪽이 먼저 제한되는지 확인한다."
- checkable: false

### `fishing-onboarding-strategy.step.choose-disposal`

- seed_key: "fishing-onboarding-strategy.step.choose-disposal"
- phase: "first_time"
- order_no: 7
- title: "처분 경로 확인"
- description: "잡은 물고기의 신선도와 목적에 맞춰 황실 납품, 무역 또는 가공 경로를 확인한다."
- checkable: false

### `fishing-onboarding-strategy.step.adjust-setup`

- seed_key: "fishing-onboarding-strategy.step.adjust-setup"
- phase: "maintenance"
- order_no: 8
- title: "다음 세션 조정"
- description: "실제 병목을 기준으로 가방, 내구도 또는 자동 낚시 준비 중 우선할 항목을 정한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `fishing-onboarding-strategy.section.mode`

- seed_key: "fishing-onboarding-strategy.section.mode"
- section_type: "strategy"
- title: "자동·직접 조작·주간 대회 구분"
- order_no: 1

#### body_markdown

자리를 비우는 시간이 목적이면 자동 낚시의 가방과 내구도를 먼저 본다. 직접 조작한다면 조작 흐름과 세션 목적을 우선하고, 주간 대회는 그 주의 대상과 조건을 최신 콘텐츠에서 별도로 확인한다.

### `fishing-onboarding-strategy.section.bottlenecks`

- seed_key: "fishing-onboarding-strategy.section.bottlenecks"
- section_type: "strategy"
- title: "자동 낚시 병목 판단"
- order_no: 2

#### body_markdown

낚시 시간 감소만 높여도 가방이나 낚싯대 내구도가 먼저 끝나면 세션은 길어지지 않는다. 첫 세션에서 실제로 먼저 소진되는 항목을 확인한 뒤 준비 우선순위를 정한다.

### `fishing-onboarding-strategy.section.mistakes`

- seed_key: "fishing-onboarding-strategy.section.mistakes"
- section_type: "common_mistakes"
- title: "처음 피할 실수"
- order_no: 3

#### body_markdown

방생 기준을 확인하지 않은 채 장시간 자리를 비우거나, 가방과 내구도 여유를 따로 보거나, 주마다 바뀌는 대회 대상과 장소를 고정 정보로 저장하지 않는다. 과거 커뮤니티의 정확한 감소 수치는 현재 공식 규칙처럼 사용하지 않는다.

## Related Contents

### `fishing-onboarding-strategy.current-system`

- seed_key: "fishing-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "fishing-current-system"
- content_name_ko: "낚시 현재 시스템"
- content_category: "life"
- note: "낚시 잠재력·숙련도 등 사실 규칙은 현재 시스템에서 확인한다."
- order_no: 1
- relative_path: "../contents/fishing-current-system.md"
### `fishing-onboarding-strategy.auto`

- seed_key: "fishing-onboarding-strategy.auto"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "auto-fishing"
- content_name_ko: "일반 자동 낚시"
- content_category: "life"
- note: "자동 낚시 시간과 방생 설정의 현재 규칙을 확인한다."
- order_no: 2
- relative_path: "../contents/auto-fishing.md"
### `fishing-onboarding-strategy.freshness`

- seed_key: "fishing-onboarding-strategy.freshness"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "fish-freshness-and-trade"
- content_name_ko: "물고기 신선도와 무역"
- content_category: "life"
- note: "물고기 신선도와 처분 경로를 확인한다."
- order_no: 3
- relative_path: "../contents/fish-freshness-and-trade.md"
### `fishing-onboarding-strategy.imperial`

- seed_key: "fishing-onboarding-strategy.imperial"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "imperial-fishing-delivery"
- content_name_ko: "황실 낚시 납품"
- content_category: "life"
- note: "황실 낚시 납품 경로를 확인한다."
- order_no: 4
- relative_path: "../contents/imperial-fishing-delivery.md"
### `fishing-onboarding-strategy.weekly`

- seed_key: "fishing-onboarding-strategy.weekly"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "fishing-encyclopedia-and-weekly-contest"
- content_name_ko: "어류 도감과 주간 낚시 대회"
- content_category: "life"
- note: "주간 대회의 현재 대상과 조건은 해당 콘텐츠에서 확인한다."
- order_no: 5
- relative_path: "../contents/fishing-encyclopedia-and-weekly-contest.md"
### `fishing-onboarding-strategy.fish-tank`

- seed_key: "fishing-onboarding-strategy.fish-tank"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "mystical-fish-tank"
- content_name_ko: "심청의 신묘한 어항"
- content_category: "life"
- note: "장기 보관 관련 진행도를 확인한다."
- order_no: 6
- relative_path: "../contents/mystical-fish-tank.md"

## Evidence and Sources

### Current evidence

### `fishing-onboarding-strategy.claim.purpose::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.purpose::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "현재 시스템과 전략 책임을 분리한 목적"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.purpose::fishing-basic-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.purpose::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "현재 시스템과 전략 책임을 분리한 목적"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.purpose::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.purpose::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "현재 시스템과 전략 책임을 분리한 목적"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.summary::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.summary::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 낚시 규칙과 조건부 커뮤니티 경험을 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.summary::fishing-afk-bottlenecks-2025-03-11`

- evidence_seed_key: "fishing-onboarding-strategy.claim.summary::fishing-afk-bottlenecks-2025-03-11"
- source_id: "fishing-afk-bottlenecks-2025-03-11"
- title: "Can you AFK Fish for a week?"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1j8fr6g"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2025-03-11"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content"
- entity_id: "fishing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 낚시 규칙과 조건부 커뮤니티 경험을 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.summary::fishing-basic-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.summary::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 낚시 규칙과 조건부 커뮤니티 경험을 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.summary::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.summary::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 낚시 규칙과 조건부 커뮤니티 경험을 분리해 구성한 입문 전략"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.mode-choice::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.mode-choice::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-onboarding-strategy.mode-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "주간 회전 대상은 정적 값으로 포함하지 않음"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.mode-choice::fishing-basic-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.mode-choice::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-onboarding-strategy.mode-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "주간 회전 대상은 정적 값으로 포함하지 않음"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.mode-choice::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.mode-choice::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-onboarding-strategy.mode-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "주간 회전 대상은 정적 값으로 포함하지 않음"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.session-bottlenecks::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.session-bottlenecks::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-onboarding-strategy.session-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 설정과 두 커뮤니티 경험에서 공통으로 확인한 조건부 점검 항목"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.session-bottlenecks::fishing-afk-bottlenecks-2025-03-11`

- evidence_seed_key: "fishing-onboarding-strategy.claim.session-bottlenecks::fishing-afk-bottlenecks-2025-03-11"
- source_id: "fishing-afk-bottlenecks-2025-03-11"
- title: "Can you AFK Fish for a week?"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1j8fr6g"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2025-03-11"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "fishing-onboarding-strategy.session-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 설정과 두 커뮤니티 경험에서 공통으로 확인한 조건부 점검 항목"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.session-bottlenecks::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.session-bottlenecks::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-onboarding-strategy.session-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "공식 설정과 두 커뮤니티 경험에서 공통으로 확인한 조건부 점검 항목"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.section-bottlenecks::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.section-bottlenecks::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fishing-onboarding-strategy.section.bottlenecks"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.section-bottlenecks::fishing-afk-bottlenecks-2025-03-11`

- evidence_seed_key: "fishing-onboarding-strategy.claim.section-bottlenecks::fishing-afk-bottlenecks-2025-03-11"
- source_id: "fishing-afk-bottlenecks-2025-03-11"
- title: "Can you AFK Fish for a week?"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1j8fr6g"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2025-03-11"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_section"
- entity_id: "fishing-onboarding-strategy.section.bottlenecks"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.section-bottlenecks::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.section-bottlenecks::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fishing-onboarding-strategy.section.bottlenecks"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.section-mistakes::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.section-mistakes::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fishing-onboarding-strategy.section.mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "과거 exact 수치와 주간 회전 값을 canonical FACT로 취급하지 않음"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.section-mistakes::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.section-mistakes::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fishing-onboarding-strategy.section.mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "과거 exact 수치와 주간 회전 값을 canonical FACT로 취급하지 않음"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.section-mode::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.section-mode::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fishing-onboarding-strategy.section.mode"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "모드 선택을 조건부 STRATEGY로 분리"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.section-mode::fishing-basic-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.section-mode::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fishing-onboarding-strategy.section.mode"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "모드 선택을 조건부 STRATEGY로 분리"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.section-mode::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.section-mode::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fishing-onboarding-strategy.section.mode"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "모드 선택을 조건부 STRATEGY로 분리"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-adjust-setup::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-adjust-setup::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.adjust-setup"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-adjust-setup::fishing-afk-bottlenecks-2025-03-11`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-adjust-setup::fishing-afk-bottlenecks-2025-03-11"
- source_id: "fishing-afk-bottlenecks-2025-03-11"
- title: "Can you AFK Fish for a week?"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1j8fr6g"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2025-03-11"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.adjust-setup"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-adjust-setup::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-adjust-setup::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.adjust-setup"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-check-potential::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-check-potential::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.check-potential"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-choose-disposal::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-choose-disposal::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.choose-disposal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-choose-disposal::fishing-basic-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-choose-disposal::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.choose-disposal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-choose-mode::fishing-basic-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-choose-mode::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.choose-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-choose-mode::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-choose-mode::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.choose-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-configure-discard::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-configure-discard::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.configure-discard"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-configure-discard::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-configure-discard::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.configure-discard"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-prepare-rod::fishing-afk-bottlenecks-2025-03-11`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-prepare-rod::fishing-afk-bottlenecks-2025-03-11"
- source_id: "fishing-afk-bottlenecks-2025-03-11"
- title: "Can you AFK Fish for a week?"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1j8fr6g"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2025-03-11"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.prepare-rod"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-prepare-rod::fishing-basic-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-prepare-rod::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.prepare-rod"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-reserve-inventory::fishing-advanced-guide`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-reserve-inventory::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.reserve-inventory"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-reserve-inventory::fishing-afk-bottlenecks-2025-03-11`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-reserve-inventory::fishing-afk-bottlenecks-2025-03-11"
- source_id: "fishing-afk-bottlenecks-2025-03-11"
- title: "Can you AFK Fish for a week?"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1j8fr6g"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2025-03-11"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.reserve-inventory"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-run-session::fishing-afk-bottlenecks-2025-03-11`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-run-session::fishing-afk-bottlenecks-2025-03-11"
- source_id: "fishing-afk-bottlenecks-2025-03-11"
- title: "Can you AFK Fish for a week?"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1j8fr6g"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2025-03-11"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "global"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.run-session"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "커뮤니티 경험을 짧은 점검 세션으로 제한"
- active: true
- is_active: true

### `fishing-onboarding-strategy.claim.step-run-session::fishing-onboarding-strategy-2024-12-05`

- evidence_seed_key: "fishing-onboarding-strategy.claim.step-run-session::fishing-onboarding-strategy-2024-12-05"
- source_id: "fishing-onboarding-strategy-2024-12-05"
- title: "낚시가이드#검은사막#초보#고인물#생활#뉴비가이드"
- url: "https://blackdesertonlineyoutube.tistory.com/176"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-12-05"
- retrieved_at: "2026-09-06T00:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fishing-onboarding-strategy.step.run-session"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: "커뮤니티 경험을 짧은 점검 세션으로 제한"
- active: true
- is_active: true

### Historical / inactive evidence

- None
