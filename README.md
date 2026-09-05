# BDO Companion — 검은사막 개인 운영체제

목표: 단순 숙제 체크리스트가 아니라, **검은사막 콘텐츠 위키 + 진행도 + 반복 숙제 + 프로젝트/재료 트래커 + 근거 관리**를 하나로 묶는 로컬 웹앱.

현재 구현 milestone은 **V1.8D — Prompt Preset Completion**이다.

## 현재 baseline

- Source: 145
- Content: 259 (모두 active)
- 지식 역할: FACT 193 / STRATEGY 17 / MEASUREMENT 11
- Project Tracker: Project 1 / Stage 4 / Material 9 / ProjectMaterial 9 / MaterialSource 9
- 테스트: backend 181 passed / frontend 31 passed
- 주요 데이터 영역: Routine, Life Foundation / Deep Packs, Combat Foundation, Grind Spot, Boss / Black Shrine / World Boss, Account / Main Quest / Adventure Log / Magnus Progression Foundation

## 제품 목표 사용 시나리오

아래 목록은 장기 제품 목표다. 현재 구현된 시나리오는 대시보드·주간 체크리스트, Content 상세·근거 확인, Prompt Bridge와 Project 목록·상세·재고·단계 상태를 포함한 부족량 추적이다. JSON import/export는 아직 구현되지 않았다.

1. "수렵 한번 해볼까?" → 수렵 페이지 진입 → 왜 하는지 / 준비물 / 장비 / 시작 루트 / 체크리스트 / 추천 다음 단계 확인.
2. "이번 주 뭐 안 했지?" → 주간 대시보드 → 초기화 규칙별로 남은 콘텐츠 확인.
3. "중범선 언제 완성하지?" → 프로젝트 페이지 → 현재 재고 입력 → 부족량 / 일퀘·주간·물교 수급처 / 다음 행동 확인.
4. "이 정보 최신 맞아?" → 모든 핵심 규칙에 출처와 마지막 검증일 표시.
5. "이 상태를 ChatGPT에 물어보고 싶어" → 현재 진행도/부족량/검증 근거를 자동 선별한 prompt를 만들어 복사.

## 권장 기술 스택

- Frontend: React + TypeScript + Vite
- Routing: React Router 또는 TanStack Router
- Backend: FastAPI + Pydantic + SQLAlchemy 2
- DB: `DATABASE_URL`로 선택. MySQL 8 권장, SQLite fallback 지원
- Styling: CSS variables + component primitives. 거대한 UI 프레임워크 의존은 피함.
- Tests: Vitest/React Testing Library + Pytest
- V1.5 AI: **외부 API 없음.** local Prompt Bridge가 ChatGPT용 Markdown context를 생성

## 로컬 실행 원칙

- 인터넷 연결 없이도 **이미 저장된 데이터와 진행도는 100% 동작**해야 한다.
- 외부 정보 갱신은 별도 "Research/Import" 흐름으로 취급한다.
- 체크리스트 초기화는 데이터 삭제가 아니라 **기간별 checklist instance** 생성으로 처리한다.

## Codex 시작

1. 현재 branch와 작업 트리 상태를 확인한다.
2. `AGENTS.md`와 관련 스펙·handoff 문서를 먼저 읽는다.
3. `docs/specs/001-core/tasks.md`의 현재 완료 상태와 요청된 milestone 범위를 확인한다.

기존 단일 HTML 프로토타입은 `legacy-prototype/`에 보존했다. 새 앱은 이를 그대로 확장하지 말고 데이터 모델부터 재구성한다.


## 현재 범위와 AI 원칙

현재 V1.8D까지 비용이 발생하는 AI 연동 없이 V1.5의 로컬 Prompt Bridge 원칙을 유지한다.

- OpenAI API: 사용 안 함
- 타사 LLM API: 사용 안 함
- 로컬 LLM: 사용 안 함
- Fine-tuning: 사용 안 함
- Prompt Bridge: 사용

앱이 DB 조회, reset 계산, 완료 상태와 source verification을 처리한 뒤 사용자가 ChatGPT에 직접 붙여넣을 prompt를 생성한다. V1.8D에서는 기존 `content_onboarding`, `weekly_review`, `project_optimizer`에 `next_action`, `verify_latest`를 더해 다섯 가지 preset을 제공한다. `next_action`은 Dashboard 전체 또는 선택한 Content/Project의 현재 상태를 사용하고, `verify_latest`는 선택한 대상의 verified 기준 정보와 미검증·충돌 claim을 분리해 전달한다. 상세 명세는 `docs/specs/002-prompt-bridge/spec.md`를 따른다.

