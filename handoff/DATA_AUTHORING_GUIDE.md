# BDO Data Authoring Guide

이 문서는 V1.6A 구현에 맞춰 외부 Research/Data Agent가 검은사막 KR 콘텐츠 seed를 작성하기 위한 작업 지침이다. 신규 사실은 반드시 조사 근거가 있어야 하며, 아래 예시는 구조 설명용 placeholder이지 게임 사실이 아니다.

정본은 다음 순서로 확인한다.

1. docs/data/SEED_FORMAT.md
2. data/seed_sources.json
3. data/seed_contents.json
4. backend/app/seed.py
5. backend/app/models.py, backend/app/schemas.py, backend/app/periods.py

## 1. 새 Content 하나를 추가하는 완전한 JSON 예시

먼저 data/seed_sources.json 배열에 출처를 추가한다.

~~~json
{
  "id": "replace-content-official-source",
  "url": "https://REPLACE_WITH_KR_OFFICIAL_URL",
  "title": "공식 문서 제목을 그대로 입력",
  "publisher": "Pearl Abyss",
  "source_type": "official_guide",
  "published_at": null,
  "retrieved_at": "YYYY-MM-DDTHH:MM:SS+09:00",
  "region": "KR"
}
~~~

source_type canonical 값은 official_patch, official_guide, official_gm, official_forum, community, database다. 기존 분류로 표현할 수 없는 값을 임의로 만들지 않는다.

그다음 data/seed_contents.json 배열에 아래와 같은 content object를 추가한다. 모든 REPLACE 값과 날짜를 실제 조사 결과로 바꾸기 전에는 import하지 않는다.

~~~json
{
  "slug": "replace-content-slug",
  "name_ko": "REPLACE 콘텐츠명",
  "category": "REPLACE_EXISTING_CATEGORY",
  "subcategory": null,
  "summary": "근거로 확인된 한 문장 설명",
  "purpose": "근거로 확인된 이용 목적",
  "party_type": null,
  "difficulty": null,
  "status": "active",
  "last_verified_at": "YYYY-MM-DD",
  "requirements": [
    {
      "seed_key": "replace-content-slug.requirement.unlock",
      "kind": "quest",
      "title": "선행 의뢰",
      "description": "확인된 선행조건을 입력",
      "structured_value": null,
      "requirement_level": "required",
      "order_no": 1
    }
  ],
  "sections": [
    {
      "seed_key": "replace-content-slug.section.preparation",
      "section_type": "preparation",
      "title": "준비",
      "body_markdown": "출처로 확인한 준비 설명",
      "order_no": 1
    }
  ],
  "steps": [
    {
      "seed_key": "replace-content-slug.step.first-entry",
      "phase": "first_time",
      "order_no": 1,
      "title": "최초 진입",
      "description": "출처로 확인한 최초 진행 단계",
      "checkable": false
    }
  ],
  "rewards": [
    {
      "seed_key": "replace-content-slug.reward.choice",
      "name": "확인된 선택 보상명",
      "reward_type": "choice_reward",
      "amount": null,
      "min_amount": null,
      "max_amount": null,
      "unit": null,
      "is_choice": true,
      "choice_group": "replace-content-slug.choice-group-1",
      "recommendation": "근거가 있을 때만 선택 추천과 조건을 입력",
      "notes": null,
      "order_no": 1
    }
  ],
  "schedules": [
    {
      "seed_key": "replace-content-slug.schedule.quest-reset",
      "rule_type": "quest_reset",
      "recurrence_type": "weekly",
      "weekday": 3,
      "time_local": "00:00",
      "timezone": "Asia/Seoul",
      "effective_from": null,
      "effective_to": null,
      "notes": "검증된 reset 설명"
    }
  ],
  "checklists": [
    {
      "seed_key": "replace-content-slug.checklist.weekly",
      "name": "REPLACE 주간 체크",
      "recurrence_scope": "weekly",
      "period_rule_seed_key": "replace-content-slug.schedule.quest-reset",
      "enabled_default": true,
      "items": [
        {
          "seed_key": "replace-content-slug.checklist.weekly.complete",
          "order_no": 1,
          "label": "검증된 반복 행동",
          "details": null,
          "reward_hint": null
        }
      ]
    }
  ],
  "relations": [
    {
      "seed_key": "replace-content-slug.relation.prerequisite",
      "to_content_slug": "REPLACE_EXISTING_TARGET_SLUG",
      "relation_type": "prerequisite",
      "note": "관계의 근거 또는 범위",
      "order_no": 1
    }
  ],
  "evidence": [
    {
      "seed_key": "replace-content-slug.evidence.summary",
      "entity_type": "content",
      "entity_seed_key": "replace-content-slug",
      "claim_key": "summary",
      "source_ids": ["replace-content-official-source"],
      "verification_status": "needs_review",
      "last_verified_at": "YYYY-MM-DD",
      "note": "출처가 뒷받침하는 claim을 짧게 요약"
    },
    {
      "seed_key": "replace-content-slug.evidence.requirement.unlock",
      "entity_type": "content_requirement",
      "entity_seed_key": "replace-content-slug.requirement.unlock",
      "claim_key": "description",
      "source_ids": ["replace-content-official-source"],
      "verification_status": "needs_review",
      "last_verified_at": "YYYY-MM-DD",
      "note": "선행조건 근거"
    },
    {
      "seed_key": "replace-content-slug.evidence.schedule.quest-reset",
      "entity_type": "schedule_rule",
      "entity_seed_key": "replace-content-slug.schedule.quest-reset",
      "claim_key": "schedule.quest_reset",
      "source_ids": ["replace-content-official-source"],
      "verification_status": "needs_review",
      "last_verified_at": "YYYY-MM-DD",
      "note": "요일과 시각을 직접 명시한 근거"
    }
  ]
}
~~~

