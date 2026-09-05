# V1.8E — Prompt Bridge V1.5 Completion 완료 보고

기준일: 2026-09-05
브랜치: `feature/v1.8e-prompt-controls`
커밋: 이 보고서를 포함하는 V1.8E 최종 커밋의 SHA는 push 완료 보고에 기록한다.

## 완료 범위

- Prompt Bridge가 수집한 정본 context에서 출력 section만 선택하는 selector를 추가했다.
- `full_prompt`와 `context_only`, `auto`와 `detailed` 출력 정책을 추가했다.
- Content relation과 Project의 직접 연결·재료 획득처 Content를 `related_contents`로 제공한다.
- 12,000 estimated token 목표를 넘는 `auto` 출력은 완전한 item 단위로 결정적으로 축소한다.
- unresolved claim, 사용자 상태, checklist, schedule, Project 핵심 stage/material/shortage 값은 우선 보존한다.
- LLM/API, 외부 검색, semantic 요약, seed·schema·migration 변경은 추가하지 않았다.

## Request contract

`PromptRequest`에 `include_sections: list[PromptSection] | None = None`, `output_mode: PromptOutputMode = FULL_PROMPT`, `size_mode: PromptSizeMode = AUTO`를 추가했다.

`include_sections=None`은 V1.8D의 legacy section set을 사용한다. 따라서 기존 caller가 신규 필드를 보내지 않으면 기존 Carrack·weekly Markdown과 동일한 결과를 얻는다. 빈 배열은 아무 context section도 선택하지 않은 명시적 요청이며 renderer는 이를 결정적으로 처리한다.

## PromptSection

- `user_state`
- `requirements`
- `canonical_facts`
- `steps`
- `schedules`
- `rewards`
- `warnings`
- `checklist`
- `related_contents`
- `project_state`
- `open_questions_or_conflicts`
- `sources`

입력 순서와 중복 여부와 관계없이 정해진 section 순서로 직렬화한다. 잘못된 enum 값은 422를 반환한다.

## Mode/target별 frontend 기본 선택

| Mode / target | 기본 section |
| --- | --- |
| `content_onboarding` / Content | user_state, requirements, canonical_facts, steps, schedules, rewards, warnings, checklist, related_contents, open_questions_or_conflicts, sources |
| `project_optimizer` / Project | canonical_facts, schedules, checklist, related_contents, project_state, open_questions_or_conflicts, sources |
| `weekly_review` / global | schedules, checklist |
| `next_action` / global | schedules, checklist |
| `next_action` / Content | content_onboarding 기본 선택 |
| `next_action` / Project | project_optimizer 기본 선택 |
| `verify_latest` / Content | canonical_facts, open_questions_or_conflicts, sources |
| `verify_latest` / Project | canonical_facts, project_state, open_questions_or_conflicts, sources |

질문 수정은 selector를 초기화하지 않는다. mode 또는 Content/Project target이 실제로 바뀔 때만 해당 기본 선택으로 초기화한다.

## Output mode

- `full_prompt`: header, request context, preset goal, response guardrails, 선택한 context, user question을 출력한다.
- `context_only`: header, generated time, region, request page/mode와 선택한 context만 출력한다. preset goal, guardrails, user question은 제외한다.

두 모드 모두 기존 clipboard 복사와 Markdown 다운로드를 지원한다.

## Size mode와 compaction

- `detailed`: 선택한 item을 생략하지 않는다. 12,000 estimated tokens를 넘어도 그대로 반환하고 `over_budget=true`로 알린다.
- `auto`: 최초 출력이 목표 이하면 그대로 반환한다. 초과하면 아래 우선순위로 완전한 item을 제거한다.

축소 우선순위:

1. related contents
2. historical source
3. community/non-official source
4. 현재 visible fact와 직접 연결되지 않은 source
5. Project acquisition detail
6. warnings, rewards, steps, requirements의 tail
7. canonical facts

문자열 중간 절단, 숫자 축약, claim 재작성과 LLM 요약은 사용하지 않는다. 보호 대상 자체만으로 목표를 초과하면 사실을 훼손하지 않고 `over_budget=true`를 유지한다.

## Compaction metadata

`PromptRenderOut`은 기존 `character_count`, `estimated_tokens`, `over_budget`와 함께 다음 값을 반환한다.

- `original_estimated_tokens`: compaction 전 추정치
- `compacted`: 하나 이상의 item이 제거되었는지
- `omitted_counts`: section별 생략 item 수

동일한 bundle, selector와 mode에는 동일한 Markdown과 metadata가 생성된다.

## Related contents

- Content: `ContentDetailOut.related_contents`를 `order_no`, relation key/slug 순으로 안정 정렬한다.
- Project: Project 직접 연결 Content와 ProjectMaterial acquisition source Content를 role과 함께 제공한다.
- 같은 Content는 중복 제거한다.
- 특정 Carrack slug를 hardcode하지 않는다.
- legacy `include_sections=None`에는 과거 출력에 없던 related contents를 자동으로 추가하지 않는다.

## Golden compatibility

- `backend/tests/golden/carrack_project_optimizer.md`: 변경 없음, exact comparison 통과
- `backend/tests/golden/weekly_review.md`: 변경 없음, exact comparison 통과
- 기존 5개 preset과 V1.8C/V1.8D Prompt Bridge 회귀: 통과

## 검증 결과

- backend 전체: `203 passed`
- V1.8C/V1.8D 기존 Prompt Bridge 지정 회귀: `24 passed`
- V1.8E backend 신규 semantic/control tests: `22 passed`
- frontend: `9 files, 39 passed`
- frontend typecheck: 통과
- frontend lint: 통과
- frontend production build: 통과
- no-network: 기존 socket outbound 차단 회귀를 포함한 Prompt Bridge 전체 테스트 통과
- `git diff --check`: 최종 커밋 전 별도 확인

## DB 무결성

- 작업 전 SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 작업 후 SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 동일 여부: 동일
- seed import, migration과 실제 DB 쓰기는 수행하지 않았다.

## Prompt Bridge V1.5 완료 여부

V1.5 명세의 로컬 deterministic Prompt Bridge 범위는 완료했다. `docs/specs/002-prompt-bridge/tasks.md`의 구현 task와 core task를 실제 검증 결과에 맞춰 완료 상태로 갱신했다.

## 잔여 범위

Prompt Bridge V1.5 내부의 미완료 task는 없다. OpenAI/타 LLM API, 로컬 LLM, runtime web search, 자동 전송, semantic/AI summarization, embedding/vector DB는 이번 milestone과 V1.5 범위 밖이며 구현하지 않았다.
