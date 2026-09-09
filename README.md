# BDO Companion — 검은사막 KR Knowledge Companion

목표: **검증된 검은사막 KR canonical knowledge, Source/Evidence, historical rule changes, deterministic game-domain calculations**를 구조화해 local UI와 향후 AI consumer가 재사용할 수 있게 한다.

기존 React frontend와 local user-state 기능은 계속 지원하지만, 사람이 매일 직접 탐색하는 consumer UI를 제품의 유일한 중심으로 가정하지 않는다. 현재 제품/ownership 방향은 `docs/PRODUCT_DIRECTION.md`를 따른다.

현재 구현 milestone은 **V1.9M — Blood Altar 22–24 Current System Closure**다.

## 현재 baseline

- Source: 183
- Content: 294 (모두 active)
- 지식 역할: FACT 280 / STRATEGY 63 / MEASUREMENT 11
- Project Tracker: Project 1 / Stage 4 / Material 9 / ProjectMaterial 9 / MaterialSource 9
- 테스트: backend 331 passed / frontend 57 passed
- 주요 데이터 영역: Routine, Life Foundation / Deep Packs, Combat Foundation, Grind Spot, Boss / Black Shrine / World Boss, Atoraxxion / Last Gladiius Weekly, Account / Main Quest / Magnus Progression Foundation, Adventure Log Current Catalog, Fairy / Pets Foundation, Guild Boss Current System, Blood Altar 24-stage Current System

## 현재 제품 역할

현재 구현은 세 층으로 본다.

1. **Canonical knowledge** — Content/Requirement/Step/Reward/Relation, Schedule/reset, Source/Evidence, knowledge roles, historical/superseded, Project canonical requirements and deterministic calculations.
2. **Existing local consumers** — Dashboard/Weekly, Content/Life/Project reference, Source/Evidence inspection, local user-state/checklist/inventory/backup, Prompt Bridge preview/copy.
3. **Future consumers** — ChatGPT/MCP/API adapters and domain-scoped external personal-state workflows. 이들은 architecture가 허용한다고 자동 구현하지 않는다.

Frontend는 reference/inspection/admin/debug/local operational UI로 계속 가치가 있다. Consumer-facing polish는 자동 roadmap 우선순위가 아니다.

Personal state는 domain별로 다른 backend가 owner가 될 수 있지만 기존 local state는 유지하며 repository-wide Notion migration을 가정하지 않는다.

## 권장 기술 스택

- Frontend: React + TypeScript + Vite
- Routing: React Router 또는 TanStack Router
- Backend: FastAPI + Pydantic + SQLAlchemy 2
- DB: `DATABASE_URL`로 선택. MySQL 8 권장, SQLite fallback 지원
- Styling: CSS variables + component primitives. 거대한 UI 프레임워크 의존은 피함.
- Tests: Vitest/React Testing Library + Pytest
- V1.5 AI: **외부 API 없음.** local Prompt Bridge가 ChatGPT용 Markdown context를 생성

## 로컬 실행 원칙

- 외부 AI 서비스가 없어도 **이미 저장된 canonical knowledge와 기존 local 기능은 동작**해야 한다.
- 외부 정보 갱신은 별도 "Research/Import" 흐름으로 취급한다.
- 체크리스트 초기화는 데이터 삭제가 아니라 **기간별 checklist instance** 생성으로 처리한다.

## Codex 시작

1. 현재 branch와 작업 트리 상태를 확인한다.
2. `AGENTS.md`, `docs/PRODUCT_DIRECTION.md`, 관련 스펙·handoff 문서를 먼저 읽는다.
3. `docs/specs/001-core/tasks.md`의 현재 완료 상태와 요청된 milestone 범위를 확인한다.

기존 단일 HTML 프로토타입은 `legacy-prototype/`에 보존했다. 새 앱은 이를 그대로 확장하지 말고 데이터 모델부터 재구성한다.


## 현재 범위와 AI 원칙

V1.5 Prompt Bridge is complete and remains a supported deterministic retrieval/context contract.

Current implementation still has no required runtime OpenAI/MCP/Notion dependency.

- OpenAI runtime adapter: not implemented
- MCP adapter: not implemented
- Notion integration in this repository: not implemented
- local LLM: not used
- Prompt Bridge / `PromptContextBundle`: implemented and preserved