목요일은 weekday 3이라는 형식 예시일 뿐이다. 대상 콘텐츠의 실제 reset이 목요일이라는 뜻이 아니므로 반드시 공식 근거로 교체한다.

## 2. Requirement 예시

~~~json
{
  "seed_key": "content-slug.requirement.party-size",
  "kind": "party",
  "title": "파티 구성",
  "description": "검증된 파티 조건",
  "structured_value": {"party_size": 3},
  "requirement_level": "required",
  "order_no": 1,
  "active": true
}
~~~

kind 허용값:

- quest, level, gear, stat, item, knowledge, party, character, other

requirement_level 허용값:

- required, recommended, optional

structured_value는 숫자·단위·ID처럼 기계적으로 사용할 값이 있을 때만 JSON object/array로 쓴다. 설명과 값이 충돌하지 않게 하고, 불확실한 수량은 넣지 않는다.

## 3. Section 예시

~~~json
{
  "seed_key": "content-slug.section.common-mistakes",
  "section_type": "common_mistakes",
  "title": "흔한 실수",
  "body_markdown": "근거로 확인한 주의사항",
  "order_no": 1
}
~~~

section_type 허용값:

- overview, why, preparation, start, strategy, common_mistakes, notes

Requirement/Step/Reward/Schedule로 표현해야 하는 정확한 사실을 Section prose에만 숨기지 않는다.

## 4. Step 예시

~~~json
{
  "seed_key": "content-slug.step.repeat-1",
  "phase": "repeat",
  "order_no": 1,
  "title": "반복 진행",
  "description": "검증된 반복 순서",
  "checkable": false
}
~~~

phase 허용값:

- unlock, preparation, first_time, repeat, reward, maintenance

Step은 공용 지식/절차다. 기간별 완료 상태가 필요하면 checklist template/item을 사용하며 Step에 사용자 완료값을 넣지 않는다.

## 5. Reward 및 추천 선택 예시

일반 보상:

~~~json
{
  "seed_key": "content-slug.reward.primary",
  "name": "확인된 보상명",
  "reward_type": "weekly_reward",
  "amount": null,
  "min_amount": null,
  "max_amount": null,
  "unit": null,
  "is_choice": false,
  "choice_group": null,
  "recommendation": null,
  "notes": "보상 조건이 확인된 경우 입력",
  "order_no": 1
}
~~~

선택 보상:

~~~json
{
  "seed_key": "content-slug.reward.choice-a",
  "name": "확인된 선택지명",
  "reward_type": "choice_reward",
  "amount": null,
  "min_amount": null,
  "max_amount": null,
  "unit": null,
  "is_choice": true,
  "choice_group": "content-slug.choice-group-1",
  "recommendation": "공식 효과와 사용 조건이 확인된 경우에만 추천 기준 입력",
  "notes": null,
  "order_no": 1
}
~~~

reward_type은 현재 importer가 enum 검증하지 않는다. 기존 canonical 용어를 재사용하고 새 용어를 임의로 만들지 않는다. 정확한 수량이 확인되지 않으면 amount/min_amount/max_amount를 null로 둔다. 개인 취향이나 추측을 recommendation으로 확정 서술하지 않는다.

## 6. reset / reward_payout / spawn_schedule 예시

