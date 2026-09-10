<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 요정 레이라 현재 시스템

## Identity

- slug: "fairy-current-system"
- name_ko: "요정 레이라 현재 시스템"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: "solo"
- difficulty: "easy"

## Overview

- summary: "요정 레이라의 현재 획득, 등급, 성장, 주요 기술, 날개돋이, 환생, 기술 변경과 외형·기술 분리 규칙을 정리한다."
- purpose: "오래된 공략과 충돌하는 요정 규칙을 피하고 현재 공식 절차에 따라 첫 요정을 설정한다."

## Requirements

### `fairy-current-system.acquisition`

- seed_key: "fairy-current-system.acquisition"
- kind: "quest"
- requirement_level: "required"
- title: "첫 요정 획득"
- description: "레벨 53 이상이고 현재 가이드가 제시하는 메인 의뢰 분기 중 하나를 완료한 뒤 흑정령 추천 의뢰 '[모험 지원] 요정, 신비스러운 동행'을 진행한다. 의뢰로 봉인된 요정의 날개를 얻거나 카마실브 사원의 테이아에게 레이라의 꽃잎 2개를 봉인된 요정의 날개 1개로 교환할 수 있다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "main_quest_condition": "any_current_guide_path",
  "minimum_level": 53,
  "petal_exchange": {
    "amount": 2,
    "item": "레이라의 꽃잎",
    "result": "봉인된 요정의 날개",
    "result_amount": 1
  },
  "quest_reward": "봉인된 요정의 날개",
  "recommended_quest": "[모험 지원] 요정, 신비스러운 동행"
}
```

### `fairy-current-system.grades`

- seed_key: "fairy-current-system.grades"
- kind: "other"
- requirement_level: "required"
- title: "등급과 최대 레벨"
- description: "요정은 희미한 10레벨, 선명한 20레벨, 영롱한 30레벨, 찬란한 50레벨까지 성장한다."
- structured_value:

```json
{
  "grades": [
    {
      "grade": "희미한",
      "max_level": 10
    },
    {
      "grade": "선명한",
      "max_level": 20
    },
    {
      "grade": "영롱한",
      "max_level": 30
    },
    {
      "grade": "찬란한",
      "max_level": 50
    }
  ],
  "knowledge_role": "fact"
}
```

### `fairy-current-system.growth`

- seed_key: "fairy-current-system.growth"
- kind: "item"
- requirement_level: "required"
- title: "요정 성장"
- description: "요정은 오네테아 흑벌꿀주, 달콤한 벌꿀주 또는 초록색 등급 장비를 성장 재료로 사용한다. 이번 데이터는 전체 성장 경험치 표를 고정하지 않는다."
- structured_value:

```json
{
  "full_experience_table_in_scope": false,
  "growth_resources": [
    "오네테아 흑벌꿀주",
    "달콤한 벌꿀주",
    "초록색 등급 장비"
  ],
  "knowledge_role": "fact"
}
```

### `fairy-current-system.major-skills`

- seed_key: "fairy-current-system.major-skills"
- kind: "other"
- requirement_level: "required"
- title: "주요 기술의 기능"
- description: "신비한 응원은 물약 자동 사용, 아낌없는 손길은 재사용 대기시간이 있는 버프 아이템 자동 사용, 깃털같은 발걸음은 무게 초과 불이익 완화, 요정의 눈물은 경험치 손실 없는 즉시 부활, 마르지 않는 우물은 사막 질병 자동 치료, 샛별은 빛, 간지러운 숨결은 잠수 한도 증가 기능이다. 현재 아낌없는 손길 I~V의 등록 가능 수는 5·8·12·16·25개다."
- structured_value:

```json
{
  "continuous_care_capacity": {
    "I": 5,
    "II": 8,
    "III": 12,
    "IV": 16,
    "V": 25
  },
  "continuous_care_requires_brilliant_grade": true,
  "knowledge_role": "fact",
  "skills": {
    "간지러운 숨결": "underwater_limit",
    "깃털같은 발걸음": "weight_penalty_relief",
    "마르지 않는 우물": "auto_desert_illness_cure",
    "샛별": "light",
    "신비한 응원": "auto_potion",
    "아낌없는 손길": "auto_reuse_buff_items",
    "요정의 눈물": "instant_revive_without_exp_loss"
  }
}
```

### `fairy-current-system.wing-upgrade`

- seed_key: "fairy-current-system.wing-upgrade"
- kind: "item"
- requirement_level: "required"
- title: "날개돋이"
- description: "요정이 현재 등급의 최대 레벨에 도달하면 재료를 사용해 다음 등급 날개돋이를 시도한다. 투입 재료에 따라 성공 확률이 달라지고 성공하면 다음 등급이 되며 배운 기술은 초기화된다. 실패한 요정은 환생하기 전에는 다시 날개돋이를 시도할 수 없다."
- structured_value:

```json
{
  "exact_probability_matrix_in_scope": false,
  "knowledge_role": "fact",
  "learned_skills_reset_on_success": true,
  "material_affects_probability": true,
  "next_grade_on_success": true,
  "requires_current_max_level": true,
  "retry_after_failure_requires_rebirth": true
}
```

### `fairy-current-system.rebirth`

- seed_key: "fairy-current-system.rebirth"
- kind: "other"
- requirement_level: "optional"
- title: "성장 환생과 인격 환생"
- description: "성장 환생은 요정의 레벨과 기술을 초기화하고, 인격 환생은 성격을 변경한다. 날개돋이 실패 뒤 다시 도전하려면 성장 환생이 필요하다."
- structured_value:

```json
{
  "growth_rebirth": {
    "resets_level": true,
    "resets_skills": true
  },
  "knowledge_role": "fact",
  "personality_rebirth": {
    "changes_personality": true
  },
  "required_item": "여왕의 권능"
}
```

### `fairy-current-system.skill-change`

- seed_key: "fairy-current-system.skill-change"
- kind: "item"
- requirement_level: "optional"
- title: "기술 변경"
- description: "테이아의 구슬로 현재 배운 기술 하나를 변경할 수 있다. 한 번 변경할 때 필요한 구슬 수는 현재 배운 기술 수와 같고 결과 확률은 게임 내 기술 변경 화면에서 확인한다."
- structured_value:

```json
{
  "guaranteed_target_skill": false,
  "item": "테이아의 구슬",
  "knowledge_role": "fact",
  "orbs_equal_learned_skill_count": true,
  "probability_visible_in_game": true
}
```

### `fairy-current-system.appearance-skill-separation`

- seed_key: "fairy-current-system.appearance-skill-separation"
- kind: "other"
- requirement_level: "required"
- title: "외형과 고유 기술 분리"
- description: "2026-08-19 이후 보유한 요정 외형과 사용할 고유 기술을 각각 선택한다. 선택할 수 있는 기술은 현재 보유한 요정의 기술이며, 외형 때문에 원하는 고유 기술을 포기해야 한다는 과거 설명은 현재 규칙이 아니다."
- structured_value:

```json
{
  "appearance_determines_skill": false,
  "appearance_selected_separately": true,
  "effective_at": "2026-08-19",
  "knowledge_role": "fact",
  "skill_must_be_owned": true,
  "skill_selected_separately": true
}
```

## Steps

### `fairy-current-system.step.check-unlock`

- seed_key: "fairy-current-system.step.check-unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "레벨 53과 현재 가이드의 메인 의뢰 대체 조건 중 하나를 확인한다."
- checkable: false

### `fairy-current-system.step.complete-quest`

- seed_key: "fairy-current-system.step.complete-quest"
- phase: "unlock"
- order_no: 2
- title: "추천 의뢰 진행"
- description: "흑정령 추천 의뢰 '[모험 지원] 요정, 신비스러운 동행'을 완료한다."
- checkable: false

### `fairy-current-system.step.register-fairy`

- seed_key: "fairy-current-system.step.register-fairy"
- phase: "unlock"
- order_no: 3
- title: "요정 등록"
- description: "봉인된 요정의 날개를 열어 얻은 요정을 등록한다."
- checkable: false

### `fairy-current-system.step.grow-fairy`

- seed_key: "fairy-current-system.step.grow-fairy"
- phase: "preparation"
- order_no: 4
- title: "현재 등급 최대 레벨까지 성장"
- description: "공식 가이드가 안내하는 성장 재료를 사용해 현재 등급의 최대 레벨까지 성장시킨다."
- checkable: false

### `fairy-current-system.step.inspect-skills`

- seed_key: "fairy-current-system.step.inspect-skills"
- phase: "preparation"
- order_no: 5
- title: "기술 기능과 확률 확인"
- description: "활동에 필요한 기술 기능을 구분하고 변경 전 게임 내 결과 확률을 확인한다."
- checkable: false

### `fairy-current-system.step.choose-wing-or-rebirth`

- seed_key: "fairy-current-system.step.choose-wing-or-rebirth"
- phase: "preparation"
- order_no: 6
- title: "날개돋이와 환생 구분"
- description: "다음 등급 도전은 날개돋이, 성장·기술 초기화 또는 성격 변경은 해당 환생으로 구분한다."
- checkable: false

### `fairy-current-system.step.change-skill-if-needed`

- seed_key: "fairy-current-system.step.change-skill-if-needed"
- phase: "maintenance"
- order_no: 7
- title: "필요할 때만 기술 변경"
- description: "보유 기술 수에 따른 테이아의 구슬 소모와 확률을 확인한 뒤 필요한 경우에만 변경한다."
- checkable: false

### `fairy-current-system.step.choose-appearance-and-skill`

- seed_key: "fairy-current-system.step.choose-appearance-and-skill"
- phase: "maintenance"
- order_no: 8
- title: "외형과 기술 각각 선택"
- description: "보유 외형과 보유 고유 기술을 현재 UI에서 서로 독립적으로 선택한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `fairy-current-system.section.system-boundary`

- seed_key: "fairy-current-system.section.system-boundary"
- section_type: "overview"
- title: "서로 다른 변경 작업"
- order_no: 1

#### body_markdown

날개돋이는 최대 레벨 요정의 다음 등급 도전, 성장 환생은 레벨과 기술 초기화, 인격 환생은 성격 변경, 기술 변경은 테이아의 구슬을 사용한 단일 기술 변경이다. 서로 같은 작업으로 취급하지 않는다.

### `fairy-current-system.section.current-continuous-care`

- seed_key: "fairy-current-system.section.current-continuous-care"
- section_type: "notes"
- title: "아낌없는 손길 현재 기준"
- order_no: 2

#### body_markdown

현재 상세 성장표의 I~V 등록 수는 5·8·12·16·25개이며, 2025-09-17 공식 패치가 V를 20개에서 25개로 상향했다고 명시한다. 같은 가이드의 상충하는 상단 표는 current canonical로 사용하지 않는다.

### `fairy-current-system.section.common-mistakes`

- seed_key: "fairy-current-system.section.common-mistakes"
- section_type: "common_mistakes"
- title: "오래된 규칙과 확정 획득 혼동 방지"
- order_no: 3

#### body_markdown

외형과 고유 기술이 종속된 과거 공략, 공식 가이드 상단의 상충 수치, 확률 기술을 보장 획득으로 표현하는 설명을 현재 규칙으로 사용하지 않는다. 테이아의 구슬 사용이나 동일한 종결 기술 세트를 모든 사용자에게 필수로 만들지 않는다.

## Related Contents

### `fairy-current-system.account-progression`

- seed_key: "fairy-current-system.account-progression"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: "가문 성장 이후 사용하는 편의 기반"
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `fairy-current-system.family-convenience`

- seed_key: "fairy-current-system.family-convenience"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "family-convenience-unlock-foundation"
- content_name_ko: "가문 편의 기능 해금"
- content_category: "progression"
- note: "가문 편의 해금 흐름과 연결"
- order_no: 2
- relative_path: "../contents/family-convenience-unlock-foundation.md"
### `fairy-pet-setup-strategy.fairy-facts`

- seed_key: "fairy-pet-setup-strategy.fairy-facts"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "fairy-pet-setup-strategy"
- content_name_ko: "요정·반려동물 초기 설정 전략"
- content_category: "progression"
- note: "현재 요정 시스템 FACT를 판단 근거로 사용"
- order_no: 1
- relative_path: "../contents/fairy-pet-setup-strategy.md"

## Evidence and Sources

### Current evidence

### `fairy-current-system.claim.purpose::fairy-appearance-skill-update-2026-08-19`

- evidence_seed_key: "fairy-current-system.claim.purpose::fairy-appearance-skill-update-2026-08-19"
- source_id: "fairy-appearance-skill-update-2026-08-19"
- title: "8월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.purpose::fairy-continuous-care-update-2025-09-17`

