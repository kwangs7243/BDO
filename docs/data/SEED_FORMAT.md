# Seed Format (V1.9Q baseline)

## 정본 파일

- `data/seed_sources.json`: 출처 목록
- `data/seed_contents.json`: 콘텐츠와 중첩 지식·일정·체크리스트·관계·근거
- `data/seed_materials.json`: Project/Recipe 공용 Material 배열
- `data/seed_projects.json`: Project와 중첩 행 (`projects` 객체 필드)
- `data/seed_recipes.json`: `ingredient_groups`, `recipes` 배열을 가진 객체
- importer: `backend/app/seed.py`

모든 파일은 UTF-8 JSON이다. Source/Content는 필수 배열이며 Material/Project/Recipe 파일은 선택적이다. 현재 Project 파일에는 `projects`만 있고 Material 정본은 shared catalog에 있다. 이전 두 파일만 가진 directory는 Project/Recipe import를 건너뛴다. 공유 파일이 없을 때만 과거 Project의 embedded `materials`를 허용한다. 공유 파일과 embedded `materials`가 동시에 있으면 빈 배열이어도 중복 정본 오류다.

## 안정 key 규칙

- 콘텐츠의 정체성은 변경하지 않는 `slug`다.
- seed 관리 중첩 행은 모두 `content-slug.meaningful-name` 형식의 `seed_key`를 가진다.
- 표시 문구, 설명, 순서가 바뀌어도 `seed_key`는 바꾸지 않는다.
- key는 schedule/요구사항/단계/보상/섹션/관계에서는 content 범위, checklist item에서는 template 범위에서 유일해야 한다. 현재 importer는 모든 key가 해당 content slug로 시작하는지도 검사한다.
- seed에서 빠진 기존 중첩 행은 삭제되지 않고 `active=false`로 archive된다. 다시 같은 key가 나타나면 같은 행이 활성화·갱신된다.

## Source 형식

```json
{
  "id": "blood-altar-guide",
  "url": "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168",
  "title": "피의 제단",
  "publisher": "Pearl Abyss",
  "source_type": "official_guide",
  "published_at": null,
  "retrieved_at": "2026-09-03T09:00:00+09:00",
  "region": "KR"
}
```

`published_at`, `retrieved_at`, `region`은 제공될 때 import하고 API에 그대로 노출한다. 없는 날짜를 추측해 넣지 않는다.

## Content 필드

필수 기본 필드는 `slug`, `name_ko`, `category`, `last_verified_at`이다. `summary`, `purpose`, `subcategory`, `party_type`, `difficulty`, `status`는 콘텐츠 기본 설명이다.

중첩 배열:

- `requirements`: `seed_key`, `kind`, `title?`, `description`, `structured_value?`, `requirement_level`, `order_no?`, `active?`
- `steps`: `seed_key`, `phase`, `title`, `description`, `checkable?`, `order_no?`, `active?`
- `rewards`: `seed_key`, `name`, `reward_type`, nullable 수량/선택 필드, `order_no?`, `active?`
- `sections`: `seed_key`, `section_type`, `title`, `body_markdown`, `order_no?`, `active?`
- `schedules`: `seed_key`, `rule_type`, `recurrence_type`, 요일/시각/기간 필드, `active?`
- `checklists`: template 정보와 `items`; 특정 reset을 따를 때 `period_rule_seed_key` 사용
- `relations`: `seed_key`, `to_content_slug`, `relation_type`, `note?`, `order_no?`, `active?`
- `evidence`: claim 단위 근거 선언

허용 enum은 `backend/app/seed.py`의 상수와 `docs/specs/001-core/data-model.md`가 정본이다.

## Checklist period 연결

```json
{
  "seed_key": "garmoth.weekly-reward",
  "name": "가모스 주간 보상 횟수",
  "recurrence_scope": "weekly",
  "period_rule_seed_key": "garmoth.attempt-reset",
  "items": [
    {
      "seed_key": "garmoth.weekly-reward.status",
      "label": "이번 주 보상 횟수 상태 확인"
    }
  ]
}
```

`period_rule_seed_key`는 같은 콘텐츠에 선언된 `quest_reset` 또는 `attempt_reset` schedule만 가리킬 수 있다. `reward_payout`은 연결하면 import가 실패한다. 연결이 없으면 `recurrence_scope`의 기존 일일/목요일 주간 fallback을 사용한다.

