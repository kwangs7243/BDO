# BDO Companion V1.6A Snapshot

작성 기준: 2026-09-03 KST

## 1. Milestone 결과

V1.5 vertical slice를 유지하면서 향후 콘텐츠 대량 확장을 위한 구조화 지식·개인 상태·안전한 seed 동기화 기반을 구현했다. V1.6B 대량 데이터 수집이나 디자인 개선은 포함하지 않는다.

- Alembic head: 20260903_0002
- down revision: 20260902_0001
- runtime LLM/API/network transport: 없음
- DB: SQLite 기본, SQLAlchemy/Alembic 기반 MySQL DDL 지원
- canonical seed: data/seed_sources.json, data/seed_contents.json

## 2. 현재 디렉터리 구조

    backend/
      alembic/versions/       # frozen V1.5 + V1.6A forward migration
      app/                    # FastAPI, models, seed, period/checklist, Prompt Bridge
      tests/                  # backend/migration acceptance tests
    data/
      seed_sources.json
      seed_contents.json
    db/
      schema.sql              # V1.6A reference; models/migrations authoritative
    docs/
      data/SEED_FORMAT.md
      research/
      specs/001-core/
      specs/002-prompt-bridge/
    frontend/
      src/                    # React UI, API types, component tests
    handoff/
      V16A_SNAPSHOT.md
    prompts/
    AGENTS.md
    ARCHITECTURE.md
    README.md

backend/bdo.db, .venv, node_modules, dist, cache는 source of truth가 아니다.

## 3. Migration revision과 호환성

20260903_0002가 기존 테이블에 추가하는 필드:

- schedule_rule: seed_key, fixed_datetime, active, scoped unique
- evidence: seed_key, active, seed key unique
- checklist_template: seed_key, period_rule_id, active, scoped unique/FK
- checklist_template_item: seed_key, active, scoped unique

새 테이블:

- content_requirement
- content_step
- reward
- content_section
- content_relation
- user_content_state

초기 revision은 동적 current metadata가 아니라 당시 V1.5 DDL로 동결했다. 따라서 새 DB도 0001 → 0002를 실제로 거친다. revision은 0001이지만 V1.6A 빈 테이블 일부가 먼저 만들어진 DB도 테이블을 재생성하지 않고 migration을 완료하도록 방어한다.

실제 backend/bdo.db 원본은 수정하지 않았다. revision 20260902_0001, checklist state/instance 각 4개인 원본을 임시 복사해 upgrade와 seed import를 수행했고, 결과는 revision 20260903_0002, state 4개, instance 4개로 이력이 보존됐다.

## 4. 데이터 모델

- Content 1:N ContentRequirement, ContentStep, Reward, ContentSection, ScheduleRule, ChecklistTemplate
- ContentRelation은 from/to 두 FK로 상세 API에서 양방향 조회
- Content 1:0..1 UserContentState; 인증/사용자 테이블 없음
- ChecklistTemplate 1:N item, 1:N period instance, instance 1:N historical state
- ChecklistTemplate.period_rule_id → reset-like ScheduleRule
- Evidence는 entity_type + entity_id(seed_key) + claim_key로 구조화 행/필드를 지칭하고 Source를 참조
- ContentRequirement.structured_value는 DB-portable SQLAlchemy JSON

정확한 필드와 enum은 backend/app/models.py, backend/app/schemas.py, docs/specs/001-core/data-model.md를 참고한다.

## 5. API 변경

새 endpoint:

- GET /api/contents/{slug}/state: 저장 행이 없으면 not_started 기본 상태 반환
- PUT /api/contents/{slug}/state: state/priority/note 생성 또는 갱신

확장 endpoint:

- GET /api/contents/{slug}: requirements, sections, phase/order 가능한 steps, schedules, rewards, 현재 checklist, 양방향 related contents, user state, current/historical evidence/source 포함

기존 endpoint:

- GET /api/health
- GET /api/contents
- GET /api/checklists/current?scope=daily|weekly
- PATCH /api/checklists/states/{state_id}
- GET /api/dashboard
- POST /api/prompt/context
- POST /api/prompt/render

상세 조회는 관계를 selectinload하고 evidence를 묶어 조회한다. 출력은 Pydantic typed response와 명시적 정렬로 deterministic하다.

## 6. Seed 동기화 의미

- content는 slug, nested row는 안정적인 seed_key로 식별한다.
- 재실행하면 text/details/schedule/reward hint/source/evidence metadata를 같은 DB ID에서 갱신한다.
- 과거 V1.5 schedule/template/item의 nullable key는 규칙/이름/순서로 한 번 대응해 안정 key를 부여한다.
- canonical seed에서 빠진 nested row는 active=false로 archive하며 삭제하지 않는다.
- archive된 checklist item의 과거 ChecklistItemState는 유지되고 현재 checklist에서만 숨긴다.
- Evidence key는 {claim seed key}::{source id}다.
- active evidence는 active=true, status != superseded, superseded_by IS NULL을 모두 만족한다. 과거 근거는 노출하되 현재 content verification을 낮추지 않는다.
- 형식과 예제: docs/data/SEED_FORMAT.md

## 7. Recurrence/checklist 의미