- evidence_seed_key: "fairy-current-system.claim.purpose::fairy-continuous-care-update-2025-09-17"
- source_id: "fairy-continuous-care-update-2025-09-17"
- title: "9월 17일(수) 업데이트 안내 (최종 수정 : 2025-09-17 14:36)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14554"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-09-17"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.purpose::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.purpose::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.summary::fairy-appearance-skill-update-2026-08-19`

- evidence_seed_key: "fairy-current-system.claim.summary::fairy-appearance-skill-update-2026-08-19"
- source_id: "fairy-appearance-skill-update-2026-08-19"
- title: "8월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.summary::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.summary::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.acquisition::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.acquisition::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.acquisition"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.appearance-skill-separation::fairy-appearance-skill-update-2026-08-19`

- evidence_seed_key: "fairy-current-system.claim.appearance-skill-separation::fairy-appearance-skill-update-2026-08-19"
- source_id: "fairy-appearance-skill-update-2026-08-19"
- title: "8월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.appearance-skill-separation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.grades::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.grades::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.grades"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.growth::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.growth::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.growth"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.major-skills::fairy-continuous-care-introduction-2022-08-10`

- evidence_seed_key: "fairy-current-system.claim.major-skills::fairy-continuous-care-introduction-2022-08-10"
- source_id: "fairy-continuous-care-introduction-2022-08-10"
- title: "8월 10일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=8708"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2022-08-10"
- retrieved_at: "2026-09-07T15:30:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.major-skills"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.major-skills::fairy-continuous-care-update-2025-09-17`

- evidence_seed_key: "fairy-current-system.claim.major-skills::fairy-continuous-care-update-2025-09-17"
- source_id: "fairy-continuous-care-update-2025-09-17"
- title: "9월 17일(수) 업데이트 안내 (최종 수정 : 2025-09-17 14:36)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14554"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-09-17"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.major-skills"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.major-skills::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.major-skills::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.major-skills"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.rebirth::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.rebirth::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.rebirth"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.skill-change::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.skill-change::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.skill-change"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.skill-change::fairy-probability-guide-current`

