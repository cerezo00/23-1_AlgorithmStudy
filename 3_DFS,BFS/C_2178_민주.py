# 2178 미로 탐색
# 메모리 34128 KB, 시간 80 ms
# N*M 크기 배열 미로 (1 : 이동 가능한 칸 0 : 이동할 수 없는 칸)
# (1,1) 출발 -> (N, M) D위치로 이동하는 최소 칸 수 구하기

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())    # N*M 배열 (미로 크기)
arr = []                            # 미로 칸
for _ in range(N):
    arr.append(list(map(int, input().rstrip()))) # 1:이동 O , 0:이동 X

def bfs(x, y):                     # bfs 탐색
    dx = [-1, 1, 0, 0]             # x 방향
    dy = [0, 0, -1, 1]             # y 방향

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):        # 상하좌우로 검사
            nx = x + dx[i]        # x 방향
            ny = y + dy[i]        # y 방향

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                # 좌표가 범위 내에 있고 이동가능한 칸(1)이면
                arr[nx][ny] = arr[x][y] + 1  # +1 이동
                q.append((nx, ny))           # 큐에 추가

    print(arr[N-1][M-1])         # 도착 시 칸 수 출력

bfs(0,0)      # bfs 호출