현재 구현의 출현 schedule rule_type 문자열은 spawn이다. 문서 개념명 spawn_schedule을 JSON에 그대로 쓰지 않는다.

canonical rule_type은 quest_reset, attempt_reset, record_cutoff, reward_payout, spawn, event_end다. recurrence_type은 daily, weekly, fixed_datetime, manual을 사용한다. importer가 두 필드의 enum 조합을 모두 강제하지 않으므로 작성자가 이 목록과 의미를 지켜야 한다.

일일 reset:

~~~json
{
  "seed_key": "content-slug.schedule.daily-reset",
  "rule_type": "quest_reset",
  "recurrence_type": "daily",
  "time_local": "06:00",
  "timezone": "Asia/Seoul",
  "notes": "검증된 일일 reset 설명"
}
~~~

주간 reset:

~~~json
{
  "seed_key": "content-slug.schedule.weekly-reset",
  "rule_type": "attempt_reset",
  "recurrence_type": "weekly",
  "weekday": 0,
  "time_local": "06:00",
  "timezone": "Asia/Seoul",
  "notes": "검증된 주간 reset 설명"
}
~~~

weekday는 Monday=0부터 Sunday=6이다. 위 요일과 시각은 형식 예시다.

보상 지급:

~~~json
{
  "seed_key": "content-slug.schedule.reward-payout",
  "rule_type": "reward_payout",
  "recurrence_type": "weekly",
  "weekday": 6,
  "time_local": "00:00",
  "timezone": "Asia/Seoul",
  "notes": "검증된 보상 지급 설명"
}
~~~

출현 일정:

~~~json
{
  "seed_key": "content-slug.schedule.spawn-1",
  "rule_type": "spawn",
  "recurrence_type": "weekly",
  "weekday": 2,
  "time_local": "20:00",
  "timezone": "Asia/Seoul",
  "notes": "검증된 출현 일정"
}
~~~

고정 일정이면 recurrence_type을 fixed_datetime으로 두고 timezone offset이 포함된 fixed_datetime을 사용한다.

~~~json
{
  "seed_key": "content-slug.schedule.fixed-spawn",
  "rule_type": "spawn",
  "recurrence_type": "fixed_datetime",
  "fixed_datetime": "YYYY-MM-DDTHH:MM:SS+09:00",
  "timezone": "Asia/Seoul",
  "notes": "검증된 단일 출현 시각"
}
~~~

quest_reset과 attempt_reset만 checklist의 period_rule_seed_key가 될 수 있다. reward_payout, record_cutoff, spawn, event_end를 checklist reset으로 연결하면 안 된다.

## 7. Relation 예시

~~~json
{
  "seed_key": "content-slug.relation.required-content",
  "to_content_slug": "existing-target-slug",
  "relation_type": "prerequisite",
  "note": "선행 관계의 근거",
  "order_no": 1
}
~~~

relation_type 허용값:

- prerequisite, unlocks, related, source_for, part_of, alternative, project_link

to_content_slug는 data/seed_contents.json 안에 이미 있거나 같은 변경에서 함께 추가된 Content여야 한다. 역방향 행을 중복 작성하지 않는다. API가 incoming/outgoing 관계를 모두 조회한다.

## 8. claim별 Evidence 연결 예시

Content summary:

~~~json
{
  "seed_key": "content-slug.evidence.summary",
  "entity_type": "content",
  "entity_seed_key": "content-slug",
  "claim_key": "summary",
  "source_ids": ["official-source-id"],
  "verification_status": "verified",
  "last_verified_at": "YYYY-MM-DD",
  "note": "공식 문서가 확인하는 요약"
}
~~~

중첩 엔티티:

~~~json
{
  "seed_key": "content-slug.evidence.reward.primary",
  "entity_type": "reward",
  "entity_seed_key": "content-slug.reward.primary",
  "claim_key": "reward",
  "source_ids": ["official-source-id"],
  "verification_status": "verified",
  "last_verified_at": "YYYY-MM-DD",
  "note": "보상명과 조건 근거"
}
~~~

권장 entity_type과 claim_key:

| 대상 | entity_type | entity_seed_key | 대표 claim_key |
|---|---|---|---|
| Content | content | content slug | summary, purpose |
| Requirement | content_requirement | requirement seed_key | description, structured_value |
| Section | content_section | section seed_key | body |
| Step | content_step | step seed_key | description |
| Reward | reward | reward seed_key | reward, amount, recommendation |
| Schedule | schedule_rule | schedule seed_key | schedule.quest_reset 등 |
| Relation | content_relation | relation seed_key | relation |
| Checklist | checklist_template 또는 checklist_template_item | 해당 seed_key | recurrence, label |

