# Tasks — Prompt Bridge V1.5

> V1.8C에서 `project_optimizer`의 Carrack Advance context 수집, Project Detail/전역 Prompt 진입점과 golden snapshot을 완료했다. 아래 미완료 항목은 V1.8C 범위 밖의 기존 V1.5 계획이다.

- [x] Add `features/prompt-bridge` frontend module
- [x] Add `prompt_bridge` backend module
- [x] Define `PromptMode`
- [x] Define `PromptContextBundle`
- [x] Build content context collector
- [x] Build project context collector — V1.8C에서 Project Detail의 stage/material/shortage/inventory와 관련 acquisition context 연결
- [x] Build recurring checklist context collector
- [x] Build user-state collector — Content 상태와 Project stage/inventory 상태·메모 수집
- [x] Build evidence/source collector
- [x] Separate unresolved/conflicting claims
- [x] Add deterministic Markdown renderer
- [ ] Add size budget/truncation policy
- [x] Add `/api/prompt/context`
- [x] Add `/api/prompt/render`
- [x] Add Prompt Bridge drawer/modal
- [ ] Add 5 prompt presets
- [x] Add clipboard copy + fallback
- [x] Add Markdown download
- [x] Add tests proving no outbound network/API call
- [x] Add Carrack Advance golden snapshot
- [ ] Add weekly review golden snapshot
