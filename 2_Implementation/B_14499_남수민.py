# 메모리 : 30616, 시간 : 36

import sys
INPUT = sys.stdin.readline
DY = [1, -1, 0, 0]  # 동서북남
DX = [0, 0, -1, 1]  # 동서북남
UP, DOWN = 0, 1     # 주사위의 상, 하 인덱스


def turn_dice(dir):
    global dice

    # 상, 하, 좌, 우 전, 후
    u, d, l, r, f, b = dice

    if dir == 1:    # 동쪽
        dice = [l, r, d, u, f, b]
    elif dir == 2:  # 서쪽
        dice = [r, l, u, d, f, b]
    elif dir == 3:  # 북쪽
        dice = [b, f, l, r, u, d]
    elif dir == 4:  # 남쪽
        dice = [f, b, l, r, d, u]


n, m, x, y, k = map(int, INPUT().split())
board = [list(map(int, INPUT().split())) for _ in range(n)]
cmd = list(map(int, INPUT().split()))

dice = [0] * 6

for c in cmd:

    # 이동 위치 계산
    nx = x + DX[c - 1]
    ny = y + DY[c - 1]

    # 이동 할 수 없는 위치라면 명령 스킵
    if 0 > nx or nx >= n or 0 > ny or ny >= m:
        continue

    # 이동 및 주사위 회전
    x, y = nx, ny
    turn_dice(c)

    if board[x][y] == 0:
        board[x][y] = dice[DOWN]
    else:
        dice[DOWN] = board[x][y]
        board[x][y] = 0

    print(dice[UP])
