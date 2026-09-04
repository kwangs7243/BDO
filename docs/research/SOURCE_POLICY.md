# Source & Verification Policy

기준일: 2026-09-02, KR 서버.

## Priority

### Tier A — authoritative
1. 최신 KR 공식 업데이트/패치노트
2. 현재 KR 모험가 가이드
3. 최신 공식 GM노트/이벤트

### Tier B — supporting
4. 최근 KR 공식 팁/포럼 글 (작성자 유저인 경우 community로 분류)
5. 최근 Inven/Reddit 등 실제 경험

### Tier C — lookup only
6. BDO Codex, Garmoth, Foundry 등 DB/가이드 사이트

## Verification rules

- **초기화 시간 / 보상 횟수 / 제작식 / 아이템 효과**: 공식 명시가 있으면 공식 1개로 확정 가능. 공식 문서끼리 충돌하면 최신 패치가 우선이며 conflict 기록.
- 커뮤니티만 있는 메타/운용 팁: 2개 이상의 최근 독립 자료를 권장하고 `community_consensus`로 표시.
- 2025년 이전 자료는 현재 시스템 설명에 직접 사용하지 말고, 최신 자료에서 세부가 누락됐을 때만 보조.
- `published_at`보다 **effective date**가 명확하면 별도 기록.
- 모든 content는 `last_verified_at` 보유.
- 90일 이상 지난 time-sensitive claim은 `needs_review` 후보. 안정적 시스템은 180~365일 정책 가능.

## Conflict handling
예: 오래된 가이드 A가 주간 완료 방식 X라고 하고, 2026 패치 B가 Y로 변경.
- A evidence → superseded
- B evidence → verified/current
- UI에는 Y만 기본 노출, 근거 펼치기에서 변경 이력 표시.

## Research workflow
1. 공식 가이드 검색
2. 최근 패치 검색 (콘텐츠명 + 최근 1년)
3. 현재 알려진 문제점 검색
4. 필요 시 최근 커뮤니티 체감/운용 팁
5. claim 단위 저장
6. 서로 다른 출처 교차검증
7. 검증일 기록

## 자동 수집 원칙
공식 사이트 전체를 무차별 scraper로 긁어 앱 런타임에 의존하지 않는다. 연구/import 도구로 가져와 사람이/에이전트가 검증한 후 canonical DB에 반영한다.