하나의 claim에 여러 출처가 같은 상태로 근거를 제공하면 source_ids에 함께 넣을 수 있다. 출처별 상태가 다르면 Evidence 선언을 분리한다. DB Evidence seed_key는 importer가 {claim seed_key}::{source id}로 만든다.

## 9. verified / needs_review / conflict / superseded 사용 규칙

- verified: 현재 KR 공식 자료 또는 정책에 맞는 충분한 근거로 사실이 확인됨.
- needs_review: 출처가 부족하거나 오래됐거나 최신 상태 확인이 더 필요함. 불확실한 사실을 verified로 올리지 않는다.
- conflict: 현재 유효한 출처들이 같은 claim에 대해 서로 다른 내용을 말함. 양쪽 근거를 별도 Evidence로 유지하고 note에 충돌점을 쓴다.
- superseded: 과거에는 맞았지만 더 최신 근거로 대체됨. 과거 Evidence를 삭제하지 말고 별도 선언으로 유지한다. 새 근거는 새 안정 key의 verified Evidence로 추가한다.

superseded Evidence는 기본적으로 current 집계에서 제외된다. 명시적으로 active=false를 함께 쓰는 것을 권장한다. superseded_by DB FK는 현재 seed importer 입력 필드가 아니므로 작성하지 않는다.

stale은 별도 저장 status가 아니다. 시간 의존 claim이 오래되어 재검증이 필요하면 needs_review를 사용한다. 근거가 전혀 없는 값을 확정 사실처럼 작성하지 말고 nullable/미기재로 남긴다. 불가피하게 기존 미검증 claim을 표현할 때만 unverified를 사용한다. 현재 importer는 verification_status 문자열 enum을 강제 검증하지 않으므로 canonical 값 외 문자열을 만들면 안 된다.

## 10. seed_key 네이밍 규칙

- 소문자 ASCII kebab-case를 사용한다.
- 모든 nested key는 정확히 content-slug. 접두사로 시작해야 한다.
- 형식: content-slug.entity-type.semantic-name
- 문구, 번역, order_no, 출처 URL이 바뀌어도 key는 유지한다.
- 숫자 index보다 의미 있는 이름을 쓴다.
- 같은 부모 범위에서 중복하지 않는다.
- Evidence claim key와 DB Evidence key를 구분한다. 작성자는 claim seed_key만 쓰며 ::source-id 접미사는 importer가 만든다.

예:

- content-slug.requirement.unlock
- content-slug.section.preparation
- content-slug.step.repeat-1
- content-slug.reward.weekly-choice
- content-slug.schedule.quest-reset
- content-slug.relation.prerequisite
- content-slug.evidence.schedule.quest-reset

## 11. 기존 seed 수정 시 importer의 동작

- Source는 id로 upsert하며 URL/title/publisher/type/published/retrieved/region을 갱신한다.
- Content는 slug로 upsert한다.
- nested entity는 부모 범위의 seed_key로 기존 행을 찾아 text/details/order/schedule/reward hint/active를 제자리 갱신한다.
- Evidence는 claim seed_key와 source_id의 조합으로 기존 행을 갱신한다.
- 같은 key의 문구만 바꾸면 DB ID와 checklist history가 유지된다.
- UserContentState는 seed importer가 읽거나 덮어쓰지 않는다.
- Source notes는 현재 Source 모델에 저장되지 않는다. 근거 설명은 Evidence note에 둔다.

중요: 기존 Content에서 schedules/requirements/steps/rewards/sections/checklists/relations/evidence 배열을 생략하면 importer는 빈 배열로 해석해 해당 canonical nested 행을 archive할 수 있다. 부분 patch 파일처럼 작성하지 말고 기존 object 전체를 유지한 채 수정한다.

## 12. archive 처리 규칙

- nested entity가 해당 Content의 canonical 배열에서 사라지면 active=false가 된다.
- 다시 같은 seed_key로 추가하고 active=true이면 같은 행을 재사용한다.
- checklist item archive는 과거 ChecklistItemState를 삭제하지 않는다.
- Evidence 선언이 사라지면 해당 content slug 범위의 기존 seeded Evidence는 active=false가 된다.
- Content 자체를 data 파일에서 제거해도 현재 importer는 자동 archive하지 않는다. Content를 중단 표시하려면 합의된 status를 명시한다.
- Source가 source 파일에서 사라져도 자동 삭제되지 않는다. 사용 중인 source_id를 먼저 제거하거나 archive한 Evidence와의 관계를 검토한다.
- seed_key를 바꾸는 것은 rename이 아니라 이전 행 archive + 새 행 생성이다. 단순 문구 수정에서 key를 바꾸지 않는다.

