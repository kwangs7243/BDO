# Constitution

## 1. 정확성이 기능보다 우선

게임 데이터는 UI나 AI 편의를 위해 임의 단순화하거나 만들지 않는다. 불확실하면 `unverified`/`needs_review`/`conflict` 등으로 표현한다.

## 2. 최신 KR 공식 자료 우선

현재 규칙은 최신 KR 공식 패치/업데이트와 가이드를 우선한다. 오래된 공식 자료와 최신 effective rule이 충돌하면 최신 규칙을 사용하고 과거 근거는 history로 보존한다.

## 3. 반복 규칙을 분리

필요 시 `quest_reset`, `attempt_reset`, `record_cutoff`, `reward_payout`, `spawn_schedule`, event deadline을 독립적으로 보존한다.

## 4. Canonical game knowledge와 personal state를 분리

게임 자체에 대한 공용 정본과 사용자의 목표/보유량/진행/Task/메모를 같은 ownership으로 섞지 않는다.

Personal-state domain은 local 또는 external일 수 있지만 owner가 명시되어야 한다. 같은 canonical game fact를 BDO DB와 personal-state system에 독립 정본으로 중복 관리하지 않는다.

## 5. Canonical Content는 유용한 답변에 충분해야 함

근거가 존재한다면 canonical representation은 무엇인지, 왜 하는지, 선행조건, 준비, 시작, 절차, 반복 규칙, reset/payout, 보상, 주의점, 관련 content/project, evidence freshness를 답할 수 있어야 한다.

이는 canonical representation 요구사항이며 특정 frontend page layout을 강제하지 않는다.

## 6. 자동 초기화는 기록 삭제가 아님

반복 상태는 period instance로 보존하고 history를 지우지 않는다. Historical/superseded canonical evidence도 삭제 대신 추적 가능하게 유지한다.

## 7. 정보 범위는 넓게, consumer context는 좁게

DB에는 넓은 지식을 저장하되 각 consumer는 질문/작업에 필요한 범위만 조회한다. local UI, Prompt Bridge, future AI adapter 모두 동일하다.

## 8. Project는 canonical requirement와 행동을 연결

Project definition은 stage, prerequisite, required material, acquisition source, recurring content, deterministic calculation을 연결한다. Personal project state는 별도다.

## 9. 원문 출처를 추적 가능하게

핵심 claim은 source URL, publication date, verification/retrieval date, evidence status/note로 추적 가능해야 한다.

## 10. Core는 외부 AI 없이도 동작 가능

Canonical knowledge service와 기존 local 기능은 mandatory external AI service 없이 동작해야 한다.

이 원칙은 local web UI가 사용자의 primary daily interface여야 한다는 뜻이 아니다.

## 11. Deterministic work before generative reasoning

Reset window, period key, shortage arithmetic, canonical lookup, evidence status처럼 결정적으로 해결 가능한 값은 backend/domain logic이 맡는다.

AI는 설명, 우선순위화, synthesis, open-ended reasoning을 담당한다.

## 12. Existing contracts are preserved unless explicitly migrated

Future integration 대비만을 이유로 stable seed key, historical import, local user-state, backup semantics, public API, `PromptContextBundle`, `canonical_facts` 호환 key를 깨지 않는다.

Migration/deprecation은 explicit milestone과 compatibility plan이 필요하다.

## 13. Product role

Repository의 장기 핵심 가치는 검증된 BDO KR knowledge backend와 deterministic game-domain logic이다.

Frontend는 supported reference/admin/local operational consumer로 유지한다.

Future AI adapters may become primary interaction surfaces, but implementation is a separate explicit milestone.

See `docs/PRODUCT_DIRECTION.md`.