Future AI integration, if explicitly selected as a milestone, should normally attach as a thin adapter behind the current structured APIs/domain services/`PromptContextBundle`. The current product-direction change does not authorize an immediate adapter implementation or core rewrite.

앱이 DB 조회, reset 계산, 완료 상태와 source verification을 처리한 뒤 사용자가 ChatGPT에 직접 붙여넣을 prompt를 생성한다. 다섯 가지 preset은 Dashboard 전체 또는 선택한 Content/Project의 현재 상태와 검증 근거를 사용한다. V1.8E에서는 mode/target별 context selector, `full_prompt`/`context_only`, `auto`/`detailed` 크기 모드를 제공하고, 12,000 estimated tokens를 넘는 auto 출력은 관련 콘텐츠·저우선 source·획득처·서술 항목을 완전한 item 단위로 결정적으로 생략한다. V1.9D에서는 verified 지식을 `FACT`/`STRATEGY`/`MEASUREMENT` 역할과 함께 직렬화해 전략이나 측정값을 공식 사실과 구분한다. 기존 API selector 키인 `canonical_facts`는 호환성을 위해 유지한다. 상세 명세는 `docs/specs/002-prompt-bridge/spec.md`를 따른다.

## 현재 구현된 데이터 기반

- FastAPI + SQLAlchemy + Alembic 백엔드
- SQLite 기본 실행과 `DATABASE_URL` 기반 MySQL 전환
- content/source/evidence/schedule/checklist period instance 모델
- requirement/step/reward/section/relation 구조화 지식 모델과 로컬 `UserContentState`
- 안정적인 중첩 `seed_key`, 제자리 갱신, 제거된 seed 행 archive를 지원하는 멱등 import
- claim 단위 evidence, source 발행일/수집일/region, active evidence 집계
- FACT / STRATEGY / MEASUREMENT 지식 역할과 `verified`, `needs_review`, `conflict`, `superseded`, `unverified` evidence 상태
- Prompt Bridge의 콘텐츠 구조 기반 knowledge role 파생, unresolved 역할 보존과 `VERIFIED_KNOWLEDGE` 직렬화
- 충돌·대체 evidence를 현재 사실과 분리하면서 이력을 보존하는 구조
- KST 일일 또는 임의 시각, 설정 가능한 요일의 주간 period와 보상 지급 일정 분리
- Dashboard, Weekly, Content Explorer, Content Detail
- 구조화 상세 payload/화면, 개인 상태·우선순위·메모 저장, 양방향 관련 콘텐츠
- 검증 상태·검증일·공식 출처와 과거 evidence 표시
- 기간별 체크 상태 저장과 과거 기록 보존
- 구조화 지식과 사용자 상태를 포함하는 5개 Prompt Bridge preset: `content_onboarding`, `weekly_review`, `project_optimizer`, `next_action`, `verify_latest`
- Dashboard와 Content/Project Detail, 전역 Prompt 화면에서 대상 의미에 맞는 prompt 생성
- mode/target별 context section selector와 Content/Project related contents
- 전체 프롬프트/컨텍스트 전용 출력, 자동 크기 조절/상세 출력
- unresolved, checklist, 사용자 상태와 Project 핵심 부족량을 우선 보존하는 deterministic item-level compaction
- Markdown 미리보기, clipboard 복사와 실패 시 수동 선택, `.md` 다운로드
- Routine과 해양, Life Foundation / Deep Packs, Combat Foundation, Grind Spot, Boss / Black Shrine / World Boss, Atoraxxion / Last Gladiius Weekly, 현행 길드 우두머리 및 24단계 피의 제단 seed
- 요정 획득·등급·성장·기술과 반려동물 행동·배고픔·교환·5세대 대장 규칙 및 조건부 초기 설정 전략
- Account / Main Quest / Adventure Log / Magnus Progression Foundation seed
- 공식 KR live 책장 기준 Adventure Log current catalog, 대표 해금 조건·총량 보상·Emma 13장 progression과 stale/known-issue 경계
- Project/Stage DAG, Material projection, global inventory와 stage completion 상태
- Carrack Advance backend tracker와 결정적 shortage 계산
- Project 목록·상세 화면, stage 완료/해제, material 재고 저장과 Content 수급처 이동
- 기존 V1.6F-I 및 해양 canonical Content를 재구성한 Life Hub와 10개 생활 분야 상세 화면
- 생활 공통 기반, 분야별 진행도·검증 상태, 노드·일꾼·물류 경제 Content 탐색
- 생활 분야에서 기존 Content Detail·Prompt Bridge와 Carrack Project로 이어지는 탐색 흐름
- 채집·낚시·수렵, 재배·가공, 요리·연금, 항해·물물교환·조련의 목적 선택, 첫 세션 준비와 다음 단계 판단을 다루는 조건부 onboarding/strategy Content
- 공식 FACT와 커뮤니티 STRATEGY를 source/evidence에서 분리하고, 동적 가격·시간당 수익·주간 회전 값은 정적 seed에서 제외
- version 1 JSON envelope로 Content 상태, 전체 checklist history, 재료 재고와 Project 단계 상태 export/import
- numeric DB ID 대신 canonical stable key를 사용하는 portable backup, 사전 validation과 archived identity resolve
- 설정 화면의 로컬 JSON 다운로드, 검증 summary, 기본 merge와 명시적 확인이 필요한 replace 복원
- unknown identity 전체 거부, 단일 transaction restore와 canonical knowledge 불변성

