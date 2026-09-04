# Architecture Decision Log

## ADR-001 Local web app over Notion as primary tracker
**Decision:** Notion은 참고/기존자료 보관, 실제 진행 관리는 로컬 웹앱.
**Reason:** 자동 period 관리, 관계형 데이터, 검색, 재료 계산, source versioning을 일반 Notion 페이지보다 명확히 구현 가능.

## ADR-002 Period instances over checkbox reset
**Decision:** 반복 체크 상태를 매주 false로 덮지 않는다.
**Reason:** history 보존, 서로 다른 reset 시간 지원, 앱 비실행 기간 안정성.

## ADR-003 MySQL optional, SQLite compatible
**Decision:** SQLAlchemy abstraction 사용.
**Reason:** 사용자 PC의 MySQL 활용 가능 + 프로젝트 이동/초기 설치 단순성.

## ADR-004 AGENTS.md is a map, not encyclopedia
**Decision:** 자세한 규칙은 docs에 분산.
**Reason:** agent context 낭비와 stale monolith 방지.


## ADR-005 V1.5 uses Prompt Bridge, not runtime LLM
**Decision:** V1.5에서는 OpenAI API/타 LLM API/로컬 LLM을 앱에 연결하지 않고, DB 검색 결과와 사용자 진행도를 구조화한 ChatGPT용 prompt를 생성한다.
**Reason:** 추가 비용 0원, local-first 유지, 데이터 정확성의 책임을 앱에 남기고 향후 V2 RAG/API로 확장 가능한 경계를 만든다.

## ADR-006 Deterministic retrieval before generative reasoning
**Decision:** shortage, reset window, 완료 여부, requirement 충족 여부처럼 규칙으로 계산 가능한 값은 백엔드가 결정한다.
**Reason:** LLM에게 사실 계산을 맡기면 비용과 오류가 모두 증가한다. V1.5 prompt에는 계산 결과와 근거만 제공한다.

## ADR-007 First V1.5 slice defers project optimizer
**Decision:** 첫 V1.5 vertical slice는 `content_onboarding`과 `weekly_review` preset을 구현하고, `project_optimizer`와 project/material context는 프로젝트 스키마가 구현되는 다음 milestone로 남긴다.
**Reason:** `prompts/CODEX_BOOTSTRAP.md`는 project/material 스키마가 없을 때 stub을 만들지 말라고 명시한다. 빈 project context나 추측한 중범선 재료 데이터를 만드는 것보다 검증된 content/checklist/source 흐름을 먼저 완성하는 편이 Constitution의 정확성 원칙에 맞는다.

## ADR-008 Stable seed identity and archival removal

**Decision:** seed 관리 중첩 행은 표시 문구가 아닌 부모 범위의 안정적인 `seed_key`로 식별한다. 재수입 시 같은 행을 제자리 갱신하고, canonical seed에서 제거된 행은 삭제 대신 `active=false`로 보관한다. 기존 V1.5의 key 없는 schedule/checklist 행은 첫 V1.6A import에서 안전하게 대응되는 행을 찾아 key를 부여한다.

**Reason:** label 기반 식별이나 삭제 후 재생성은 문구 수정만으로 ID와 checklist history를 끊는다. 안정 key와 archival 방식은 대량 데이터 확장 시 diff 검토가 가능하고 기존 사용자 이력을 유지한다.

## ADR-009 Checklist period-rule ownership

**Decision:** checklist template은 nullable `period_rule_id`로 특정 `ScheduleRule`을 참조할 수 있다. `quest_reset`과 `attempt_reset`만 period를 구동하며, 참조가 없을 때만 기존 daily 00:00/weekly 목요일 00:00 KST fallback을 사용한다. `reward_payout`과 `record_cutoff`은 표시용 schedule로 남긴다.

**Reason:** 모든 주간 콘텐츠가 목요일 기준이라는 가정은 확장되지 않는다. reset의 소유자를 명시하면 콘텐츠별 요일·시각을 지원하면서 보상 지급과 진행 초기화를 혼동하지 않는다.

## ADR-010 Portable structured values and forward-only V1.6A migration

**Decision:** requirement의 `structured_value`는 SQLAlchemy `JSON`을 사용한다. V1.6A 변경은 새 revision `20260903_0002`로 적용하며, initial revision 파일은 당시 V1.5 테이블 정의로 동결해 새 DB에서도 `0001 → 0002` 경로가 동일하게 실행되도록 한다.

**Reason:** SQLAlchemy JSON은 SQLite 직렬화와 MySQL native JSON을 같은 모델/API로 다룰 수 있다. initial revision이 현재 metadata를 동적으로 생성하면 새 DB에서 `0002`가 컬럼을 중복 추가하므로, 이미 적용된 DB의 revision 상태는 건드리지 않으면서 역사적 DDL만 고정할 필요가 있다.
