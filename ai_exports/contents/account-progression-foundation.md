<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가문 성장 기반

## Identity

- slug: "account-progression-foundation"
- name_ko: "가문 성장 기반"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "메인 의뢰, 영구 가문 보상, 콘텐츠 해금과 편의 기능을 한 흐름으로 추적하는 최상위 기반이다."
- purpose: "일회성 가문 성장을 반복 숙제와 구분하고 하위 콘텐츠의 진행 상태를 연결한다."

## Requirements

### `account-progression-foundation.scope`

- seed_key: "account-progression-foundation.scope"
- kind: "knowledge"
- requirement_level: "required"
- title: "가문 단위 성장 범위"
- description: "메인 의뢰와 모험일지에는 가문 전체에 적용되는 영구 능력치·편의·콘텐츠 해금 보상이 포함된다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "persistence": "permanent",
  "scope": "family"
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

### `account-progression-foundation.energy`

- seed_key: "account-progression-foundation.energy"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "energy-foundation"
- content_name_ko: "기운 기반"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/energy-foundation.md"
### `account-progression-foundation.contribution`

- seed_key: "account-progression-foundation.contribution"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "contribution-economy-foundation"
- content_name_ko: "공헌도 경제 기반"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/contribution-economy-foundation.md"
### `account-progression-foundation.ecology`

- seed_key: "account-progression-foundation.ecology"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "ecology-family-drop-bonus"
- content_name_ko: "생태 지식·가문 명성 획득 확률 보너스"
- content_category: "combat_pve"
- note: null
- order_no: 3
- relative_path: "../contents/ecology-family-drop-bonus.md"
### `account-progression-foundation.combat`

- seed_key: "account-progression-foundation.combat"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "combat-gear-progression-strategy"
- content_name_ko: "전투 장비 성장 전략"
- content_category: "combat_pve"
- note: null
- order_no: 4
- relative_path: "../contents/combat-gear-progression-strategy.md"
### `account-progression-foundation.life`

- seed_key: "account-progression-foundation.life"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-family-levels"
- content_name_ko: "가문 통합 생활 레벨"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/life-family-levels.md"
### `account-progression-foundation.grind`

- seed_key: "account-progression-foundation.grind"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-recommendation-system"
- content_name_ko: "사냥터 추천 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 6
- relative_path: "../contents/grind-zone-recommendation-system.md"
### `account-progression-foundation.carrack`

- seed_key: "account-progression-foundation.carrack"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: null
- order_no: 7
- relative_path: "../contents/carrack-advance.md"
### `account-progression-foundation.panokseon`

- seed_key: "account-progression-foundation.panokseon"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "panokseon"
- content_name_ko: "판옥선"
- content_category: "ocean_guide"
- note: null
- order_no: 8
- relative_path: "../contents/panokseon.md"
### `account-progression-foundation.barter`

- seed_key: "account-progression-foundation.barter"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: null
- order_no: 9
- relative_path: "../contents/barter-current-system.md"
### `adventure-log-foundation.account`

- seed_key: "adventure-log-foundation.account"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventure-log-foundation.md"
### `content-unlock-foundation.account`

- seed_key: "content-unlock-foundation.account"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "content-unlock-foundation"
- content_name_ko: "콘텐츠 해금 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/content-unlock-foundation.md"
### `fairy-current-system.account-progression`

- seed_key: "fairy-current-system.account-progression"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fairy-current-system"
- content_name_ko: "요정 레이라 현재 시스템"
- content_category: "progression"
- note: "가문 성장 이후 사용하는 편의 기반"
- order_no: 1
- relative_path: "../contents/fairy-current-system.md"
### `family-convenience-unlock-foundation.account`

- seed_key: "family-convenience-unlock-foundation.account"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "family-convenience-unlock-foundation"
- content_name_ko: "가문 편의 기능 해금"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/family-convenience-unlock-foundation.md"
### `magnus-progression.account`

- seed_key: "magnus-progression.account"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "magnus-progression"
- content_name_ko: "마그누스 전체 진행"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/magnus-progression.md"
### `main-quest-progression-foundation.account`

- seed_key: "main-quest-progression-foundation.account"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `permanent-family-reward-foundation.account`

- seed_key: "permanent-family-reward-foundation.account"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "permanent-family-reward-foundation"
- content_name_ko: "영구 가문 보상 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/permanent-family-reward-foundation.md"
### `pet-current-system.account-progression`

- seed_key: "pet-current-system.account-progression"
- direction: "incoming"
- relation_type: "related"
- content_slug: "pet-current-system"
- content_name_ko: "반려동물 현재 시스템"
- content_category: "progression"
- note: "가문 단위 반려동물 등록과 성장 기반"
- order_no: 1
- relative_path: "../contents/pet-current-system.md"

## Evidence and Sources

### Current evidence

### `account-progression-foundation.claim.scope::adventure-log-bookshelf-guide`

- evidence_seed_key: "account-progression-foundation.claim.scope::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "account-progression-foundation.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `account-progression-foundation.claim.scope::magnus-guide`

- evidence_seed_key: "account-progression-foundation.claim.scope::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "account-progression-foundation.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
