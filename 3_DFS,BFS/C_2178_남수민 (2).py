# 2178. 미로 탐색
# 30616KB | 44ms

import sys
INPUT = sys.stdin.readline
VECTOR = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(y, x):
    step = 1         # step := 이동 거리
    que = [(y, x)]   # que := 좌표 대기열

    graph[y][x] = 0  # 방문 여부 업데이트

    # (n, m)에 도착할 때까지 반복
    while graph[n-1][m-1]:
        step += 1  # step 업데이트

        que_ = []  # que_ := 다음 Step 큐 그룹

        # 큐의 좌표에 대하여, 상하좌우 탐색
        for y, x in que:
            for dx, dy in VECTOR:
                nx, ny = x + dx, y + dy

                # 조건 1. 맵의 범위 내에 위치
                # 조건 2. 해당 위치로 이동 가능
                if 0 <= nx < m and 0 <= ny < n:
                    if graph[ny][nx] == 1:
                        graph[ny][nx] = 0      # 방문 여부 업데이트
                        que_.append((ny, nx))  # 다음 Step 큐 그룹에 추가

        # 새로운 큐 그룹으로 While 반복
        que = que_

    return step


n, m = map(int, INPUT().split())
graph = [list(map(int, str(INPUT()).strip())) for _ in range(n)]

print(bfs(0, 0))