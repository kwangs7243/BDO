# BDO Companion Agent Map

이 프로젝트는 검은사막 개인 위키/숙제/진행도 앱이다. **추측으로 게임 데이터를 만들지 않는다.**

## 먼저 읽을 문서

1. `docs/CONSTITUTION.md` — 절대 규칙
2. `docs/specs/001-core/spec.md` — 제품 요구사항
3. `docs/specs/001-core/data-model.md` — 데이터 모델
4. `docs/research/SOURCE_POLICY.md` — 검은사막 정보 검증 규칙
5. `docs/research/SEED_CATALOG.md` — 초기 콘텐츠 범위
6. `docs/specs/001-core/ui-map.md` — 화면 구조
7. `docs/specs/001-core/tasks.md` — 구현 순서
8. `docs/specs/002-prompt-bridge/spec.md` — V1.5 ChatGPT 프롬프트 브리지

## 개발 원칙

- 한국 서버 / Asia-Seoul 기준.
- 반복 콘텐츠의 `재수주 초기화`, `기록 집계`, `보상 지급`, `출현 스케줄`을 하나의 reset 필드로 뭉치지 않는다.
- 소스가 없는 게임 규칙은 `unverified`로 저장하고 UI에서 확정 정보처럼 노출하지 않는다.
- 핵심 규칙 변경 시 source/evidence record와 last_verified_at을 함께 갱신한다.
- 과거 체크 기록은 삭제하지 않는다.
- 특정 날짜의 상태를 재현할 수 있어야 한다.
- DB는 MySQL/SQLite 모두 지원하도록 SQLAlchemy dialect-independent하게 작성한다.
- 기존 `legacy-prototype`은 참고만 하고 신규 구조의 source of truth로 사용하지 않는다.
- **V1.5에서는 어떤 LLM/API도 런타임 호출하지 않는다.** AI 기능은 로컬 데이터로 ChatGPT용 prompt/context bundle을 생성하는 `Prompt Bridge`까지만 구현한다.
- API key 입력/저장, OpenAI SDK, 로컬 LLM, embedding API는 V2 이전에 추가하지 않는다.

## 테스트 필수 항목

- KST 일일 00:00 경계
- 일반 주간 목요일 00:00 경계
- 일요일 00:00 보상 규칙이 있는 콘텐츠
- 월跨/연跨(12/31→1/1) 기간 키
- source가 stale/superseded일 때 표시
- project material shortage 계산
- checklist history 보존
- Prompt Bridge가 네트워크 호출 없이 deterministic Markdown을 생성하는지
- 완료/미완료 체크 상태와 source verification 상태가 prompt context에 정확히 반영되는지