## Claim-level evidence mapping

```json
{
  "seed_key": "blood-altar.schedule.reward-payout",
  "entity_type": "schedule_rule",
  "entity_seed_key": "blood-altar.reward-payout",
  "claim_key": "schedule.reward_payout",
  "source_ids": ["blood-altar-guide"],
  "verification_status": "verified",
  "last_verified_at": "2026-09-02",
  "note": "일요일 00:00 보상 지급"
}
```

- `seed_key`: claim 선언의 안정 key
- `entity_type`: 근거가 설명하는 모델 종류
- `entity_seed_key`: 콘텐츠면 slug, 중첩 엔티티면 그 엔티티의 `seed_key`
- `claim_key`: 엔티티 안에서 검증하는 사실의 의미
- `source_ids`: 한 claim을 뒷받침하는 출처 ID 목록

DB의 Evidence `seed_key`는 `{claim seed_key}::{source id}`로 만들어진다. 동일 claim/source 재수입은 기존 Evidence를 갱신한다. `active=false`, `verification_status=superseded`, 또는 `superseded_by`가 있는 근거는 이력으로 보이지만 현재 verification 집계에는 참여하지 않는다.

## 완전한 golden example

아래 `blood-altar`는 V1.6A가 사용하는 기본·요구사항·단계·보상·자유 섹션·일정·체크리스트·관계·claim 근거를 한 콘텐츠에 모두 보여준다. 내용은 기존 저장소의 검증된 seed 사실만 사용했다.

```json
{
  "slug": "blood-altar",
  "name_ko": "피의 제단",
  "category": "combat_pve",
  "summary": "단계형 3인 콘텐츠. 주간 최고 기록에 따른 보상이 일요일 00시에 지급됨.",
  "purpose": "주간 최고 기록에 따른 보상을 받기 위해 진행하는 단계형 콘텐츠.",
  "party_type": "party",
  "status": "active",
  "last_verified_at": "2026-09-02",
  "requirements": [
    {
      "seed_key": "blood-altar.party-size",
      "kind": "party",
      "title": "파티 구성",
      "description": "3인 콘텐츠다.",
      "structured_value": {"party_size": 3},
      "requirement_level": "required"
    }
  ],
  "steps": [
    {
      "seed_key": "blood-altar.weekly-record",
      "phase": "repeat",
      "title": "주간 최고 기록 진행",
      "description": "단계형 콘텐츠를 진행해 주간 최고 기록을 남긴다.",
      "checkable": false
    }
  ],
  "rewards": [
    {
      "seed_key": "blood-altar.weekly-record-reward",
      "name": "주간 최고 기록 보상",
      "reward_type": "weekly_reward",
      "is_choice": false,
      "notes": "일요일 00:00 KST 지급"
    }
  ],
  "sections": [
    {
      "seed_key": "blood-altar.payout-warning",
      "section_type": "common_mistakes",
      "title": "보상 지급과 초기화 구분",
      "body_markdown": "일요일 00:00 보상 지급은 체크리스트 초기화 규칙과 같은 의미가 아니다."
    }
  ],
  "schedules": [
    {
      "seed_key": "blood-altar.reward-payout",
      "rule_type": "reward_payout",
      "recurrence_type": "weekly",
      "weekday": 6,
      "time_local": "00:00",
      "timezone": "Asia/Seoul",
      "notes": "주간 최고 기록 보상 지급: 일요일 00:00 KST"
    }
  ],
  "checklists": [
    {
      "seed_key": "blood-altar.weekly-record-check",
      "name": "피의 제단 주간 기록",
      "recurrence_scope": "weekly",
      "items": [
        {
          "seed_key": "blood-altar.weekly-record-check.status",
          "label": "이번 주 최고 기록 상태 확인"
        }
      ]
    }
  ],
  "relations": [
    {
      "seed_key": "blood-altar.weekly-framework",
      "to_content_slug": "weekly-quest-framework",
      "relation_type": "related"
    }
  ],
  "evidence": [
    {
      "seed_key": "blood-altar.requirement.party-size",
      "entity_type": "content_requirement",
      "entity_seed_key": "blood-altar.party-size",
      "claim_key": "description",
      "source_ids": ["blood-altar-guide"],
      "verification_status": "verified",
      "last_verified_at": "2026-09-02",
      "note": "3인 콘텐츠"
    },
    {
      "seed_key": "blood-altar.schedule.reward-payout",
      "entity_type": "schedule_rule",
      "entity_seed_key": "blood-altar.reward-payout",
      "claim_key": "schedule.reward_payout",
      "source_ids": ["blood-altar-guide"],
      "verification_status": "verified",
      "last_verified_at": "2026-09-02",
      "note": "일요일 00:00 보상 지급"
    }
  ]
}
```

