# Codex Bootstrap Prompt — V1.5 Local-first

이 저장소의 `AGENTS.md`를 먼저 읽고, AGENTS.md가 가리키는 문서 중 아래를 반드시 읽어라.

1. `docs/CONSTITUTION.md`
2. `docs/specs/001-core/spec.md`
3. `docs/specs/001-core/data-model.md`
4. `docs/specs/001-core/ui-map.md`
5. `docs/specs/001-core/tasks.md`
6. `docs/specs/002-prompt-bridge/spec.md`
7. `docs/specs/002-prompt-bridge/prompt-presets.md`
8. `docs/research/SOURCE_POLICY.md`

## Product boundary

목표는 BDO Companion V1.5다.

- React + TypeScript + Vite frontend
- FastAPI + SQLAlchemy backend
- SQLite 기본, MySQL `DATABASE_URL` 호환
- local-first
- Asia/Seoul timezone
- checklist는 period instance 방식
- source/evidence 추적
- **LLM/API 호출 금지**
- **API key UI/환경변수 금지**
- AI 관련 기능은 `Prompt Bridge`: 로컬 DB에서 context를 모아 ChatGPT에 붙여넣을 Markdown prompt를 생성하는 것까지만

## 이번 Codex 작업

한 번에 전체 게임 데이터를 만들지 말고 **작동하는 vertical slice**를 구현하라.

### Part A — Foundation
- `frontend/`, `backend/` 생성
- lint/typecheck/test 실행 경로 구성
- SQLAlchemy + Alembic
- SQLite 기본 실행
- MySQL URL 호환
- `/api/health`
- source/content/schedule/checklist 최소 schema
- Asia/Seoul daily/Thursday-weekly period calculator + tests
- seed importer

### Part B — Knowledge slice
- Dashboard
- Content explorer
- Content detail
- source badge / last verified / verification state
- current checklist 조회 및 상태 저장

### Part C — Minimal Prompt Bridge
`docs/specs/002-prompt-bridge/` 계약을 기반으로 최소 vertical slice를 추가한다.

- `PromptContextBundle` schema
- `content_onboarding` preset
- `weekly_review` preset
- current content + schedules + checklist state + sources context collector
- deterministic Markdown renderer
- Content Detail와 Weekly 화면의 `ChatGPT에 물어보기` action
- preview + clipboard copy + `.md` download
- no-network test

`project_optimizer`는 project/material schema가 아직 구현되지 않았다면 stub을 만들지 말고 다음 milestone로 남긴다.

## 절대 하지 말 것
- legacy prototype 리팩터링으로 시작
- 웹에서 임의 게임 데이터 scraping
- 검증되지 않은 게임 규칙 seed 생성
- OpenAI SDK / LangChain / LlamaIndex / Ollama 등 LLM runtime dependency 추가
- embedding/vector DB를 미래 대비라는 이유로 선구현
- checkbox 전체 false UPDATE 방식 reset
- 거대한 generic repository/service abstraction 생성

## 완료 조건
1. frontend test/typecheck 통과
2. `pytest` 통과
3. SQLite에서 seed import 후 앱 부팅
4. current daily/weekly period가 KST 기준으로 정확
5. content detail에 source/검증일 노출
6. checklist 상태 변경 후 새로고침해도 유지
7. Prompt Bridge가 outbound network 없이 Markdown prompt 생성
8. 생성 prompt에서 verified 사실과 unresolved 사실이 구분됨
9. 실행 방법, MySQL 전환 방법, 테스트 결과를 README에 갱신

구현 중 spec 불일치가 발견되면 임의로 사실을 만들지 말고 `docs/DECISIONS.md`에 문제/선택/근거를 기록하고 보수적으로 구현하라.
