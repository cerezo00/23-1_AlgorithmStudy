# 1946 신입사원
# 메모리 35124 KB, 시간 2260ms
# 모든 이와 비교하여 서류 심사 성적, 면접 성적 중 하나라도 높아야 함
# 서류 심사 성적 오름차순 정렬 -> 면접 성적을 비교하여 이전 사람보다 높아야 함

import sys
input = sys.stdin.readline

T = int(input())      # 테스트 케이스 개수 입력
for _ in range(T):
    N = int(input())  # 지원자 숫자 N 입력
    rank = [0] * (N + 1) # 지원자 서류심사 성적 순위, 면접 성적 순위 저장하는 배열 생성

    for _ in range(N):   # 지원자 N명의 성적 입력
         document, interview = map(int, input().split()) # 서류심사 성적 ,면접 성적 입력
         rank[document] = interview # document, interview를 rank에 저장

    top_rank = rank[1] # 순위 비교할 변수, 첫 번째 지원사 순위가 가장 높으므로 저장
    result = 1    # 선발할 수 있는 최대 인원수, 첫 번째 사람은 채용이 가능하므로 1 할당

    for i in range(2, N+1 ):
        if top_rank > rank[i]: #지원자의 순위가 최고 순위보다 높다면
            result += 1    # 선발할 수 있는 인원 수에 추가
            top_rank = rank[i] # 최고 순위에 현재 지원자의 순위 저장

    print(result)  # 결과값 출력