## 현재 구현된 데이터 기반

- FastAPI + SQLAlchemy + Alembic 백엔드
- SQLite 기본 실행과 `DATABASE_URL` 기반 MySQL 전환
- content/source/evidence/schedule/checklist period instance 모델
- requirement/step/reward/section/relation 구조화 지식 모델과 로컬 `UserContentState`
- 안정적인 중첩 `seed_key`, 제자리 갱신, 제거된 seed 행 archive를 지원하는 멱등 import
- claim 단위 evidence, source 발행일/수집일/region, active evidence 집계
- FACT / STRATEGY / MEASUREMENT 지식 역할과 `verified`, `needs_review`, `conflict`, `superseded`, `unverified` evidence 상태
- 충돌·대체 evidence를 현재 사실과 분리하면서 이력을 보존하는 구조
- KST 일일 또는 임의 시각, 설정 가능한 요일의 주간 period와 보상 지급 일정 분리
- Dashboard, Weekly, Content Explorer, Content Detail
- 구조화 상세 payload/화면, 개인 상태·우선순위·메모 저장, 양방향 관련 콘텐츠
- 검증 상태·검증일·공식 출처와 과거 evidence 표시
- 기간별 체크 상태 저장과 과거 기록 보존
- 구조화 지식과 사용자 상태를 포함하는 5개 Prompt Bridge preset: `content_onboarding`, `weekly_review`, `project_optimizer`, `next_action`, `verify_latest`
- Dashboard와 Content/Project Detail, 전역 Prompt 화면에서 대상 의미에 맞는 prompt 생성
- Markdown 미리보기, clipboard 복사와 실패 시 수동 선택, `.md` 다운로드
- Routine과 해양, Life Foundation / Deep Packs, Combat Foundation, Grind Spot, Boss / Black Shrine / World Boss seed
- Account / Main Quest / Adventure Log / Magnus Progression Foundation seed
- Project/Stage DAG, Material projection, global inventory와 stage completion 상태
- Carrack Advance backend tracker와 결정적 shortage 계산
- Project 목록·상세 화면, stage 완료/해제, material 재고 저장과 Content 수급처 이동

정본 seed 형식은 `docs/data/SEED_FORMAT.md`, V1.8A backend 기반은 `handoff/V18A_PROJECT_TRACKER_FOUNDATION_REPORT.md`, V1.8B frontend 경험은 `handoff/V18B_CARRACK_PROJECT_UI_REPORT.md`, V1.8C Project Prompt Bridge는 `handoff/V18C_PROJECT_PROMPT_BRIDGE_REPORT.md`, V1.8D Prompt Preset Completion은 `handoff/V18D_PROMPT_PRESET_COMPLETION_REPORT.md`에 기록한다.

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

2026-09-05 기준 backend 테스트는 181 passed, frontend 테스트는 31 passed다.

```powershell
cd backend
uv run pytest
# 181 passed

cd ../frontend
npm run typecheck
npm run lint
npm run test
npm run build
# frontend: 31 passed
```

V1.6A 기반 구조는 `handoff/V16A_SNAPSHOT.md`, V1.7 데이터 팩 결과는 `handoff/V17A_COMBAT_FOUNDATION_REPORT.md`, `handoff/V17B_GRIND_SPOT_REPORT.md`, `handoff/V17C_BOSS_BLACK_SHRINE_REPORT.md`, `handoff/V17D_ACCOUNT_PROGRESSION_REPORT.md`에 기록되어 있다. V1.8A Project Tracker backend foundation은 `handoff/V18A_PROJECT_TRACKER_FOUNDATION_REPORT.md`, V1.8B Carrack Project UI는 `handoff/V18B_CARRACK_PROJECT_UI_REPORT.md`, V1.8C Project Prompt Bridge는 `handoff/V18C_PROJECT_PROMPT_BRIDGE_REPORT.md`, V1.8D Prompt Preset Completion은 `handoff/V18D_PROMPT_PRESET_COMPLETION_REPORT.md`에 기록한다.
