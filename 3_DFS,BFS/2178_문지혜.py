# 2178번 미로찾기
# (1,1)에서 (n,m)의 위치로 이동할 때 지나야 하는 최소의 칸 수 구하는 프로그램
from collections import deque #
import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input())))

def bfs(x,y):
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # deque 생성
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치 벗어나면 안됌
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽이므로 진행 불가
            if arr[nx][ny] == 0:
                continue
            # 벽이 아니므로 이동
            if arr[nx][ny] ==1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny)) ## 이거 왜하는거지

    # 마지막 값에서 카운트 값을 뽑는다.
    return arr[n - 1][m - 1]

print(bfs(0, 0))
