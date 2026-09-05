# V1.8D — Prompt Preset Completion 완료 보고

기준일: 2026-09-05
브랜치: `feature/v1.8d-prompt-presets`
커밋: 이 보고서를 포함하는 최종 커밋의 SHA는 push 완료 보고에 기록

## 완료 범위

- 기존 `content_onboarding`, `weekly_review`, `project_optimizer`에 `next_action`, `verify_latest`를 추가해 PromptMode 5개를 완성했다.
- 두 신규 mode는 기존 Content/Project context collector를 재사용한다.
- Content collector는 기존 onboarding의 구조화 지식, 사용자 상태, checklist, schedule, evidence 출력을 바꾸지 않고 공용 함수로 분리했다.
- Project collector와 `get_project_detail`의 stage/material/inventory/shortage 계산 경로를 그대로 사용한다.
- 외부 web search, LLM/API 호출, 자동 전송을 추가하지 않았다.
- seed, schema, migration과 실제 `backend/bdo.db`를 변경하지 않았다.

## Mode 계약

| Mode | 대상 계약 | Context |
| --- | --- | --- |
| `content_onboarding` | `content_slug` 필수 | Content 구조화 지식과 사용자 상태 |
| `weekly_review` | target 없음 | 현재 weekly checklist와 목요일 00:00 KST 경계 |
| `project_optimizer` | `project_slug` 필수 | Project stage/material/shortage와 관련 획득처 |
| `next_action` | target 없음 또는 Content/Project 중 하나 | Dashboard daily+weekly 또는 선택 대상 context |
| `verify_latest` | Content/Project 중 정확히 하나 | verified 기준 정보, unresolved/conflict, evidence/source |

## next_action 의미

- target 없음: page는 `dashboard`이며 current daily와 weekly checklist를 함께 포함한다.
- 전역 checklist label에 `[daily]`, `[weekly]` scope를 붙여 같은 출력 안에서 구분한다.
- daily는 매일 00:00 KST, weekly는 목요일 00:00 KST 기간 의미를 기존 주기 엔진으로 계산한다.
- 완료와 미완료 상태는 현재 `ChecklistItemState`를 그대로 반영한다.
- Content target은 onboarding과 같은 Content collector를 사용한다.
- Project target은 V1.8C Project collector를 사용하며 shortage를 재계산하지 않는다.
- Content와 Project target을 동시에 보내면 422를 반환한다.

## verify_latest 의미

- `content_slug` 또는 `project_slug` 중 정확히 하나가 필요하다.
- target 없음 또는 두 target 동시 입력은 422다.
- 존재하지 않는 Content/Project는 각각 명확한 404를 반환한다.
- verified claim은 `CANONICAL_FACTS`, needs_review/conflict/unverified claim은 `OPEN_QUESTIONS_OR_CONFLICTS`에 둔다.
- Project Requirement lineage의 `structured_value` 또는 `description` evidence 선택은 V1.8C 의미를 유지한다.
- unresolved claim이 없으면 새 사실이나 충돌을 만들지 않고 “현재 저장된 정보에서 재검증이 필요한 항목이 없다.”고 결정적으로 표시한다.

## UI 진입점

- Dashboard: `지금 할 일 ChatGPT에 물어보기` — target 없는 global `next_action`
- Content Detail: 기존 onboarding 유지 + `최신 정보 검증 프롬프트`
- Project Detail: 기존 optimizer 유지 + `최신 정보 검증 프롬프트`
- 전역 Prompt 화면: 5개 preset 모두 제공
- Next Action selector: 전체 대시보드 / Content / Project
- Verify Latest selector: Content / Project
- Content와 Project 목록은 각각 `GET /api/contents`, `GET /api/projects` 응답을 사용하며 특정 slug를 하드코딩하지 않는다.
- 신규 placeholder:
  - next_action: `지금 내 상태에서 무엇부터 하면 돼?`
  - verify_latest: `미검증 항목을 최신 KR 공식 자료로 확인해줘`

## Validation과 회귀

- backend 전체: `181 passed`
- V1.8C Prompt Bridge + V1.8D 지정 테스트: `24 passed`
- frontend: `9 files, 31 passed`
- frontend typecheck: 통과
- frontend lint: 통과
- frontend production build: 통과
- no-network: socket outbound connect를 차단한 상태에서 다섯 target 조합의 신규 mode 렌더링 통과

### Weekly golden

- 파일: `backend/tests/golden/weekly_review.md`
- 고정 시각: `2026-09-02T23:00:00+09:00`
- mode/goal/guardrails, 목요일 reset 의미, 완료 `[x]`와 미완료 `[ ]`, 사용자 질문을 포함한 전체 Markdown exact compare를 통과했다.

### Carrack 회귀

- `backend/tests/golden/carrack_project_optimizer.md`는 변경하지 않았다.
- Carrack 4 stages / 9 materials, inventory note, backend shortage, checklist/schedule/evidence와 Requirement claim resolution 회귀를 포함한 기존 테스트가 통과했다.

## DB 무결성

- 작업 전 SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 작업 후 SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 동일 여부: 동일

## 남은 Prompt Bridge 범위

- size budget 초과 시 automatic truncation/compaction 정책
- context selector 전체 UI
- context-only/full-prompt toggle

위 항목은 V1.8D 완료로 처리하지 않았고, `docs/specs/002-prompt-bridge/tasks.md`의 size budget/truncation 항목도 미완료로 유지했다.