- evidence_seed_key: "fairy-current-system.claim.skill-change::fairy-probability-guide-current"
- source_id: "fairy-probability-guide-current"
- title: "요정 기술 습득 / 날개 돋이 확률"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.skill-change"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.wing-upgrade::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.wing-upgrade::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.wing-upgrade"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.wing-upgrade::fairy-probability-guide-current`

- evidence_seed_key: "fairy-current-system.claim.wing-upgrade::fairy-probability-guide-current"
- source_id: "fairy-probability-guide-current"
- title: "요정 기술 습득 / 날개 돋이 확률"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-current-system.wing-upgrade"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.section.common-mistakes::fairy-appearance-skill-update-2026-08-19`

- evidence_seed_key: "fairy-current-system.claim.section.common-mistakes::fairy-appearance-skill-update-2026-08-19"
- source_id: "fairy-appearance-skill-update-2026-08-19"
- title: "8월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-current-system.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.section.common-mistakes::fairy-continuous-care-update-2025-09-17`

- evidence_seed_key: "fairy-current-system.claim.section.common-mistakes::fairy-continuous-care-update-2025-09-17"
- source_id: "fairy-continuous-care-update-2025-09-17"
- title: "9월 17일(수) 업데이트 안내 (최종 수정 : 2025-09-17 14:36)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14554"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-09-17"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-current-system.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.section.common-mistakes::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.section.common-mistakes::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-current-system.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.section.current-continuous-care::fairy-continuous-care-introduction-2022-08-10`

