# Data Model

## 핵심 원칙

`content`는 지식의 중심 엔티티다. 절차·선행조건·보상·자유 형식 설명·관계·일정은 별도 엔티티로 저장하고, 검증 근거는 claim 단위로 연결한다. 반복 체크 상태는 기간별 instance로 보존한다.

seed가 관리하는 중첩 엔티티는 사람이 읽을 수 있는 안정적인 `seed_key`를 가진다. 문구와 순서가 바뀌어도 key는 바꾸지 않으며, seed에서 사라진 행은 삭제하지 않고 `active=false`로 보관한다.

## V1.6A 구현 엔티티

### content

- `id`, `slug`, `name_ko`
- `category`, `subcategory`
- `summary`, `purpose`
- `party_type`, `difficulty`
- `status` (`active`, `deprecated`, `temporarily_disabled`, `unknown`)
- `last_verified_at`

### content_requirement

- `content_id`, `seed_key`
- `kind` (`quest`, `level`, `gear`, `stat`, `item`, `knowledge`, `party`, `character`, `other`)
- `title` nullable, `description`
- `structured_value` nullable JSON
- `requirement_level` (`required`, `recommended`, `optional`)
- `order_no`, `active`

`structured_value`는 SQLAlchemy `JSON`을 사용한다. SQLite에서는 JSON 직렬화 형태, MySQL에서는 native JSON으로 매핑되며 애플리케이션 API 형태는 동일하다.

### content_step

- `content_id`, `seed_key`
- `phase` (`unlock`, `preparation`, `first_time`, `repeat`, `reward`, `maintenance`)
- `order_no`, `title`, `description`
- `checkable`, `active`

지식/절차 데이터이며 기간별 완료 이력을 담는 checklist item과 구분한다.

### reward

- `content_id`, `seed_key`
- `name`, `reward_type`
- `amount`, `min_amount`, `max_amount`, `unit` nullable
- `is_choice`, `choice_group`, `recommendation`, `notes`
- `order_no`, `active`

확인되지 않은 수량은 추정값을 넣지 않고 nullable로 둔다.

### content_section

- `content_id`, `seed_key`
- `section_type` (`overview`, `why`, `preparation`, `start`, `strategy`, `common_mistakes`, `notes`)
- `title`, `body_markdown`, `order_no`, `active`

### content_relation

- `from_content_id`, `to_content_id`, `seed_key`
- `relation_type` (`prerequisite`, `unlocks`, `related`, `source_for`, `part_of`, `alternative`, `project_link`)
- `note`, `order_no`, `active`

상세 API에서는 들어오는 관계와 나가는 관계를 함께 조회한다.

### schedule_rule

- `content_id`, `seed_key`
- `rule_type` (`quest_reset`, `attempt_reset`, `record_cutoff`, `reward_payout`, `spawn`, `event_end`)
- `timezone` (기본 `Asia/Seoul`)
- `recurrence_type` (`daily`, `weekly`, `fixed_datetime`, `manual`)
- `weekday` nullable (`0..6`), `time_local`, `fixed_datetime`
- `effective_from`, `effective_to`, `notes`, `active`

`quest_reset`과 `attempt_reset`만 checklist period를 구동할 수 있다. `reward_payout`과 `record_cutoff`은 표시용 일정이며 reset으로 사용하지 않는다.

### source / evidence

`source`:

- `id`, `url`, `title`, `publisher`, `source_type`
- `published_at`, `retrieved_at`, `region`

`evidence`:

- `seed_key`
- `entity_type`, `entity_id`, `claim_key`
- `source_id`, `evidence_note`
- `verification_status`, `last_verified_at`
- `superseded_by`, `active`

현재 상태 집계에 참여하는 active evidence는 `active=true`, `verification_status != superseded`, `superseded_by IS NULL`을 모두 만족한다. 과거/superseded 근거는 삭제하지 않고 상세 API에서 열람할 수 있다. seed mapping은 [Seed Format](../../data/SEED_FORMAT.md)을 따른다.

### checklist_template / checklist_template_item

`checklist_template`:

- `content_id`, `seed_key`, `name`
- `recurrence_scope` (`daily`, `weekly`, `custom`, `none`)
- `period_rule_id` nullable
- `enabled_default`, `active`

`checklist_template_item`:

- `template_id`, `seed_key`, `order_no`
- `label`, `details`, `reward_hint`, `active`

`period_rule_id`가 있으면 해당 reset-like schedule을 사용하고, 없으면 기존 호환을 위해 `recurrence_scope`의 일일 00:00/목요일 00:00 KST 규칙을 사용한다.

### checklist_instance / checklist_item_state

`checklist_instance`:

- `template_id`, `period_key`
- `period_start`, `period_end`, `generated_at`

`checklist_item_state`:

- `instance_id`, `template_item_id`
- `completed`, `completed_at`, `note`

`(template_id, period_key)`와 `(instance_id, template_item_id)`가 각각 유일하다. 새 기간은 새 instance를 만들며 과거 상태를 일괄 갱신하거나 삭제하지 않는다.

### user_content_state

- `content_id` unique
- `state` (`not_started`, `foundation`, `in_progress`, `completed`, `paused`, `ignore`)
- `priority` nullable integer
- `note`, `updated_at`

단일 로컬 사용자의 명시적 상태다. V1.6A에서는 checklist 완료 여부로 자동 추론하지 않는다.

## V1.8A Project Tracker 엔티티

게임 지식의 원본은 기존 Content/evidence에 둔다. 아래 Project 계열 정본은 계산에 적합한 normalized projection이며, `source_entity_type`과 `source_entity_seed_key`로 원본 Requirement 또는 Section을 추적한다. 사용자 입력은 seed-managed 정본과 분리한다.

### project / project_stage / project_stage_dependency

`project`:

- `slug` unique stable identity, `name_ko`, nullable `content_id`
- `summary`, `active`

`project_stage`:

- `project_id`, `seed_key`, `name`, nullable `description`
- `order_no`, `active`
- `(project_id, seed_key)` unique

`project_stage_dependency`:

- `project_id`, `stage_id`, `depends_on_stage_id`, `seed_key`, `active`
- 자기 자신 참조는 DB 제약과 importer validation으로 거부하며, 순환 DAG는 importer가 거부한다.

### material / project_material / project_material_source

`material`:

- 표시명이 아닌 stable `key` unique, `name_ko`, `unit`, `active`

`project_material`:

- `project_id`, nullable `stage_id`, `material_id`, `seed_key`
- `required_quantity >= 0`, `order_no`, nullable `notes`, `active`
- nullable `source_entity_type`, `source_entity_seed_key`

`project_material_source`:

- `project_material_id`, 기존 `content_id`, `seed_key`
- nullable `quantity_per_completion >= 0`, nullable `notes`, `order_no`, `active`
- 정본에서 정확한 1회 획득량을 확인할 수 없으면 `quantity_per_completion=null`로 둔다.

### user_material_inventory / user_project_stage_state

`user_material_inventory`:

- `material_id` unique, `quantity >= 0`, nullable `note`, `updated_at`
- 프로젝트별 예약량이 아닌 material별 전역 사용자 재고다.

`user_project_stage_state`:

- `stage_id` unique, `completed`, nullable `completed_at`, nullable `note`, `updated_at`
- 미완료로 되돌리면 `completed_at`을 null로 만든다.

seed 재수입은 두 user table을 수정하거나 archive하지 않는다. 부족량은 backend가 `max(required_quantity - owned_quantity, 0)`으로 결정적으로 계산한다.

## Period key 예시

- 일일 KST 00:00: `D:2026-09-02`
- 목요일 주간: `W:2026-08-27T00:00:00+09:00`
- 월요일 06:00 주간: `W:2026-08-31T06:00:00+09:00`
- 일요일 보상 지급: schedule 표시용이며 checklist period와 같지 않음

**절대 `checked=false` 일괄 UPDATE로 초기화하지 않는다.**

## 후속 milestone로 연기된 모델

- `character`, `character_role`
- `life_skill_profile`

이 항목은 설계 의도만 유지하며 현재 DB에는 stub 테이블을 만들지 않는다.
