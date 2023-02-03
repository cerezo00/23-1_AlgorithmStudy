# 2583 영역 구하기
# 메모리 34184 KB, 시간 76 ms
# M*N 모눈, K개 직사각형 -> 직사각형 내부 제외 나머지 부분 영역 개수 / 넓이

import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())
# 크기 M*N, K : 직사각형 개수
arr = [[0]*N for i in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())   # 왼쪽 아래 / 오른쪽 위 꼭짓점 x, y 좌표
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1        # 직사각형 부분은 방문 처리

def bfs(x, y, arr):  # bfs 탐색
    dx = [0, 0, 1, -1]  # x 방향
    dy = [1, -1, 0, 0]  # y 방향
    q = deque()        # 큐 생성
    q.append((x, y))   # 큐에 좌표 추가
    arr[x][y] = 1      # 방문 처리
    area = 1          # 영역 개수 카운트

    while q:
        x, y = q.popleft()
        for i in range(4):  # 상하좌우 확인
            nx = x + dx[i]  # x 방향
            ny = y + dy[i]  # y 방향

            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                # 좌표가 범위 내에 있고 방문 안한 좌표라면 (직사각형 외부)
                arr[nx][ny] = 1  # 방문 처리
                q.append((nx, ny))  # 큐에 추가
                area += 1        # 영역 넓이 + 1
    return area

total_area = []         # 각 영역 넓이 담을 배열
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:  # 방문 안한 직사각형 외부 좌표이면
            total_area.append(bfs(i, j, arr))  # bfs 호출하여 배열에 추가
print(len(total_area))      # 영역의 개수 출력
print(*sorted(total_area))  # 각 영역의 넓이 출력
