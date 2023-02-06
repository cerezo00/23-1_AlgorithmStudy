# 2583 영역 구하기
# 메모리 34176 KB, 시간 72 ms
# 아군 B 파란색, 적군 W 흰색
# N명 뭉치면 N*N 위력 -> 아군 위력의 합 적군 위력의 합 출력

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())    # 전쟁터 가로 * 세로
arr = [list(input()) for _ in range(M)]  # 전쟁터 병사 옷색
B_result = 0                        # 아군 병사의 위력의 합
W_result = 0                        # 적군 병사의 위력의 합

def bfs(x, y, k):                   # 좌표(x, y), 옷 색 k
    dx = [0, 0, 1, -1]  # x 방향
    dy = [1, -1, 0, 0]  # y 방향

    q = deque()
    q.append((x, y))
    arr[x][y] = 1                   # 방문 처리
    count = 1                       # 카운트 1에서 시작 (현재 칸 병사 카운트)
    while q:
        x, y = q.popleft()
        for i in range(4):          # 상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == k:
                # 병사가 범위 내에 있고 옷 색이 k이면
                arr[nx][ny] = 1      # 방문 처리
                q.append((nx, ny))   # 좌표 큐에 추가
                count += 1           # 카운트
    return count**2                  # count**2 반환 (N**2 위력)

for i in range(M):
    for j in range(N):
        if arr[i][j] == "W":             # 옷 색이 W(흰 색이면)
            W_result += bfs(i, j, "W")   # 아군 병사 위력 합에 재귀호출하여 갱신
        elif arr[i][j] == "B":           # 옷 색이 B(청색이면)
            B_result += bfs(i, j, "B")   # 적군 병사 위력 합에 갱신

print(W_result, B_result)                # 출력
