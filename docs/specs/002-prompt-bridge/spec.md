# Feature Spec 002 — ChatGPT Prompt Bridge (V1.5)

## Product statement
V1.5는 런타임 LLM/API 없이도 BDO Companion의 구조화된 최신 데이터와 사용자 진행도를 이용해 **ChatGPT에 붙여넣을 고품질 질문 프롬프트**를 생성한다.

앱이 사실 검색/선별/계산을 담당하고, ChatGPT는 사용자가 원할 때만 별도 대화에서 해석·요약·의사결정을 돕는다.

## V1.5 boundaries

### 포함
- 관련 콘텐츠/프로젝트/체크리스트/사용자 상태를 로컬에서 검색
- 검증 상태와 출처를 포함한 context bundle 생성
- 목적별 prompt template 적용
- 미리보기 / 복사 / Markdown 다운로드
- 사용자 질문을 prompt 끝에 결합
- context token/문자 수 추정과 과다 컨텍스트 경고
- `verified` 정보 우선, `conflict`/`needs_review` 명시

### 제외
- OpenAI API 호출
- 외부 LLM API 호출
- 로컬 LLM 실행
- fine-tuning
- embedding API 의존
- 자동으로 ChatGPT 웹 UI를 조작하거나 대화를 전송하는 기능

## Primary user stories

### US-1 콘텐츠 입문 질문
사용자가 수렵 상세 페이지에서 `ChatGPT에 물어보기`를 누른다.
앱은 수렵의 개요, 선행조건, 현재 장비 체계, 체크리스트, 사용자 상태, 검증 출처를 모아 프롬프트를 만든다.
사용자는 질문에 `지금 내 상태에서 오늘 뭘 하면 돼?`를 입력하고 복사한다.

### US-2 프로젝트 최적화 질문
중범선 : 점진 페이지에서 현재 재료 보유량, 부족량, 완료 단계, 일/주간 완료 상태, 반복 수급처가 자동 포함된다.
사용자는 `이번 주 안에 최대한 빨리 끝내는 순서를 짜줘`를 붙여 ChatGPT에 질문한다.

### US-3 정보 검증 질문
콘텐츠의 일부 claim이 `needs_review` 또는 `conflict` 상태면 prompt에 이를 별도 섹션으로 넣는다.
ChatGPT에게 `아래 미검증 항목은 최신 KR 공식 자료를 웹 검색해서 검증해줘`라고 요청할 수 있다.

## Functional requirements

### FR-P1 Prompt entry points
다음 화면에서 Prompt Bridge를 열 수 있어야 한다.
- content detail
- life detail
- project detail
- today/weekly dashboard
- global `/prompt` page

### FR-P2 Context selector
사용자는 포함할 범위를 확인/토글할 수 있다.
- 현재 페이지 핵심 정보
- requirements / steps / rewards
- schedules/reset rules
- 사용자 진행도/메모
- 현재 checklist 상태
- project materials/shortages
- related contents
- evidence/source summary
- unresolved claims

기본값은 현재 질문에 필요한 최소 범위를 선택한다.

### FR-P3 Deterministic context bundle
백엔드는 동일 입력에 대해 순서가 안정적인 구조화 bundle을 반환한다.

권장 순서:
1. `REQUEST_CONTEXT`
2. `USER_STATE`
3. `VERIFIED_KNOWLEDGE`
4. `SCHEDULES`
5. `PROJECT_STATE` (해당 시)
6. `OPEN_QUESTIONS_OR_CONFLICTS`
7. `SOURCES`
8. `USER_QUESTION`

### FR-P4 Source-aware serialization
각 verified knowledge 항목은 가능하면 다음 메타데이터를 포함한다.
- knowledge role: `fact`, `strategy`, `measurement`
- verification status
- last verified date
- source title
- source URL
- source type

원문 전체를 복사하지 않고 **claim과 짧은 evidence note** 중심으로 직렬화한다.

