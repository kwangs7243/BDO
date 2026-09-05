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

## FACT / STRATEGY / MEASUREMENT handling

- 수량, 효과, 시스템 조건과 현재 동작은 최신 KR 공식 자료를 근거로 FACT에 저장한다.
- 커뮤니티·정보 사이트 자료는 입문 순서, 목적별 선택, 동선과 운용 팁 같은 STRATEGY를 보조하며 공식 FACT를 대신하지 않는다.
- 커뮤니티의 exact 수치는 최신 공식 검증 없이는 FACT로 승격하지 않는다.
- 실제 세션의 시간·수익·효율·확률 표본은 MEASUREMENT로 분리한다.
- 일반화된 커뮤니티 추천은 가능하면 최근 독립 자료 둘 이상으로 교차검증한다. 교차검증이 부족하면 적용 조건과 단일 작성자 맥락을 명시하거나 seed에서 제외한다.
- 과거 전략 자료를 사용할 때는 최신 공식 변경과 충돌하는지 먼저 확인하고, 오래된 exact 세팅·수치는 현재 canonical 값으로 복사하지 않는다.
- 특정 커뮤니티 사이트나 작성자를 authoritative tier로 승격하지 않는다. 검사학개론 자료도 supporting strategy source로만 사용한다.

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