- 기존 period instance/history 모델을 유지하며 일괄 checkbox reset은 하지 않는다.
- period_rule_id가 있으면 해당 schedule의 recurrence/weekday/time을 사용한다.
- 허용 driver: quest_reset, attempt_reset
- fallback: daily 00:00 KST, weekly 목요일 00:00 KST
- 지원 계산: configurable daily local time, configurable weekly weekday/local time
- reward_payout, record_cutoff은 표시용이며 checklist reset driver가 아니다.
- fixed datetime/event 일정은 상세 schedule에 표시할 수 있지만 V1.6A checklist period engine으로 확장하지 않았다.

## 8. Golden seed 범위

전체 content 7개는 유지했다.

- weekly-quest-framework: reset schedule + period-bound checklist + claim evidence
- blood-altar: party requirement, repeat step, nullable reward, why/warning, Sunday payout, checklist, relation, claim evidence
- pit-of-undying: stable checklist/evidence migration
- garmoth: attempt reset이 checklist period를 소유
- vell: 기존 summary/evidence 유지
- life-common-gear: overview/preparation prose와 claim evidence. 구체 장비 requirement는 저장소에 검증 사실이 없어 추가하지 않음
- carrack-advance: 기존 검증 사실 범위의 purpose, starting-ship requirement, preparation step, prose, evidence. 재료 수량은 추가하지 않음

활성 seed 합계: requirements 2, steps 2, rewards 1, sections 5, evidence 23. schema/UI 검증용 golden set이며 콘텐츠 완성도를 뜻하지 않는다.

## 9. Content Detail UI

기존 화면 구조를 재디자인하지 않고 다음 순서로 조건부 렌더링한다.

1. 한눈에 보기/개인 상태 편집
2. 왜 하는가
3. 선행조건
4. 준비
5. 시작 방법
6. 최초 진행
7. 반복 진행/current checklist
8. 일정/초기화
9. 보상/선택 추천
10. 실수/주의
11. 관련 콘텐츠
12. 근거/검증

state selector, priority, note, save로 구성한 작은 편집기를 추가했다. 데이터가 없는 섹션은 숨기고 한 줄 missing-data 안내만 유지한다.

## 10. Prompt Bridge 범위

- mode는 content_onboarding, weekly_review 두 개만 유지
- onboarding에 requirements, steps, rewards/recommendation, schedules, personal state/note, warnings, checklist, claim source metadata 포함
- verified와 needs_review/conflict/unverified fact를 분리
- active/historical evidence를 구분
- 동일 입력은 안정적인 정렬의 Markdown 생성
- 외부 LLM/API/network 호출 없음

next_action, project_optimizer, verify_latest는 prompt spec의 장기 target이지만 V1.6A 구현 mode가 아니다.

## 11. 알려진 부족/연기 항목

- 대량 검은사막 콘텐츠 조사·입력
- project/material/shortage 및 project_optimizer
- AI/API/RAG, embedding, vector DB
- global search index
- character 관리와 생활 숙련도 계산기
- crawler/scraper
- 인증/다중 사용자
- 시각 디자인 전면 개선
- full RRULE checklist engine
- 과거 checklist 조회용 별도 UI/API; DB history는 보존됨
- life-common-gear의 구체 장비 requirement와 carrack-advance 재료 수량: 검증된 근거 추가 조사 필요

## 12. V1.6B 대량 연구/import에서 먼저 건드릴 파일

일반 콘텐츠 추가는 다음 파일만 우선 사용한다.

1. docs/research/SOURCE_POLICY.md — 검증/우선순위 규칙
2. docs/research/SEED_CATALOG.md — 조사 범위와 상태
3. data/seed_sources.json — 신규 공식 출처 metadata
4. data/seed_contents.json — 콘텐츠 구조와 claim evidence

형식은 docs/data/SEED_FORMAT.md, 공식 URL map은 docs/research/OFFICIAL_SOURCE_MAP.md를 사용한다. 새 enum/관계/필드가 꼭 필요할 때만 아래 구현 경로를 함께 바꾼다.

    backend/app/models.py
    backend/alembic/versions/<new_revision>.py
    backend/app/seed.py
    backend/app/schemas.py
    backend/app/content.py
    frontend/src/types.ts
    frontend/src/features/content/ContentDetailPage.tsx
    backend/tests/ + frontend/src/**/*.test.tsx

기존 20260903_0002를 대량 데이터 작업 때문에 수정하지 않는다. schema 변화는 새 migration으로 추가한다.

## 13. 최종 검증 결과

    Backend pytest:                 28 passed
    Frontend TypeScript typecheck: passed
    Frontend ESLint:               passed
    Frontend Vitest:               3 files / 4 tests passed
    Frontend production build:     passed (34 modules)
    SQLite clean V1.5 migration:   pytest acceptance passed
    SQLite actual DB temp copy:    0001 → 0002, 4 states/4 instances preserved
    SQLite migrated seed import:   passed, 4 historical states preserved
    MySQL offline DDL:             generated, 0001 + 0002 / new tables / period FK present

주요 acceptance coverage:

- seed idempotence와 nested row ID 유지 갱신
- checklist text 변경/제거 후 history 보존
- evidence/source metadata 재수입 갱신
- superseded evidence current aggregate 제외
- 구조화 상세/양방향 relation serialization
- user content state create/update
- KST daily, 목요일 weekly, 다른 요일+시각, 월跨/연跨
- reward payout 비-reset
- 구조화 onboarding prompt와 network 미호출
- 상세 섹션 순서/빈 섹션 숨김/개인 상태 편집