전체 canonical 행과 나머지 claim들은 `data/seed_contents.json`의 `blood-altar` 항목을 사용한다.

## Project seed 형식 (V1.8A 호환, V1.9Q shared catalog)

현재 `seed_projects.json`의 최상위 구조는 다음과 같다. 아래 Material key는 별도 `seed_materials.json`에 먼저 정의한다.

```json
{
  "projects": [
    {
      "slug": "project-slug",
      "name_ko": "프로젝트 이름",
      "content_slug": "existing-content-slug",
      "summary": "설명",
      "active": true,
      "stages": [
        {"seed_key": "project-slug.stage.prepare", "name": "준비", "order_no": 1}
      ],
      "stage_dependencies": [
        {
          "seed_key": "project-slug.dependency.finish-prepare",
          "stage_seed_key": "project-slug.stage.finish",
          "depends_on_stage_seed_key": "project-slug.stage.prepare"
        }
      ],
      "project_materials": [
        {
          "seed_key": "project-slug.material.example",
          "stage_seed_key": "project-slug.stage.prepare",
          "material_key": "stable-material-key",
          "required_quantity": 10,
          "order_no": 1,
          "source_entity_type": "content_requirement",
          "source_entity_seed_key": "existing-content-slug.requirement-key",
          "sources": [
            {
              "seed_key": "project-slug.material.example.source.content",
              "content_slug": "existing-source-content",
              "quantity_per_completion": null,
              "notes": "정확한 1회 획득량이 없으면 null",
              "order_no": 1
            }
          ]
        }
      ]
    }
  ]
}
```

- Material identity는 표시명 대신 전역 unique `key`를 사용한다.
- Project 하위 `seed_key`는 `{project slug}.`로 시작해야 하며 부모 범위에서 유일해야 한다.
- `content_slug`, stage 참조, material 참조와 `source_entity_*` 참조는 기존 정본 row가 존재해야 한다.
- `source_entity_type`은 현재 `content_requirement` 또는 `content_section`만 허용한다.
- `required_quantity`와 값이 존재하는 `quantity_per_completion`은 0 이상이어야 한다.
- stage dependency의 자기 참조와 순환은 import 오류다.
- 현재 canonical 파일에서 빠진 Project 계열 row는 hard delete하지 않고 `active=false`로 archive한다.
- 동일 stable key를 다시 import하면 기존 ID를 유지하며 값을 갱신한다.
- `UserMaterialInventory`와 `UserProjectStageState`는 사용자 소유이므로 seed에 작성하지 않으며 importer도 수정하거나 archive하지 않는다.

## 검토 절차

검증용 import는 임시 DB에서 실행한다. 기본 설정의 seed CLI는 실제 로컬 DB를 수정하므로 검증 목적으로 무심코 실행하지 않는다.

1. 기존 행이면 `seed_key`를 유지하고 사실·문구·검증일만 수정한다.
2. 정확한 변동 사실은 별도 evidence claim에 연결한다.
3. 수량/시간이 확인되지 않았으면 nullable/미기재로 둔다.
4. 삭제가 필요하면 JSON에서 제거하거나 `active=false`로 두고 import 후 이력이 보존되는지 테스트한다.
5. 임시 DB를 쓰는 `uv run pytest tests/test_recipe_seed.py tests/test_recipe_migration.py` 등 해당 회귀에서 중복 수, 변경 행 ID, checklist history를 검증한다.

## V1.9Q shared Material catalog

```json
[
  {"key": "wheat", "name_ko": "밀", "unit": "개", "active": true}
]
```

`material_seed.sync_materials`가 key로 제자리 갱신한다. shared catalog에서 빠진 Material만 archive한다. 파일 자체가 없으면 기존 행을 archive하지 않는다. legacy embedded catalog는 부분 목록이므로 다른 도메인의 Material을 archive하지 않는다. Project importer는 전역 Material 동기화/삭제를 수행하지 않는다. Recipe와 Project 모두 반환된 공유 key map을 resolve한다. 표시명 변경은 key/ID/FK/개인 재고를 바꾸지 않는다. 실제 전체 목록은 41개이며 기존 Carrack 9개가 포함된다.