API bundle과 context selector의 `canonical_facts` 키는 기존 클라이언트 호환성을 위해 유지하지만, 의미상 `verified` 상태의 지식 전체를 뜻한다. Content의 기본 역할은 모든 Requirement가 같은 지원 role을 명시할 때 그 role을 따르고 그 외에는 `fact`로 보수적으로 처리한다. Requirement는 자신의 명시 role을 우선하며, `strategy` Section은 항상 `strategy`, Reward/Schedule과 결정적 Project 계산값은 항상 `fact`다. source type만으로 role을 추론하지 않으며 unresolved로 이동해도 role은 보존한다.

### FR-P5 Prompt modes
최소 5개 preset을 제공한다.

1. `next_action` — 지금 무엇을 해야 하는가
2. `content_onboarding` — 이 콘텐츠 입문 가이드
3. `project_optimizer` — 장기 프로젝트 최적화
4. `weekly_review` — 오늘/이번 주 남은 것 우선순위
5. `verify_latest` — 미검증/충돌 정보를 최신 KR 공식 자료로 재검증 요청

### FR-P6 Prompt guardrails
생성된 prompt에는 다음 지침을 기본 포함한다.
- 제공된 verified 데이터는 우선 사용
- 날짜/패치 의존 정보는 최신 KR 공식 자료를 우선 검증
- 미검증 값은 추측하지 않음
- 과거 공략이 최신 공식 자료와 충돌하면 최신 공식 자료 우선
- 정확한 수량/초기화/보상은 근거 없이는 단정하지 않음
- 사용자의 현재 완료 상태를 다시 해야 할 일로 추천하지 않음
- `FACT`/`STRATEGY`/`MEASUREMENT`를 구분하고 전략·측정값을 공식 사실처럼 단정하지 않음

### FR-P7 Copy/export
- 클립보드 복사
- `.md` 다운로드
- 필요 시 `context-only` / `full prompt` 선택
- 생성 결과는 기본적으로 DB에 저장하지 않는다.

### FR-P8 Size control
- 문자 수와 대략적 token 추정치 표시
- 기본 목표: 12,000 tokens 이하
- 12,000 초과 시 related/community evidence를 우선 줄임
- 사용자가 `상세하게`를 선택하면 수동 확장 가능

### FR-P9 Privacy/local-first
- Prompt Bridge 생성은 100% localhost에서 수행
- API key 입력 UI를 V1.5에 만들지 않는다.
- 외부 전송 버튼을 만들지 않는다.
- 사용자가 직접 복사/붙여넣기 한다.

## Context bundle example

```markdown
# BDO Companion Context
Generated: 2026-09-02T23:00:00+09:00
Region: KR

## REQUEST_CONTEXT
- page: project/carrack-advance
- mode: project_optimizer

## USER_STATE
- current ship: Epheria Caravel
- target: Carrack Advance
- weekly Black Rust: completed

## VERIFIED_KNOWLEDGE
- Carrack Advance requires ...
  - knowledge_role: fact
  - verification: verified
  - last_verified: 2026-09-02

## PROJECT_STATE
- material A: 40 / 90 (shortage 50)
...

## OPEN_QUESTIONS_OR_CONFLICTS
- none

## SOURCES
1. [Official] ...

## USER_QUESTION
이번 주 안에 최대한 빨리 끝내는 순서를 짜줘.
```

## Definition of done
- LLM/API 없이 작동한다.
- 현재 페이지에서 2클릭 이내로 prompt 미리보기에 도달한다.
- 완료된 checklist와 미완료 checklist가 정확히 구분되어 포함된다.
- `verified`와 `needs_review/conflict`가 prompt에서 명확히 구분된다.
- `FACT`, `STRATEGY`, `MEASUREMENT`가 prompt에서 명시되고 unresolved 항목도 원래 역할을 유지한다.
- project shortage는 DB 계산값을 사용하며 LLM에게 계산을 떠넘기지 않는다.
- 브라우저 clipboard 실패 시 textarea 선택 + 수동 복사가 가능하다.
