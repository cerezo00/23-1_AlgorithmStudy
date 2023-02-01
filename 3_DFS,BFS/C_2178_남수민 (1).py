# 2178. 미로 탐색
# 34112KB | 68ms

from collections import deque
import sys
input = sys.stdin.readline


def bfs(y, x):
    que = deque()
    que.append((x, y))

    graph[y][x] = 0

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = (x + dx[i], y + dy[i])
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    move[ny][nx] = move[y][x] + 1
                    que.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, str(input()).strip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
move = [[1] * m for _ in range(n)]

bfs(0, 0)

print(move[n-1][m-1])