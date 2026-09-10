<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 우두머리 가이드 충돌 및 발표 상태

## Identity

- slug: "boss-guide-conflicts"
- name_ko: "우두머리 가이드 충돌 및 발표 상태"
- category: "combat_pve"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "현재 규칙, 충돌 이력, 발표됐지만 미적용인 계획, 임시 알려진 문제를 분리한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `boss-guide-conflicts.gumiho-known-issue`

- seed_key: "boss-guide-conflicts.gumiho-known-issue"
- kind: "knowledge"
- requirement_level: "required"
- title: "구미호 임시 알려진 문제"
- description: "부활·재사망·여우굴 관련 현상은 임시 이슈이며 영구 규칙이 아니다."
- structured_value:

```json
{
  "boss": "Gumiho",
  "domain": "donghae",
  "knowledge_role": "temporary_known_issue",
  "permanent_fact": false,
  "symptoms": [
    "revive",
    "re-death",
    "fox cave"
  ]
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

- None

## Related Contents

### `boss-guide-conflicts.donghae`

- seed_key: "boss-guide-conflicts.donghae"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-donghae-current-system.md"
### `boss-guide-conflicts.hwanghae`

- seed_key: "boss-guide-conflicts.hwanghae"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-hwanghae-current-system"
- content_name_ko: "검은사당 황해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/black-shrine-hwanghae-current-system.md"
### `boss-guide-conflicts.world-boss`

- seed_key: "boss-guide-conflicts.world-boss"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-current-system"
- content_name_ko: "월드 우두머리 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 3
- relative_path: "../contents/world-boss-current-system.md"

## Evidence and Sources

### Current evidence

### `boss-guide-conflicts.claim.gumiho-known-issue::known-issues-current-2026-09-04`

- evidence_seed_key: "boss-guide-conflicts.claim.gumiho-known-issue::known-issues-current-2026-09-04"
- source_id: "known-issues-current-2026-09-04"
- title: "알려진 문제점 (최종 수정 : 2026-09-03 17:37)"
- url: "https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=2989&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_known_issues"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-guide-conflicts.gumiho-known-issue"
- claim_key: "requirement:gumiho-known-issue"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `boss-guide-conflicts.claim.future-black-shadow-removal::heidel-ball-boss-announcements-2026`

- evidence_seed_key: "boss-guide-conflicts.claim.future-black-shadow-removal::heidel-ball-boss-announcements-2026"
- source_id: "heidel-ball-boss-announcements-2026"
- title: "2026 하이델 연회 - 우두머리 및 검은사당 향후 계획"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?ADContent=v_noticecreator&ADMedium=kr_notice&ADSource=youtube_content_none&ADTrackerName=none&ADcampaign=heidel&countryType=ko-KR&gameCode=101&groupContentNo=15943"
- publisher: "Pearl Abyss"
- source_type: "official_announcement"
- published_at: "2026-07-25"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-guide-conflicts.future-black-shadow-removal"
- claim_key: "requirement:future-black-shadow-removal"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `boss-guide-conflicts.claim.future-donghae-orb-removal::heidel-ball-boss-announcements-2026`

- evidence_seed_key: "boss-guide-conflicts.claim.future-donghae-orb-removal::heidel-ball-boss-announcements-2026"
- source_id: "heidel-ball-boss-announcements-2026"
- title: "2026 하이델 연회 - 우두머리 및 검은사당 향후 계획"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?ADContent=v_noticecreator&ADMedium=kr_notice&ADSource=youtube_content_none&ADTrackerName=none&ADcampaign=heidel&countryType=ko-KR&gameCode=101&groupContentNo=15943"
- publisher: "Pearl Abyss"
- source_type: "official_announcement"
- published_at: "2026-07-25"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-guide-conflicts.future-donghae-orb-removal"
- claim_key: "requirement:future-donghae-orb-removal"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `boss-guide-conflicts.claim.future-hwanghae-rework::heidel-ball-boss-announcements-2026`

- evidence_seed_key: "boss-guide-conflicts.claim.future-hwanghae-rework::heidel-ball-boss-announcements-2026"
- source_id: "heidel-ball-boss-announcements-2026"
- title: "2026 하이델 연회 - 우두머리 및 검은사당 향후 계획"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?ADContent=v_noticecreator&ADMedium=kr_notice&ADSource=youtube_content_none&ADTrackerName=none&ADcampaign=heidel&countryType=ko-KR&gameCode=101&groupContentNo=15943"
- publisher: "Pearl Abyss"
- source_type: "official_announcement"
- published_at: "2026-07-25"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-guide-conflicts.future-hwanghae-rework"
- claim_key: "requirement:future-hwanghae-rework"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `boss-guide-conflicts.claim.future-laurau::heidel-ball-boss-announcements-2026`

- evidence_seed_key: "boss-guide-conflicts.claim.future-laurau::heidel-ball-boss-announcements-2026"
- source_id: "heidel-ball-boss-announcements-2026"
- title: "2026 하이델 연회 - 우두머리 및 검은사당 향후 계획"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?ADContent=v_noticecreator&ADMedium=kr_notice&ADSource=youtube_content_none&ADTrackerName=none&ADcampaign=heidel&countryType=ko-KR&gameCode=101&groupContentNo=15943"
- publisher: "Pearl Abyss"
- source_type: "official_announcement"
- published_at: "2026-07-25"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-guide-conflicts.future-laurau"
- claim_key: "requirement:future-laurau"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
