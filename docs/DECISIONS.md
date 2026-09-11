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

## ADR-011 Project knowledge projection and user inventory separation

**Decision:** 게임 사실의 원본은 기존 Content/evidence로 유지하고, ProjectMaterial은 tracker 계산을 위한 normalized projection으로 저장한다. 각 ProjectMaterial은 가능한 경우 원본 Requirement 또는 Section의 stable seed key를 기록한다. Project, Stage, Material과 획득처 연결은 seed-managed 정본이며, 재료 보유량과 단계 완료 상태는 각각 `UserMaterialInventory`, `UserProjectStageState`에 분리한다. 부족량은 backend가 `max(required_quantity - owned_quantity, 0)`으로 계산한다.

**Reason:** 원본 지식과 계산용 투영을 구분하면 같은 사실을 독립적으로 재작성하는 오류를 줄일 수 있다. 사용자 상태를 canonical import 대상과 분리하면 seed 갱신·archive·재수입 뒤에도 재고와 완료 이력을 보존할 수 있고, shortage 결과는 UI나 LLM에 맡기지 않고 항상 재현할 수 있다.

## ADR-012 Deterministic Prompt selection and compaction

**Decision:** Context selector는 canonical knowledge와 사용자 데이터를 수정하지 않고 직렬화할 section만 제어한다. 자동 size control은 문자열을 자르거나 사실을 재작성하지 않고 완전한 item 또는 section 단위의 deterministic omission만 사용한다. unresolved claim, 사용자 상태, checklist, schedule과 Project의 stage/material/shortage 핵심 값은 우선 보존하고, related contents, historical/non-official/unlinked source, Project acquisition detail과 저우선 narrative를 먼저 줄인다. `detailed` mode는 자동 생략을 수행하지 않는다.

**Reason:** 12,000 estimated token 목표를 적용하면서도 값 왜곡, LLM 기반 요약과 실행마다 달라지는 결과를 피하고 동일 입력의 재현성을 유지하기 위해서다.


## ADR-013 Stable-key user backup and atomic restore

**Decision:** 사용자 백업은 canonical knowledge가 아니라 `UserContentState`, 전체 `ChecklistInstance`/`ChecklistItemState` 이력, `UserMaterialInventory`, `UserProjectStageState`만 포함한다. DB별로 달라지는 numeric ID 대신 Content slug, checklist template/item seed key와 period key, Material key, Project slug와 stage seed key를 사용한다. import는 전체 payload와 모든 canonical 참조를 먼저 검증한 뒤 한 transaction으로 실행하며, unknown identity는 조용히 건너뛰지 않고 전체 복원을 거부한다. `merge`는 backup에 있는 identity를 덮어쓰고 local-only 상태를 유지하며, `replace`는 네 사용자 상태 영역을 backup 내용으로 정확히 교체한다. archive된 canonical identity도 history 복원을 위해 resolve하지만 active 상태로 되돌리지 않는다.

**Reason:** 사용자 기록을 다른 seed 초기화 DB로 안전하게 옮기려면 DB row ID와 canonical 본문을 백업에서 분리해야 한다. 완전한 사전 검증과 원자적 복원은 일부 이력만 적용되는 손상을 방지하며, merge/replace 의미를 구분하면 보존 중심 복원과 명시적 전체 교체를 모두 예측 가능하게 제공할 수 있다.

## ADR-014 Prompt knowledge role semantics and compatibility

**Decision:** Prompt Bridge의 verified knowledge는 claim마다 `fact`, `strategy`, `measurement` 역할을 명시한다. 역할은 Requirement의 `structured_value.knowledge_role`과 Content 구조에서 결정하며 source type으로 추론하지 않는다. 모든 Requirement가 같은 지원 역할을 선언한 Content만 그 역할을 기본값으로 사용하고, 혼합·누락·지원하지 않는 값은 `fact` 기본값으로 처리한다. `strategy` Section은 항상 전략, Reward/Schedule과 Project의 결정적 투영·계산은 항상 사실로 분류한다. verification 상태와 역할은 독립적이므로 unresolved/conflict 항목도 원래 역할을 유지한다. API bundle 및 12개 context selector의 `canonical_facts` 키는 호환성을 위해 유지하고 Markdown 표시 heading만 `VERIFIED_KNOWLEDGE`로 명확히 한다.

**Reason:** verified는 근거 검증 상태이지 공식 사실 여부를 뜻하지 않는다. 커뮤니티 기반 전략과 측정 관찰값도 검증될 수 있으므로 이를 사실과 구분해야 ChatGPT가 전략·측정값을 게임의 공식 규칙처럼 단정하지 않는다. 동시에 공개 계약 키를 바꾸지 않아 기존 UI와 요청 payload를 깨뜨리지 않는다.

## ADR-015 Product role centered on canonical knowledge; personal-state ownership is domain-scoped

**Status:** Accepted 2026-09-09.
**Supersedes:** ADR-001 only where ADR-001 states that Notion is merely reference storage and the local web app must be the primary tracker for all personal progress.

