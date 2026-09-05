# Tasks — Prompt Bridge V1.5

> V1.8E에서 context selector, output mode와 deterministic size compaction까지 구현해 Prompt Bridge V1.5 범위를 완료했다.

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
- [x] Add context selector
- [x] Add context-only/full-prompt output
- [x] Add size budget/truncation policy
- [x] Add `/api/prompt/context`
- [x] Add `/api/prompt/render`
- [x] Add Prompt Bridge drawer/modal
- [x] Add 5 prompt presets
- [x] Add clipboard copy + fallback
- [x] Add Markdown download
- [x] Add tests proving no outbound network/API call
- [x] Add Carrack Advance golden snapshot
- [x] Add weekly review golden snapshot