- evidence_seed_key: "fairy-current-system.claim.section.current-continuous-care::fairy-continuous-care-introduction-2022-08-10"
- source_id: "fairy-continuous-care-introduction-2022-08-10"
- title: "8월 10일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=8708"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2022-08-10"
- retrieved_at: "2026-09-07T15:30:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-current-system.section.current-continuous-care"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.section.current-continuous-care::fairy-continuous-care-update-2025-09-17`

- evidence_seed_key: "fairy-current-system.claim.section.current-continuous-care::fairy-continuous-care-update-2025-09-17"
- source_id: "fairy-continuous-care-update-2025-09-17"
- title: "9월 17일(수) 업데이트 안내 (최종 수정 : 2025-09-17 14:36)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14554"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-09-17"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-current-system.section.current-continuous-care"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.section.current-continuous-care::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.section.current-continuous-care::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-current-system.section.current-continuous-care"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.section.system-boundary::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.section.system-boundary::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-current-system.section.system-boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.change-skill-if-needed::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.change-skill-if-needed::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.change-skill-if-needed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.change-skill-if-needed::fairy-probability-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.change-skill-if-needed::fairy-probability-guide-current"
- source_id: "fairy-probability-guide-current"
- title: "요정 기술 습득 / 날개 돋이 확률"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.change-skill-if-needed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.check-unlock::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.check-unlock::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.check-unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.choose-appearance-and-skill::fairy-appearance-skill-update-2026-08-19`

- evidence_seed_key: "fairy-current-system.claim.step.choose-appearance-and-skill::fairy-appearance-skill-update-2026-08-19"
- source_id: "fairy-appearance-skill-update-2026-08-19"
- title: "8월 19일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.choose-appearance-and-skill"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.choose-wing-or-rebirth::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.choose-wing-or-rebirth::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.choose-wing-or-rebirth"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.complete-quest::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.complete-quest::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.complete-quest"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.grow-fairy::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.grow-fairy::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.grow-fairy"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.inspect-skills::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.inspect-skills::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.inspect-skills"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.inspect-skills::fairy-probability-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.inspect-skills::fairy-probability-guide-current"
- source_id: "fairy-probability-guide-current"
- title: "요정 기술 습득 / 날개 돋이 확률"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.inspect-skills"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-current-system.claim.step.register-fairy::fairy-guide-current`

- evidence_seed_key: "fairy-current-system.claim.step.register-fairy::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-current-system.step.register-fairy"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
