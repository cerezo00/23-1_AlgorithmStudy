# 6593. 상범 빌딩
# 00ms

import sys
input = sys.stdin.readline
vector = ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))

while True:
    L, R, C = map(int, input().split())
    if not L:
        break

    maps = [[list(str(input()).rstrip()) for _ in range(R + 1)][:-1] for _ in range(L)]

    # 시작지점 찾기
    S = 0
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if maps[l][r][c] == 'S':
                    S = (l, r, c)
                    break

    # 너비탐색 시작
    que = [S]
    time = 0
    find = False
    while que:
        que_ = []
        time += 1

        for z, y, x in que:
            # 탈출구 발견시 2중 반복문 탈출
            if find:
                break

            for dz, dy, dx in vector:
                nz, ny, nx = z + dz, y + dy, x + dx

                if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C:
                    # 이동 가능할 경우 이동
                    if maps[nz][ny][nx] == '.':
                        maps[nz][ny][nx] = 'V'
                        que_.append((nz, ny, nx))

                    # 탈출구 발견시 2중 반복문 탈출
                    elif maps[nz][ny][nx] == 'E':
                        que, que_ = [], []
                        find = True
                        break

        que = que_

    if find:
        print(f'Escaped in {time} minute(s).')
    else:
        print('Trapped!')