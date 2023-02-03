# 10451 순열 사이클
# 메모리 31348 KB, 시간 440 ms
# 순열 -> 사이클 개수 계산 
# 1부터 N까지 방문 체크 -> 방문 다음 수도 방문 X 상태이면 방문 -> 방문 시 + 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(k):          # DFS 탐색
    visit[k] = 1     # 방문 처리
    num = arr[k]     # 다음 방문 저장
    if visit[num] == 0:  # 방문 안한 상태이면 (방문 가능)
        dfs(num)     # 재귀 호출

T = int(input())     # 테스트 케이스 개수 입력
for _ in range(T):
    N = int(input()) # 순열의 크기
    arr = [0] + list(map(int, input().split())) # 순열 입력
    visit = [0] * (N+1)  # 방문 체크
    result = 0  # 순열 사이클의 개수

    for i in range(1, N+1):
        if visit[i] == 0:  # 방문 안한 상태이면
            dfs(i)         # DFS 호출
            result += 1    # 사이클 개수 + 1
    print(result)          # 출력