## 13. seed validation 실행 명령

프로젝트 루트에서 JSON 문법과 importer/idempotence를 실제 bdo.db 변경 없이 검사한다.

~~~powershell
cd backend
uv run python -c "import json, pathlib; [json.loads(pathlib.Path(path).read_text(encoding='utf-8')) for path in ('../data/seed_sources.json', '../data/seed_contents.json')]; print('seed JSON valid')"
uv run pytest -q tests/test_seed.py
~~~

전체 회귀 검증:

~~~powershell
uv run pytest -q
~~~

uv run python -m app.seed는 설정된 DATABASE_URL DB를 실제 갱신한다. Research Agent는 검토/승인 없이 이 명령을 실제 사용자 DB에 실행하지 않는다.

## 14. 절대 생성하지 않을 필드와 자동 생성 필드

Research Agent가 seed JSON에 쓰지 않는 필드:

- 모든 DB id, content_id, from_content_id, to_content_id, template_id, period_rule_id, source_id FK
- Evidence의 DB seed_key 완성값(::source-id 포함)과 superseded_by
- Content 최상위 verification_status: active Evidence에서 계산됨
- is_active, next_occurrence, relation direction: API 계산/직렬화 값
- UserContentState 전체: state, priority, note, updated_at은 개인 데이터이며 API로만 저장
- ChecklistInstance/ChecklistItemState, period_key, period_start/end, generated_at, completed/completed_at
- 프로젝트/재료/캐릭터/AI/RAG 관련 필드: V1.6A schema에 없음
- 소스에 없는 정확한 수량, reset 시각, 보상, 스펙, 추천
- 임의의 API key, 비밀번호, 접속정보, 개인정보

자동/기본 처리:

- DB PK/FK는 importer/DB가 생성한다.
- nested order_no가 없으면 배열 순서(1부터)를 사용한다.
- active 기본값은 true다.
- schedule timezone 기본값은 Asia/Seoul이다.
- source region 기본값은 KR이다.
- Content status 기본값은 active다.
- Step checkable, Reward is_choice 기본값은 false다.
- Evidence verification_status 기본값은 unverified이며 last_verified_at은 생략 시 Content 날짜로 fallback한다. 다만 authoring 시 둘 다 명시하는 것을 권장한다.

## 15. 최소 필수 필드와 선택 필드

| 객체 | importer 최소 필수 | 선택/기본 필드 |
|---|---|---|
| Source | id, url, title, source_type | publisher, published_at, retrieved_at, region(KR) |
| Content | slug, name_ko, category, last_verified_at | subcategory, summary, purpose, party_type, difficulty, status(active), 모든 nested 배열 |
| Requirement | seed_key, kind, description, requirement_level | title, structured_value, order_no, active |
| Section | seed_key, section_type, title, body_markdown | order_no, active |
| Step | seed_key, phase, title, description | order_no, checkable, active |
| Reward | seed_key, name, reward_type | amount/min/max/unit, choice fields, recommendation, notes, order_no, active |
| Schedule | seed_key, rule_type, recurrence_type | weekday, time_local, fixed_datetime, timezone, effective_from/to, notes, active |
| Checklist template | seed_key, name, recurrence_scope | period_rule_seed_key, enabled_default, active, items |
| Checklist item | seed_key, label | order_no, details, reward_hint, active |
| Relation | seed_key, to_content_slug, relation_type | note, order_no, active |
| Evidence claim | seed_key, claim_key, source_ids | entity_type(content), entity_seed_key(content slug), note, verification_status(unverified), last_verified_at(Content 날짜), active |
| UserContentState | seed 입력 없음 | API/사용자 입력 전용 |

날짜는 YYYY-MM-DD, timestamp는 timezone offset을 포함한 ISO 8601, time_local은 HH:MM 형식을 사용한다. nullable 값이 확인되지 않았으면 null 또는 필드 생략을 사용하고 추정값을 넣지 않는다.

Content status canonical 값은 active, deprecated, temporarily_disabled, unknown이다. category, reward_type, source_type, schedule rule_type 일부는 importer가 문자열 enum을 강제하지 않으므로 기존 taxonomy를 재사용하고 새 분류가 필요하면 schema 담당자에게 먼저 제안한다.
