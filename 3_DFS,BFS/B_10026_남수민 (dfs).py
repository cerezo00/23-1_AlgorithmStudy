# 10026 적록색약
# 31168 KB, 60 ms

# DFS
# 1. Visited 체크
# 2. row, col을 하나씩 늘려가며 깊이탐색

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def count_group(graph):
    count = 0

    # 방문하지 않은 좌표를 탐색하여 그룹화 수행
    for r in range(size):
        for c in range(size):
            if not visited[r][c]:
                count += 1
                dfs(r, c, graph[r][c])

    return count


def dfs(row, col, color):
    # 방문 여부 업데이트
    visited[row][col] = True

    # 상하좌우 탐색
    for i in range(4):
        nx = col + dx[i]
        ny = row + dy[i]

        # 재귀 조건
        # 1. Graph 범위 내 위치
        # 2. 방문하지 않음
        # 3. 현재 색과 동일
        if 0 <= nx < size and 0 <= ny < size:
            if not visited[ny][nx]:
                if graph[ny][nx] == color:
                    dfs(ny, nx, color)


# R을 G로 변환하는 함수
def r_to_g():
    for r in range(size):
        for c in range(size):
            if graph[r][c] == 'R':
                graph[r][c] = 'G'


# 상하좌우 (좌상단 부터 0, 0)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

size = int(input())
graph = [list(input()) for _ in range(size)]

# 일반 그룹화
visited = [[False] * size for _ in range(size)]
normal = count_group(graph)

# 색약 그룹화
r_to_g()  # 색약 그래프로 변환
visited = [[False] * size for _ in range(size)]
special = count_group(graph)

print(normal, special)