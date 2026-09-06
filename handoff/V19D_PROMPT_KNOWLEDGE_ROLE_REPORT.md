# V1.9D — Prompt Knowledge Role Semantics Closure 완료 보고

## Git 기준

- 기준일: 2026-09-06
- Source of Truth: `main` @ `825862e46db15bc6c2c78974733db518ac21950e`
- 작업 branch: `feature/v1.9d-prompt-knowledge-role`
- 구현 commit: 이 보고서를 포함하는 V1.9D commit

## 완료 범위

Prompt Bridge가 evidence의 검증 상태와 지식의 의미 역할을 서로 다른 축으로 표현하도록 정리했다.

- `PromptKnowledgeRole`: `fact`, `strategy`, `measurement`
- `PromptFact.knowledge_role` additive 응답 필드
- verified 지식 heading: `VERIFIED_KNOWLEDGE`
- 모든 fact 직렬화에 `knowledge_role` metadata 포함
- Requirement, Step, common-mistakes warning에 verification과 role label 동시 표시
- FACT/STRATEGY/MEASUREMENT를 구분하도록 response guardrail 추가
- unresolved/conflict로 이동한 claim의 원래 role 보존
- Project requirement, acquisition quantity와 schedule은 결정적 FACT로 유지

## 발견한 기존 semantic limitation

V1.8E까지의 Prompt Bridge는 `verified` claim을 `canonical_facts`에 넣고 verification metadata만 직렬화했다. 당시에는 본격적인 Strategy Pack이 없어 문제가 드러나지 않았지만, V1.9C에서 verified strategy가 추가되면서 ChatGPT가 이를 공식 FACT와 구분할 정보가 사라졌다. V1.9D는 V1.8E 구현을 오류로 간주하지 않고, 새 데이터가 드러낸 소비 계층의 semantic gap을 additive role 필드로 닫는다.

## 역할 파생 규칙

| 대상 | 역할 |
| --- | --- |
| Content 기본값 | 모든 active Requirement가 지원 role을 명시하고 모두 같으면 그 role, 아니면 `fact` |
| summary / purpose / step | Content 기본값 |
| requirement | 자신의 지원 role이 있으면 우선, 없으면 Content 기본값 |
| `strategy` section | 항상 `strategy` |
| 그 외 section | Content 기본값 |
| reward / schedule | `fact` |
| Project의 결정적 projection / 계산 | `fact` |

역할은 source type으로 추론하지 않는다. verification status가 `verified`인지 여부도 역할 선택 기준으로 사용하지 않는다.

## 호환성

- `PromptFact` 이름 유지
- 응답 bundle의 `canonical_facts` 필드 유지
- 요청 selector의 `canonical_facts` 값 유지
- `PromptSection` 12개 값과 순서 유지
- frontend API request payload 유지
- `canonical_facts`는 호환 필드명이며 의미상 verified knowledge를 담는다.
- 새 Prompt mode, section, DB schema, migration 또는 seed field를 추가하지 않았다.

## 현재 seed role audit

실제 `data/seed_contents.json`의 Requirement를 직접 집계했다.

- role 없음: 385
- `fact`: 193
- `strategy`: 23
- `measurement`: 11
- 기존 비지원 값: `announced_not_live` 4, `historical` 2, `temporary_known_issue` 1

active Requirement 기준:

- role 없음: 382
- `fact`: 178
- `strategy`: 23
- `measurement`: 11
- `temporary_known_issue`: 1

V1.9D는 Prompt 역할 enum을 지시된 세 값으로만 제한했다. 기존 비지원 값에 새 의미를 임의 부여하지 않고 명시 role로 인정하지 않으며, 혼합·누락과 같은 보수적 `fact` fallback 경로를 사용한다. seed 데이터는 변경하지 않았다.

## V1.9C 의미 검증

다음 세 Content는 모든 Requirement가 `strategy`를 명시하므로 summary, purpose, requirements, steps, sections와 common mistakes가 strategy로 직렬화된다.

1. `gathering-onboarding-strategy`
2. `fishing-onboarding-strategy`
3. `hunting-onboarding-strategy`

실제 measurement seed인 `hexe-sanctuary-elvia` Requirement도 `measurement`로 직렬화됨을 검증했다. 일반 factual Content와 Carrack Project의 결정적 값은 `fact`를 유지한다.

## Golden 변경

`backend/tests/golden/carrack_project_optimizer.md`와 `weekly_review.md`는 다음 의도적 변화만 반영했다.

1. 역할 혼동 방지 guardrail 추가
2. `CANONICAL_FACTS` 표시 heading을 `VERIFIED_KNOWLEDGE`로 변경
3. Carrack verified knowledge 16개에 `knowledge_role: fact` 추가

기존 claim, verification, source, project state, checklist와 user question 내용은 변경하지 않았다.

## 테스트

### Backend

- V1.9D 전용 semantic tests: 15 passed
- Prompt Bridge 핵심 지정 회귀: 28 passed
- 전체: 259 passed, 기존 Starlette TestClient deprecation warning 1건

전용 테스트는 V1.9C strategy 기본값, factual/measurement/mixed role, unresolved 역할 보존, Project FACT, Markdown heading/metadata, context-only, guardrail, 12개 selector 호환성, deterministic compaction과 visible fact source 보존을 검증한다.

### Frontend

- `npm.cmd run typecheck`: passed
- `npm.cmd run lint`: passed
- `npm.cmd run test -- --run`: 14 files / 57 tests passed
- `npm.cmd run build`: passed, 41 modules transformed

selector 표시명은 `검증된 지식 (FACT/STRATEGY/MEASUREMENT)`으로 바뀌었고 요청 key는 계속 `canonical_facts`임을 테스트했다.

### 공통

- `git diff --check`: passed
- Source: 150, 변경 없음
- Content: 262 active, 변경 없음
- seed/migration/DB schema 변경: 없음
- 작업 전 `backend/bdo.db` SHA-256: `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 작업 후 `backend/bdo.db` SHA-256: `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 실제 DB 변경: 없음

## 제외 범위

- 신규 검은사막 데이터 또는 web research
- seed / schema / migration 변경
- 새 Prompt mode 또는 role별 별도 section
- role별 compaction 정책 재설계
- frontend 화면 흐름 또는 디자인 확장
- LLM/API 호출

## 후속 Life Pack 준비 상태

후속 Life 데이터가 Requirement의 지원 role을 명시하면 Prompt Bridge가 Content 기본값과 entity별 예외 규칙에 따라 역할을 보존할 준비가 되었다. mixed/incomplete 데이터는 결정적으로 `fact`로 fallback하므로 새 데이터 팩이 기존 prompt 의미를 임의로 바꾸지 않는다. 이번 milestone에서는 후속 Life seed를 추가하지 않았다.

`docs/DECISIONS.md`의 기존 ADR-013은 사용자 백업·복원 결정이므로 번호를 덮어쓰지 않고 본 결정을 ADR-014로 기록했다.
