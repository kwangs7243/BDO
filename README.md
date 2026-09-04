# BDO Companion — 검은사막 개인 운영체제

목표: 단순 숙제 체크리스트가 아니라, **검은사막 콘텐츠 위키 + 진행도 + 반복 숙제 + 프로젝트/재료 트래커 + 근거 관리**를 하나로 묶는 로컬 웹앱.

## 핵심 사용 시나리오

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

1. 현재 폴더를 Git 저장소로 만든다.
2. Codex에서 `/init`을 실행해도 되지만, 이 패키지의 `AGENTS.md`를 우선 유지한다.
3. `prompts/CODEX_BOOTSTRAP.md`의 지시를 첫 작업으로 준다.
4. 실제 Spec Kit를 쓰고 싶다면 최신 Spec Kit를 설치한 뒤 이 문서들을 specification source로 가져간다.

기존 단일 HTML 프로토타입은 `legacy-prototype/`에 보존했다. 새 앱은 이를 그대로 확장하지 말고 데이터 모델부터 재구성한다.


## V1.6A 범위

V1.6A도 비용이 발생하는 AI 연동 없이 V1.5 구조를 유지한다. 이번 milestone은 대량 콘텐츠 입력 전의 데이터 기반 작업이다.

- OpenAI API: 사용 안 함
- 타사 LLM API: 사용 안 함
- 로컬 LLM: 사용 안 함
- Fine-tuning: 사용 안 함
- Prompt Bridge: 사용

앱이 DB 조회, reset 계산, 완료 상태와 source verification을 처리한 뒤 사용자가 ChatGPT에 직접 붙여넣을 prompt를 생성한다. project/material 계산은 관련 모델과 함께 후속 milestone로 남겼다. 상세 명세는 `docs/specs/002-prompt-bridge/spec.md`를 따른다.

## 현재 구현된 V1.6A 데이터 기반

- FastAPI + SQLAlchemy + Alembic 백엔드
- SQLite 기본 실행과 `DATABASE_URL` 기반 MySQL 전환
- content/source/evidence/schedule/checklist period instance 모델
- requirement/step/reward/section/relation 구조화 지식 모델과 로컬 `UserContentState`
- 안정적인 중첩 `seed_key`, 제자리 갱신, 제거된 seed 행 archive를 지원하는 멱등 import
- claim 단위 evidence, source 발행일/수집일/region, active evidence 집계
- KST 일일 또는 임의 시각, 설정 가능한 요일의 주간 period와 보상 지급 일정 분리
- Dashboard, Weekly, Content Explorer, Content Detail
- 구조화 상세 payload/화면, 개인 상태·우선순위·메모 저장, 양방향 관련 콘텐츠
- 검증 상태·검증일·공식 출처와 과거 evidence 표시
- 기간별 체크 상태 저장과 과거 기록 보존
- 구조화 지식을 포함하는 `content_onboarding`, `weekly_review` Prompt Bridge
- Markdown 미리보기, clipboard 복사와 실패 시 수동 선택, `.md` 다운로드

정본 seed 형식은 `docs/data/SEED_FORMAT.md`, 구현 snapshot은 `handoff/V16A_SNAPSHOT.md`에 기록한다. 프로젝트/재료 스키마가 없는 이번 milestone에서는 `project_optimizer`를 만들지 않았다.

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

2026-09-03 기준 아래 검증을 통과했다.

```powershell
cd backend
uv run pytest
# 28 passed

cd ../frontend
npm run typecheck
npm run lint
npm run test
# 4 passed
npm run build
```

추가로 V1.5 SQLite schema에서 revision `20260903_0002`로 checklist history를 보존하는 forward migration을 테스트하고 MySQL migration SQL을 offline 생성·검토한다. 정확한 최종 결과는 `handoff/V16A_SNAPSHOT.md`에 기록한다.
