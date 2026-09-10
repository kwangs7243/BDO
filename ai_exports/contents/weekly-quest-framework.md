<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 주간 의뢰 공통 규칙

## Identity

- slug: "weekly-quest-framework"
- name_ko: "주간 의뢰 공통 규칙"
- category: "system"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-02"
- party_type: null
- difficulty: null

## Overview

- summary: "일반 주간 의뢰 재수주는 목요일 00:00 KST 기준. 콘텐츠별 예외/보상 지급 규칙은 별도 schedule로 저장."
- purpose: null

## Requirements

- None

## Steps

- None

## Schedules

### `weekly-quest-framework.quest-reset`

- seed_key: "weekly-quest-framework.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일반 주간 의뢰 재수주 기준: 목요일 00:00 KST"

## Rewards

- None

## Sections

- None

## Related Contents

### `blood-altar.weekly-framework`

- seed_key: "blood-altar.weekly-framework"
- direction: "incoming"
- relation_type: "related"
- content_slug: "blood-altar"
- content_name_ko: "피의 제단"
- content_category: "combat_pve"
- note: "일반 주간 reset과 일요일 보상 지급을 구분하기 위한 관련 시스템 항목"
- order_no: 1
- relative_path: "../contents/blood-altar.md"
### `lekrashan-hunting.relation.weekly-framework`

- seed_key: "lekrashan-hunting.relation.weekly-framework"
- direction: "incoming"
- relation_type: "related"
- content_slug: "lekrashan-hunting"
- content_name_ko: "레크라샨 해왕류 의뢰"
- content_category: "ocean_guide"
- note: "일반 주간 목요일 초기화 규칙"
- order_no: 1
- relative_path: "../contents/lekrashan-hunting.md"
### `guild-boss-current-system.relation.weekly`

- seed_key: "guild-boss-current-system.relation.weekly"
- direction: "incoming"
- relation_type: "related"
- content_slug: "guild-boss-current-system"
- content_name_ko: "길드 우두머리 현행 시스템"
- content_category: "combat_pve"
- note: "일반 목요일 주간과 다른 reset"
- order_no: 2
- relative_path: "../contents/guild-boss-current-system.md"
### `last-gladiius-weekly.weekly-framework`

- seed_key: "last-gladiius-weekly.weekly-framework"
- direction: "incoming"
- relation_type: "related"
- content_slug: "last-gladiius-weekly"
- content_name_ko: "최후의 글라디우스 주간 토벌"
- content_category: "combat_pve"
- note: "일반 주간 의뢰 period와 목요일 reset 의미"
- order_no: 2
- relative_path: "../contents/last-gladiius-weekly.md"
### `panokseon.relation.weekly-framework`

- seed_key: "panokseon.relation.weekly-framework"
- direction: "incoming"
- relation_type: "related"
- content_slug: "panokseon"
- content_name_ko: "판옥선"
- content_category: "ocean_guide"
- note: "도면 주간 의뢰 초기화"
- order_no: 3
- relative_path: "../contents/panokseon.md"

## Evidence and Sources

### Current evidence

### `weekly-quest-framework.summary::weekly-reset-2021`

- evidence_seed_key: "weekly-quest-framework.summary::weekly-reset-2021"
- source_id: "weekly-reset-2021"
- title: "7월 28일 (수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=6125"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "weekly-quest-framework"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-02"
- evidence_note: "일반 주간 의뢰 재수주 기준을 목요일 00시로 통일한 근거"
- active: true
- is_active: true

### `weekly-quest-framework.schedule.quest-reset::weekly-reset-2021`

- evidence_seed_key: "weekly-quest-framework.schedule.quest-reset::weekly-reset-2021"
- source_id: "weekly-reset-2021"
- title: "7월 28일 (수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=6125"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "weekly-quest-framework.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-02"
- evidence_note: "목요일 00:00 KST 재수주 기준"
- active: true
- is_active: true

### Historical / inactive evidence

- None
