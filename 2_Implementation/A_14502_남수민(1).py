import sys
from collections import deque

input = sys.stdin.readline

# 방향 벡터 : 0(오른쪽), 1(왼쪽), 2(위쪽), 3(아래쪽)
DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


# 모든 좌표에 대해 3개의 벽을 세우는 DFS 함수
# 3개의 벽 위치 -> 가능한 바이러스의 최댓값
def build_wall_dfs(num_wall):

    # 벽을 모두 세웠다면 바이러스 전파
    if num_wall == 3:
        spred_virus()
        return

    # 모든 좌표에 대하여 벽을 한 개씩 세워보며 깊이탐색
    for i in range(height):
        for j in range(width):
            if graph[i][j] == 0:
                graph[i][j] = 1
                build_wall_dfs(num_wall + 1)
                graph[i][j] = 0


# 바이러스가 전파지대의 넓이를 계산하는 함수
# min 함수를 통해 최솟값 업데이트
def spred_virus():

    global min_virus

    # num_virus := 바이러스가 전파된 좌표 수
    # visited := 각 좌표의 바이러스 전파 여부
    num_virus = 0
    visited = [[0] * width for _ in range(height)]

    # pos_virus := 바이러스의 좌표 목록 (양방향 큐)
    pos_virus = deque()
    for h in range(height):
        for w in range(width):
            if graph[h][w] == 2:
                visited[h][w] = 1
                pos_virus.append((h, w))

    # 각 바이러스에 대하여 전파 시작
    while pos_virus:
        # x, y := # 바이러스의 좌표
        x, y = pos_virus.popleft()

        # 각 바이러스의 상하좌우에 대하여 전파
        for dir in range(4):
            nx = x + DX[dir]
            ny = y + DY[dir]

            # 아래 조건을 만족하면 바이러스 전파
            # 조건 1. 전파 위치는 맵을 벗어나지 않는다
            # 조건 2. 전파 위치에 도달한 적이 없다
            # 조건 3. 전파 위치는 안전지대이다
            if 0 <= nx < height and 0 <= ny < width:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 1         # 방문 위치 추가
                    pos_virus.append((nx, ny))  # 바이러스 목록 추가
                    num_virus += 1              # 바이러스 수 증가

    # 바이러스지대의 최솟값 업데이트
    min_virus = min(min_virus, num_virus)


# 맵의 세로, 가로 길이
height, width = map(int, input().split())

# graph := 맵의 지도
graph = []
for _ in range(height):
    graph.append(list(map(int, input().split())))

# min_virus := 바이러스의 최솟값
min_virus = height * width

# 알고리즘 시작
build_wall_dfs(0)

# num_safe := 안전지대의 넓이 = 최초 안전지대의 넓이 - 바이러스 전파지대의 넓이 - 벽의 개수
num_safe = sum(graph[i].count(0) for i in range(height)) - min_virus - 3

print(num_safe)
