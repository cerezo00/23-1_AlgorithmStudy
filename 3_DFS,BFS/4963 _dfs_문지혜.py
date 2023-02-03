# 4963 섬의 개수
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


# 배열에 있으면 x,y 반대로 읽기
# 특히 y값은 위로 갈수록 작아짐
def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    graph[x][y] = 0  # 탐색을 시작하는 위치 방문 처리..가 맞나?

    # 현재 위치에서 8가지 방향으로 위치 확인
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        # 섬이면서 위치도 안벗어났으면
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:  # 섬이면
                dfs(i, j)
                count += 1

    print(count)

