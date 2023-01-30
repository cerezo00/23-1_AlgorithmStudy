# 10026 적록색약
# 메모리 32248KB, 시간 68ms
# 적록색약인 사람이 봤을 때 / 아닌 사람이 봤을 때 구역 수 계산 (N*N)
# 상하좌우 인접한 같은 색은 같은 구역, 적록색약은 적색/녹색 같은 색으로 인식

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    dx = [-1, 0, 1, 0]    # X 방향
    dy = [0, 1, 0, -1]    # Y 방향
    visit[x][y] = 1

    for k in range(4):  # 상하좌우 4방향
        nx = x + dx[k]  # X
        ny = y + dy[k]  # Y

        if 0<=nx<N and 0<=ny<N and space[nx][ny] == space[x][y] and not visit[nx][ny]:
                # 그리드(N*N) 범위 내 + 인접한 칸이 같은 색 + 방문 X 조건 충족 시
                dfs(nx, ny)  # 재귀 호출

N = int(input())    # 그리드 크기 N*N
space = [list(input()) for _ in range(N)] # 색 입력

# 적록색약이 아닌 사람이 봤을 때의 구역의 개수
visit = [[0] * N for _ in range(N)]   # 방문 체크 생성
not_blind = 0 # 적록색약 아닌 사람이 봤을 때 구역 개수 카운트
for i in range(N):
    for j in range(N):
        if not visit[i][j]:  # 방문 안된 좌표라면
            dfs(i, j)        # 재귀 호출
            not_blind += 1   # 구역 개수 카운트

# 적록색약인 사람이 봤을 때의 구역의 수
# 적색과 녹색을 같은 색으로 보므로 G->R로 변환해줌
for i in range(N):
    for j in range(N):
        if space[i][j] == 'G':
            space[i][j] = 'R'

visit = [[0] * N for _ in range(N)] # 방문체크 생성
blind = 0  # 적록색약이 봤을 때 구역의 개수 카운트
for i in range(N):
    for j in range(N):
        if not visit[i][j]:  # 방문 안된 좌표라면
            dfs(i, j)        # 재귀 호출
            blind += 1       # 구역 개수 카운트

print(not_blind, blind)      # 구역 개수 출력
