# Codex Follow-up — Complete V1.5 Prompt Bridge

현재 구현을 먼저 읽고 테스트를 실행하라. 그 다음 `docs/specs/002-prompt-bridge/`를 source of truth로 사용해 아직 빠진 V1.5 Prompt Bridge 항목만 구현하라.

중요:
- 외부 LLM/API를 호출하지 않는다.
- OpenAI API key/SDK를 추가하지 않는다.
- DB가 이미 계산할 수 있는 shortage/reset/completion을 prompt에서 AI에게 계산시키지 않는다.
- context 수집과 Markdown rendering은 deterministic해야 한다.
- verified와 needs_review/conflict를 분리한다.
- 현재 페이지 관련 정보만 기본 포함하고, 관련 콘텐츠는 size budget을 넘기지 않게 제한한다.

완료 후:
1. 테스트 결과
2. 구현한 endpoint/UI
3. 생성된 예시 prompt 2개
4. 남은 V2 후보(구현하지 말 것)
를 README 또는 작업 결과에 정리하라.
