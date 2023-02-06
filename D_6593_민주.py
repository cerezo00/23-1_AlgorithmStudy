# 6593 상범 빌딩
# 메모리 34184 시간 120
# 막힌 칸 '#', 비어있는 칸 '.'
# 탈출하는데 걸리는 시간

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visit = [[[0] * C for _ in range(R)] for _ in range(L)] # 최단 시간 체크
    visit[start_L][start_R][start_C] = 1   # 방문처리
    q = deque([(start_L, start_R, start_C)])  # 시작점에서 큐
    dx = [-1, 1, 0, 0, 0, 0]   # x 방향
    dy = [0, 0, -1, 1, 0, 0]   # y 방향
    dz = [0, 0, 0, 0, -1, 1]   # z 방향
    while q:
        l, r, c = q.popleft()
        for i in range(6):  # 동서남북상하
            nl = l + dx[i]  # x
            nr = r + dy[i]  # y
            nc = c + dz[i]  # z

            if not (0 <= nl < L and 0 <= nr < R and 0 <= nc < C): # 범위 벗어나면 넘기기
                continue
            if visit[nl][nr][nc] != 0:     # 방문한 곳이면 넘기기
                continue
            if arr[nl][nr][nc] == "#":     # 지나갈 수 없다면 넘기기
                continue
            if arr[nl][nr][nc] == "E":     # 출구이면
                print("Escaped in {} minute(s).".format(visit[l][r][c])) # 출력
                return
            visit[nl][nr][nc] = visit[l][r][c] + 1 # 지나갈 수 있다면 시간 +1 추가
            q.append((nl, nr, nc))         # 좌표 추가

    print("Trapped!")   # 불가능하면 Trapped! 출력

while True:
    L, R, C = map(int, input().split())
    # L : 빌딩 층수 R, C : 한 층의 행/열
    if L == 0 and R == 0 and C == 0:          # 0 0 0 이면 종료
        break
    arr = []                                  # 빌딩 칸
    # 시작 지점 S, 출구 E
    # 지나갈 수 없는 칸 #, 비어있는 칸 .

    for l in range(L):
        arr.append([list(input().rstrip()) for _ in range(R)])  # 칸 입력
        for r in range(R):
            for c in range(C):
                if arr[l][r][c] == "S":      # S면 시작 지점
                    start_L, start_R, start_C = l, r, c  # 시작 값 저장
        input()
    bfs()  # bfs 호출