정본 seed 형식은 `docs/data/SEED_FORMAT.md`, V1.8A backend 기반은 `handoff/V18A_PROJECT_TRACKER_FOUNDATION_REPORT.md`, V1.8B frontend 경험은 `handoff/V18B_CARRACK_PROJECT_UI_REPORT.md`, V1.8C Project Prompt Bridge는 `handoff/V18C_PROJECT_PROMPT_BRIDGE_REPORT.md`, V1.8D Prompt Preset Completion은 `handoff/V18D_PROMPT_PRESET_COMPLETION_REPORT.md`, V1.8E Prompt Bridge V1.5 Completion은 `handoff/V18E_PROMPT_BRIDGE_COMPLETION_REPORT.md`, V1.9A Life Hub는 `handoff/V19A_LIFE_HUB_REPORT.md`, V1.9B 사용자 백업·복원은 `handoff/V19B_USER_BACKUP_RESTORE_REPORT.md`, V1.9C 생활 전략 팩은 `handoff/V19C_LIFE_STRATEGY_DEEP1_REPORT.md`, V1.9D 지식 역할 의미론 정리는 `handoff/V19D_PROMPT_KNOWLEDGE_ROLE_REPORT.md`, V1.9E 재배·가공 전략 팩은 `handoff/V19E_LIFE_STRATEGY_DEEP2_REPORT.md`, V1.9F 요리·연금 전략 팩은 `handoff/V19F_LIFE_STRATEGY_DEEP3_REPORT.md`, V1.9G 항해·물물교환 전략 팩은 `handoff/V19G_LIFE_STRATEGY_DEEP4_REPORT.md`, V1.9H 조련 실전 전략 팩은 `handoff/V19H_TRAINING_STRATEGY_DEEP5_REPORT.md`, V1.9I 최후의 글라디우스 주간 콘텐츠는 `handoff/V19I_LAST_GLADIIUS_WEEKLY_REPORT.md`, V1.9J 요정·반려동물 기반은 `handoff/V19J_FAIRY_PETS_FOUNDATION_REPORT.md`, V1.9K 길드 우두머리 현행 시스템은 `handoff/V19K_GUILD_BOSS_CURRENT_REPORT.md`, V1.9L 모험일지 현행 카탈로그는 `handoff/V19L_ADVENTURE_LOG_CURRENT_REPORT.md`, V1.9M 피의 제단 22~24단계 현행화는 `handoff/V19M_BLOOD_ALTAR_CURRENT_REPORT.md`에 기록한다.

## 실행

Python 3.12+와 Node.js 20+가 필요하다. 터미널 두 개에서 백엔드와 프런트엔드를 각각 실행한다.

### 백엔드

```powershell
cd backend
uv sync
uv run alembic upgrade head
uv run python -m app.seed
uv run uvicorn app.main:app --reload
```

