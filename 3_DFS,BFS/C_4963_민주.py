# 4963 섬의 개수
# 메모리 34176 KB, 시간 76 ms
# 섬의 개수 세기
# 1 : 땅, 0 : 바다

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):  # bfs 탐색
    dx = [1, -1, 0, 0, 1, -1, 1, -1]  # x 방향
    dy = [0, 0, 1, -1, -1, 1, 1, -1]  # y 방향
    q = deque()        # 큐 생성
    q.append((x, y))   # 큐에 좌표 추가

    while q:
        x, y = q.popleft()
        for i in range(8):  # 상하좌우대각선 확인
            nx = x + dx[i]  # x 방향
            ny = y + dy[i]  # y 방향

            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                # 좌표가 범위 내에 있고 땅(1)이면 같은 섬
                arr[nx][ny] = 0  # 방문 처리
                q.append((nx, ny))  # 큐에 추가

while True:
    w, h = map(int, input().split())  # 너비, 높이
    if w == 0 and h == 0:             # 0 0 입력 받으면 종료
        break
    arr = []                          # 지도 저장
    for _ in range(h):
        arr.append(list(map(int, input().split())))  # 1은 땅, 0은 바다
    count = 0                         # 섬 개수 카운트
    for i in range(h):                # w*h 크기에서
        for j in range(w):
            if arr[i][j] == 1:        # 땅이면
                bfs(i, j)             # 재귀호출
                count += 1            # 섬의 개수 카운트
    print(count)                      # 출력