## V1.9Q/V1.9X Recipe 입력 계약

정확한 validation 정의는 `backend/app/recipe_seed.py`의 Pydantic 모델이다. 알려지지 않은 Recipe 필드는 거부한다. 아래 `?`는 선택 필드다.

| 계층 | 필수 필드 | 선택 필드/기본값 |
| --- | --- | --- |
| Group | `key`, `name_ko`, `last_verified_at` | `members=[]`, `evidence=[]`, `active=true` |
| Member | `seed_key`, `material_key` | `order_no=1`, `active=true` |
| Recipe | `slug`, `name_ko`, `process_type`, `result_material_key`, `last_verified_at` | `summary=null`, `required_skill_tier=null`, `required_skill_level=null`, `ingredients=[]`, `evidence=[]`, `active=true` |
| Slot | `seed_key`, `label` | `options=[]`, `order_no=1`, `notes=null`, `active=true` |
| Option | `seed_key`, `required_quantity`, 정확히 하나의 `material_key` 또는 `ingredient_group_key` | `order_no=1`, `notes=null`, `active=true` |
| Evidence | `seed_key`, `entity_type`, `entity_seed_key`, `claim_key`, `source_ids`, `last_verified_at` | `verification_status=unverified`, `note=null`, `active=true` |

현재 process는 formulation-style `cooking`, `alchemy`만 지원하며 skill tier는 `beginner`, `apprentice`, `skilled`, `professional`, `artisan`, `master`, `guru`다. Processing 계열 process는 지원하지 않는다. level은 null 또는 양의 정수다. option quantity는 유한한 양수다. result/member/option 참조와 Source ID는 존재해야 한다. 중복 recipe slug/group key/member material/중첩 key/evidence key는 거부한다.

Stable key 예시: `beer`, `ingredient-group.grain.wheat`, `beer.water`, `beer.water.mineral-water`. Slot key는 Recipe slug, Option key는 Slot key, Member key는 `ingredient-group.{group key}.`로 시작한다. 같은 key는 기존 ID를 유지하며 누락 행은 archive한다. 부모가 비활성화되면 하위 row와 관련 Evidence도 비활성화한다. 동일 key 재등장은 기존 row를 재활성화한다. Recipe 파일 부재는 과거 seed import로 간주하여 기존 Recipe를 archive하지 않는다.

Evidence target은 `recipe`(Recipe slug), `recipe_ingredient_slot`(Slot key), `recipe_ingredient_option`(Option key), `ingredient_group`(Group key)다. 해당 소유자의 `evidence` 배열에 기록하고 `(entity_type, entity_seed_key)`로 구분한다. DB Evidence stable key는 `{claim seed_key}::{source_id}`다. 정상 조회는 active 구조를 반환하며 Evidence의 inactive/superseded 이력은 따로 유지한다.

수량은 **Recipe의 완전한 1회 배합** 기준이다. 슬롯 간 AND, 같은 슬롯 옵션 간 OR이며 IngredientGroup은 멤버십만 나타낸다. 전역 multiplier, 고급/특상품 환산, 혼합 대체, 결과물 고정 수량, 감소 투입 성공 확률을 추론하지 않는다. 예를 들어 맥주의 물 슬롯은 `mineral-water:6` 또는 `purified-water:3`, 집중의 비약 약초 슬롯은 `wild-grass:2` 또는 `weed:8`인 별도 option이다. 연금 수량은 성공 가능성이 있는 최소 투입량이 아니라 canonical full formulation이다.

공식 현행 가이드의 그룹 멤버십·1회 시도 의미는 verified, 공식 현행 exact formula 확인이 부족한 배합·option quantity는 needs_review로 유지한다. conflict/superseded는 편한 값을 선택해 verified로 승격하지 않는다. 날짜는 확인한 날을 사용하며 모르는 발행일은 null로 둔다.

seed에는 numeric DB ID, 사용자 inventory/note/state, shortage, 계산 결과, generated export 필드를 작성하지 않는다. 개인 재고는 기존 UserMaterialInventory와 backup version 1의 별도 소유 영역이다. Recipe API/export는 사용자 상태를 읽지 않는다.