**Decision:** BDO Companion's primary long-term responsibility is verified Black Desert Online KR canonical knowledge, evidence/history, deterministic game-domain logic, and stable retrieval/context contracts. The existing local frontend and local personal-state system remain supported, but they are not required to be the user's primary daily interaction surface.

Personal-state ownership may be assigned by domain. Actual life-project usage has validated an external Notion workspace as an effective AI-readable/writable personal-state backend, but this does not authorize migration of all user state. Existing `UserContentState`, checklist history, `UserMaterialInventory`, `UserProjectStageState`, and backup behavior remain intact until an explicit domain migration/integration milestone changes their ownership.

Canonical game knowledge must not be independently maintained in Notion or another personal-state store. Future ChatGPT/MCP/API integrations should normally be thin consumers behind the existing domain service/API/`PromptContextBundle` boundaries rather than replacements for the canonical database.

The frontend remains a supported reference / inspection / admin / local operational consumer. Consumer-UI expansion is lower roadmap priority unless explicitly requested.

**Reason:** Actual usage shows that conversational interaction through ChatGPT can be more effective than manually navigating a dedicated tracker UI, while the repository's strongest reusable asset is its structured, sourced, version-aware game knowledge. Keeping the canonical backend and current compatibility intact preserves previous implementation value and allows AI or external personal-state integrations to be introduced incrementally without a rewrite.

## ADR-016 Caller-provided personal state is ephemeral calculation input

**Status:** Accepted 2026-09-10.

**Decision:** External or caller-owned personal state may be supplied as input to a deterministic calculation request. The V1.9O Project calculator combines caller-provided material quantities with canonical Project requirements, but does not automatically write those values to local user-state tables. Canonical Project requirements remain owned by the BDO database. A missing caller quantity means `0`, not a fallback to `UserMaterialInventory`. Persistence and synchronization require a separate explicit milestone.

**Reason:** Keeping caller state ephemeral allows future AI or external personal-state consumers to reuse canonical formulas without creating a second writable Source of Truth, mutating the local tracker, or making the same request depend on hidden local values. The result remains deterministic for the same canonical Project definition and request payload.

## ADR-017 Generated AI exports are derived, disposable consumer artifacts

**Status:** Accepted 2026-09-10.

**Decision:** `ai_exports/` contains disposable consumer artifacts generated from the canonical BDO backend. Humans do not authoritatively edit these files; the canonical seed and domain model remain the Source of Truth. Exports contain no personal state, are deterministic for the same canonical input, and must be usable from GitHub or another static reader without a paid runtime/API dependency. Automated freshness checks fail when committed output is missing, changed, or contains unexpected files. A future MCP or API consumer must not promote this export directory into a canonical store.

**Reason:** This makes the existing structured backend directly useful in the current ChatGPT Plus + GitHub environment without additional paid infrastructure, while preventing generated Markdown from becoming a manually maintained second Source of Truth.

## ADR-018 — Material identity is shared; Recipe quantities belong to recipe options

**Status:** Accepted 2026-09-10.

**Decision:** `seed_materials.json` owns the shared Material catalog. Project and Recipe importers resolve stable keys rather than independently owning or archiving Material rows. Existing Material IDs, ProjectMaterial references and user inventory remain intact. Historical embedded Project materials are accepted only when the shared file is absent; simultaneous authorities are rejected. A legacy partial catalog never archives other domains' materials.

Cooking recipes use IngredientGroup, IngredientGroupMember, Recipe, RecipeIngredientSlot and RecipeIngredientOption. Membership describes substitutability, not a global conversion ratio. Slots are AND; options within a slot are OR. Each option targets exactly one Material or IngredientGroup and records a positive, finite quantity for one cooking attempt. Mixed substitution, guaranteed output quantities, quality conversion, profitability and recipe calculations are not implemented.

Recipe/group/slot/option claims reuse typed stable-key Evidence. Official membership and per-attempt semantics may be verified while an exact formula remains needs_review. Canonical recipe retrieval/search excludes personal state and numeric DB identities. Static recipe Markdown consumes the same read service through an isolated DB; manifest schema version 2 adds recipes while preserving Content/Project entries. PromptContextBundle, Project calculations and user backup version 1 remain unchanged.

**Reason:** One Material identity supports recipes and existing projects without breaking inventory history. Option-level quantities avoid false global substitution multipliers; unconfirmed formulas remain inspectable without being promoted to verified official facts.

## ADR-019 — Recipe batch calculation preserves alternative semantics

**Status:** Accepted 2026-09-11.

**Decision:** Canonical `RecipeIngredientOption.required_quantity` means the quantity for one cooking attempt. The V1.9S stateless batch calculator multiplies each option independently by a strict positive integer `attempt_count`, preserving slot AND, option OR, option order, stable identities, and IngredientGroup targets. It does not select, sum, mix, or optimize OR options and does not resolve an IngredientGroup to one member. It reads no personal state and writes no database state. Result quantity, cooking proc behavior, quality conversion, inventory shortage, profitability, and optimization remain separate future milestones. Canonical Recipe data and the existing knowledge service are the calculation Source of Truth.

**Reason:** Separating deterministic scaling from substitution and optimization makes the verified canonical one-attempt facts reusable without inventing unmodeled replacement, quality, production-output, or economic rules.
