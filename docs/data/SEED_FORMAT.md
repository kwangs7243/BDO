# Seed Format (V1.8A baseline)

## 정본 파일

- `data/seed_sources.json`: 출처 목록
- `data/seed_contents.json`: 콘텐츠와 중첩 지식·일정·체크리스트·관계·근거
- importer: `backend/app/seed.py`

`seed_sources.json`과 `seed_contents.json`은 UTF-8 JSON 배열이다. V1.8A의 선택 파일 `seed_projects.json`은 `materials`와 `projects` 배열을 가진 UTF-8 JSON 객체다. 기존 두 파일만 가진 임시 seed directory에서는 project import를 건너뛰어 과거 회귀 테스트와 importer 호환성을 유지한다.

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

## V1.8A Project seed 형식

`seed_projects.json`의 최상위 구조는 다음과 같다.

```json
{
  "materials": [
    {"key": "stable-material-key", "name_ko": "표시 이름", "unit": "개", "active": true}
  ],
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

1. 기존 행이면 `seed_key`를 유지하고 사실·문구·검증일만 수정한다.
2. 정확한 변동 사실은 별도 evidence claim에 연결한다.
3. 수량/시간이 확인되지 않았으면 nullable/미기재로 둔다.
4. 삭제가 필요하면 JSON에서 제거하거나 `active=false`로 두고 import 후 이력이 보존되는지 테스트한다.
5. `uv run python -m app.seed` 재실행 후 중복 수, 변경 행 ID, checklist history를 검증한다.