API는 `http://127.0.0.1:8000`, health endpoint는 `http://127.0.0.1:8000/api/health`다. 기본 SQLite 파일은 `backend/bdo.db`에 생성된다.

### 프런트엔드

```powershell
cd frontend
npm install
npm run dev
```

브라우저에서 `http://127.0.0.1:5173`을 연다. Vite가 `/api` 요청을 로컬 FastAPI 서버로 전달한다.

## MySQL 전환

MySQL 8 데이터베이스를 먼저 만든 뒤 백엔드 터미널에서 `DATABASE_URL`을 설정한다. URL에 `%` 같은 특수 문자가 들어가면 URL encoding이 필요하다.

```powershell
$env:DATABASE_URL = "mysql+pymysql://USER:PASSWORD@127.0.0.1/bdo_companion?charset=utf8mb4"
uv run alembic upgrade head
uv run python -m app.seed
uv run uvicorn app.main:app --reload
```

앱에는 API key 설정이 없으며 Prompt Bridge는 외부 AI/LLM을 호출하지 않는다.

## 검증 명령과 결과

2026-09-09 기준 backend 테스트는 331 passed, frontend 테스트는 57 passed다.

```powershell
cd backend
uv run pytest
# 331 passed

cd ../frontend
npm run typecheck
npm run lint
npm run test
npm run build
# frontend: 57 passed
```

V1.6A 기반 구조는 `handoff/V16A_SNAPSHOT.md`, V1.7 데이터 팩 결과는 `handoff/V17A_COMBAT_FOUNDATION_REPORT.md`, `handoff/V17B_GRIND_SPOT_REPORT.md`, `handoff/V17C_BOSS_BLACK_SHRINE_REPORT.md`, `handoff/V17D_ACCOUNT_PROGRESSION_REPORT.md`에 기록되어 있다. V1.8A Project Tracker backend foundation은 `handoff/V18A_PROJECT_TRACKER_FOUNDATION_REPORT.md`, V1.8B Carrack Project UI는 `handoff/V18B_CARRACK_PROJECT_UI_REPORT.md`, V1.8C Project Prompt Bridge는 `handoff/V18C_PROJECT_PROMPT_BRIDGE_REPORT.md`, V1.8D Prompt Preset Completion은 `handoff/V18D_PROMPT_PRESET_COMPLETION_REPORT.md`, V1.8E Prompt Bridge V1.5 Completion은 `handoff/V18E_PROMPT_BRIDGE_COMPLETION_REPORT.md`, V1.9A Life Hub Experience는 `handoff/V19A_LIFE_HUB_REPORT.md`, V1.9B User Data Backup & Restore는 `handoff/V19B_USER_BACKUP_RESTORE_REPORT.md`, V1.9C Life Strategy Deep Pack I은 `handoff/V19C_LIFE_STRATEGY_DEEP1_REPORT.md`, V1.9D Prompt Knowledge Role Semantics Closure는 `handoff/V19D_PROMPT_KNOWLEDGE_ROLE_REPORT.md`, V1.9E Life Strategy Deep Pack II는 `handoff/V19E_LIFE_STRATEGY_DEEP2_REPORT.md`, V1.9F Life Strategy Deep Pack III는 `handoff/V19F_LIFE_STRATEGY_DEEP3_REPORT.md`, V1.9G Life Strategy Deep Pack IV는 `handoff/V19G_LIFE_STRATEGY_DEEP4_REPORT.md`, V1.9H Training Practical Strategy Deep Pack은 `handoff/V19H_TRAINING_STRATEGY_DEEP5_REPORT.md`, V1.9I Last Gladiius Weekly Content Closure는 `handoff/V19I_LAST_GLADIIUS_WEEKLY_REPORT.md`, V1.9J Fairy / Pets Foundation은 `handoff/V19J_FAIRY_PETS_FOUNDATION_REPORT.md`, V1.9K Guild Boss Current System은 `handoff/V19K_GUILD_BOSS_CURRENT_REPORT.md`, V1.9L 모험일지 현행 카탈로그는 `handoff/V19L_ADVENTURE_LOG_CURRENT_REPORT.md`, V1.9M 피의 제단 22~24단계 현행화는 `handoff/V19M_BLOOD_ALTAR_CURRENT_REPORT.md`에 기록한다.
