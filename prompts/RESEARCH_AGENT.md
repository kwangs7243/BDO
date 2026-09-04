# Research / Data Enrichment Prompt

목표: 하나의 검은사막 콘텐츠를 canonical DB seed에 추가할 수 있을 정도로 조사한다.

입력: 콘텐츠명 1개.

반드시 수행:
1. KR 공식 모험가 가이드 검색
2. 최근 12개월 KR 패치노트 검색
3. 알려진 문제점 검색
4. reset/reward/recipe/item effect처럼 변동성이 큰 claim을 별도 추출
5. 최근 커뮤니티 자료는 운용 팁/체감에만 보조 사용
6. 과거 자료와 최신 자료가 충돌하면 변경 이력 작성

출력 JSON 필드:
- content
- requirements[]
- steps[]
- schedules[]
- rewards[]
- pitfalls[]
- related_content[]
- sources[]
- evidence[]
- unresolved_questions[]
- last_verified_at

금지:
- 출처 없는 숫자 생성
- 오래된 가이드를 최신인 것처럼 사용
- 목요일 reset과 일요일 payout을 같은 필드로 표현
