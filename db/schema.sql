-- V1.6A reference schema. SQLAlchemy models and Alembic revisions are authoritative.
-- AUTO_INCREMENT notation is illustrative; runtime DDL supports SQLite and MySQL.

CREATE TABLE source (
  id VARCHAR(64) PRIMARY KEY, url TEXT NOT NULL, title VARCHAR(255) NOT NULL,
  publisher VARCHAR(120), source_type VARCHAR(32) NOT NULL,
  published_at DATE NULL, retrieved_at DATETIME NULL,
  region VARCHAR(16) NOT NULL DEFAULT 'KR'
);

CREATE TABLE content (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, slug VARCHAR(120) UNIQUE NOT NULL,
  name_ko VARCHAR(255) NOT NULL, category VARCHAR(64) NOT NULL,
  subcategory VARCHAR(64), summary TEXT, purpose TEXT,
  party_type VARCHAR(32), difficulty VARCHAR(32),
  status VARCHAR(32) NOT NULL DEFAULT 'active', last_verified_at DATE NULL
);

CREATE TABLE schedule_rule (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, content_id BIGINT NOT NULL,
  seed_key VARCHAR(160), rule_type VARCHAR(32) NOT NULL,
  timezone VARCHAR(64) NOT NULL DEFAULT 'Asia/Seoul',
  recurrence_type VARCHAR(32) NOT NULL, weekday INT NULL, time_local TIME NULL,
  fixed_datetime DATETIME NULL, effective_from DATE NULL, effective_to DATE NULL,
  notes TEXT, active BOOLEAN NOT NULL DEFAULT TRUE,
  UNIQUE(content_id, seed_key), FOREIGN KEY (content_id) REFERENCES content(id)
);

CREATE TABLE evidence (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, seed_key VARCHAR(255) UNIQUE,
  entity_type VARCHAR(32) NOT NULL, entity_id VARCHAR(128) NOT NULL,
  claim_key VARCHAR(128) NOT NULL, source_id VARCHAR(64) NOT NULL,
  evidence_note TEXT, verification_status VARCHAR(32) NOT NULL,
  last_verified_at DATE NOT NULL, superseded_by BIGINT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  FOREIGN KEY (source_id) REFERENCES source(id),
  FOREIGN KEY (superseded_by) REFERENCES evidence(id)
);

CREATE TABLE content_requirement (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, content_id BIGINT NOT NULL,
  seed_key VARCHAR(160) NOT NULL, kind VARCHAR(32) NOT NULL,
  title VARCHAR(255), description TEXT NOT NULL, structured_value JSON NULL,
  requirement_level VARCHAR(32) NOT NULL, order_no INT NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE, UNIQUE(content_id, seed_key),
  FOREIGN KEY (content_id) REFERENCES content(id)
);

CREATE TABLE content_step (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, content_id BIGINT NOT NULL,
  seed_key VARCHAR(160) NOT NULL, phase VARCHAR(32) NOT NULL,
  order_no INT NOT NULL, title VARCHAR(255) NOT NULL, description TEXT NOT NULL,
  checkable BOOLEAN NOT NULL DEFAULT FALSE, active BOOLEAN NOT NULL DEFAULT TRUE,
  UNIQUE(content_id, seed_key), FOREIGN KEY (content_id) REFERENCES content(id)
);

CREATE TABLE reward (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, content_id BIGINT NOT NULL,
  seed_key VARCHAR(160) NOT NULL, name VARCHAR(255) NOT NULL,
  reward_type VARCHAR(64) NOT NULL, amount FLOAT NULL, min_amount FLOAT NULL,
  max_amount FLOAT NULL, unit VARCHAR(64), is_choice BOOLEAN NOT NULL DEFAULT FALSE,
  choice_group VARCHAR(120), recommendation TEXT, notes TEXT, order_no INT NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE, UNIQUE(content_id, seed_key),
  FOREIGN KEY (content_id) REFERENCES content(id)
);

CREATE TABLE content_section (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, content_id BIGINT NOT NULL,
  seed_key VARCHAR(160) NOT NULL, section_type VARCHAR(32) NOT NULL,
  title VARCHAR(255) NOT NULL, body_markdown TEXT NOT NULL, order_no INT NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE, UNIQUE(content_id, seed_key),
  FOREIGN KEY (content_id) REFERENCES content(id)
);

CREATE TABLE content_relation (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, from_content_id BIGINT NOT NULL,
  to_content_id BIGINT NOT NULL, seed_key VARCHAR(160) NOT NULL,
  relation_type VARCHAR(32) NOT NULL, note TEXT, order_no INT NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE, UNIQUE(from_content_id, seed_key),
  FOREIGN KEY (from_content_id) REFERENCES content(id),
  FOREIGN KEY (to_content_id) REFERENCES content(id)
);

CREATE TABLE checklist_template (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, content_id BIGINT NULL,
  seed_key VARCHAR(160), name VARCHAR(255) NOT NULL,
  recurrence_scope VARCHAR(32) NOT NULL, period_rule_id BIGINT NULL,
  enabled_default BOOLEAN NOT NULL DEFAULT TRUE, active BOOLEAN NOT NULL DEFAULT TRUE,
  UNIQUE(content_id, seed_key), FOREIGN KEY (content_id) REFERENCES content(id),
  FOREIGN KEY (period_rule_id) REFERENCES schedule_rule(id)
);

CREATE TABLE checklist_template_item (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, template_id BIGINT NOT NULL,
  seed_key VARCHAR(160), order_no INT NOT NULL, label VARCHAR(255) NOT NULL,
  details TEXT, reward_hint TEXT, active BOOLEAN NOT NULL DEFAULT TRUE,
  UNIQUE(template_id, seed_key), FOREIGN KEY (template_id) REFERENCES checklist_template(id)
);

CREATE TABLE checklist_instance (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, template_id BIGINT NOT NULL,
  period_key VARCHAR(100) NOT NULL, period_start DATETIME NOT NULL,
  period_end DATETIME NOT NULL, generated_at DATETIME NOT NULL,
  UNIQUE(template_id, period_key), FOREIGN KEY (template_id) REFERENCES checklist_template(id)
);

CREATE TABLE checklist_item_state (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, instance_id BIGINT NOT NULL,
  template_item_id BIGINT NOT NULL, completed BOOLEAN NOT NULL DEFAULT FALSE,
  completed_at DATETIME NULL, note TEXT, UNIQUE(instance_id, template_item_id),
  FOREIGN KEY (instance_id) REFERENCES checklist_instance(id),
  FOREIGN KEY (template_item_id) REFERENCES checklist_template_item(id)
);

CREATE TABLE user_content_state (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, content_id BIGINT UNIQUE NOT NULL,
  state VARCHAR(32) NOT NULL DEFAULT 'not_started', priority INT NULL,
  note TEXT, updated_at DATETIME NOT NULL,
  FOREIGN KEY (content_id) REFERENCES content(id)
);
