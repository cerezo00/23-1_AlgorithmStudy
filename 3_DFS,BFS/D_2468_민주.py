# 2468 안전 영역
# 메모리 35108 시간 1736

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(x, y, height):
    dx = [0, 0, -1, 1]   # x방향
    dy = [1, -1, 0, 0]   # y방향

    for i in range(4):   # 상하좌우 확인
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
            # 범위 내에 있고 방문 안한 지점이면
            if arr[nx][ny] > height:  # 일정 높이 height보다 크면 잠기지 않으므로
                visit[nx][ny] = 1     # 방문 처리
                dfs(nx, ny, height)   # 재귀호출

N = int(input())    # 행/열 크기
arr = []            # 칸별 높이
max_height = 0      # 최고 높이
result = 1          # 모두 잠기지 않을 수 있으므로 1 

for _ in range(N):
    num = list(map(int, input().split()))  # 칸별 높이 입력
    arr.append(num)
    for i in num:
        if i > max_height:
            max_height = i   # 입력 값 중 최고 높이 찾기

for i in range(max_height): # 최고 높이만큼 루프 (비의 범위)
    visit = [[0]*N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if arr[j][k] > i and visit[j][k] == 0: # 현재 루프 높이보다 크고 방문 안한 지점이면
                count += 1       # 영역 추가
                visit[j][k] = 1  # 방문 처리
                dfs(j, k, i)     # dfs
    result = max(result, count)  # 현재 영역 수와 이전 강수량 수치에서의 영역 수를 비교하며 큰 값 result에 저장
print(result)    # 최대 안전영역 수 출력 

