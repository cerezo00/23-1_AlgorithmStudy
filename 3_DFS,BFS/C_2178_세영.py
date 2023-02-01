#32452	104

from collections import deque
import sys
input = sys.stdin.readline

# n x m 크기의 미로판
# graph : 미로판 좌표를 저장할 배열

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

# dx, dy : 방향 배열
dx = [-1,1,0,0]
dy=[0,0,-1,1]

# bfs를 이용하여 미로를 빠져나감
# deque 자료구조를 사용하여 queue에 현재 좌표를 넣어가며
# queue가 빌 때까지 dx, dy를 이용하여 이동해나간다.
# 좌표가 미로를 벗어나거나 현재 위치의 배열값이 0이면 이동할 수 없는 것이므로 continue로 넘기고
# 1인 경우에만 현재 위치에 지금까지 걸음수에 +1을 해나가면서 현재 위치까지 오기까지 지나야하는 칸 수 를 저장해간다.
# 마지막에 (n, m)의 배열값을 리턴하여 출력한다.
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))