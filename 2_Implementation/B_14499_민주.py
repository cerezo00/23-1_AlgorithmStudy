# 14499 주사위 굴리기
# 메모리 30616 KB, 시간 40ms

import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
# N : 지도의 세로 크기, M : 가로 크기
# (x, y) : 주사위를 놓은 곳의 좌표
# K : 명령의 개수

arr = []   # 지도에 쓰여있는 수
for i in range(N):
    arr.append(list(map(int, input().split())))  # 지도에 쓰여 있는 수 입력
order = list(map(int, input().split()))    # 주사위 굴릴 방향 순서대로 입력
# 동 서 북 남
dx = [0, 0, -1, 1]    # 이동 방향 x
dy = [1, -1, 0, 0]    # 이동 방향 y

dice = [0 for _ in range(6)]  # 주사위 (' ', 위, 앞, 우, 좌, 뒤, 아래)
# dice[0] = 위, dice[5] = 바닥
for i in range(K):
    dir = order[i]
    nx = x + dx[dir-1]   # 이동 위치 X
    ny = y + dy[dir-1]   # 이동 위치 Y

    if not 0 <= nx <= N-1 or not 0 <= ny <= M-1:    # 지도 범위를 벗어나면 명령 건너뛰기
        continue
    x, y = nx, ny

    # 주사위 회전, 이동 (동 - 서 - 북 - 남)

    if dir == 1: # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 2: # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3: # 남
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:         # 북
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if arr[nx][ny] == 0:      # 칸에 쓰인 수가 0이면
        arr[nx][ny] = dice[5]   # 칸에 주사위 바닥 수 복사
    else:                     # 0이 아닌 경우
        dice[5] = arr[nx][ny]   # 칸에 쓰인 수를 바닥면에 복사
        arr[nx][ny] = 0         # 칸에 쓰인 수는 0이 됨

    print(dice[0])  # 주사위 윗면에 쓰인 수 출력
