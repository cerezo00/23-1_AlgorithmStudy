# 메모리 : 116964, 시간 : 644 (PyPy3)

# 접근법
#   > 한 층씩 회전시킨다.
#   > 1자 모양의 사이클이 생기면 어떻게 해야하나?
# 입력조건
#   > min(N, M) mod 2 = 0  :  1자 모양의 사이클이 생기지 않는다.

import sys

INPUT = sys.stdin.readline


def solution():
    row, col, repeat = map(int, INPUT().split())
    arr = [list(map(int, INPUT().split())) for _ in range(row)]

    # 가장 밖의 첫 번째 층부터 (0층 ~ )
    for layer in range(min(row, col) // 2):
        rotate(arr, layer, repeat)

    print_arr(arr)


def rotate(arr, layer, repeat):
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    dir = 0
    x, y = layer, layer
    tmp = arr[layer][layer + 1]

    cycle = 0
    while cycle < repeat:
        ny = y + dy[dir % 4]
        nx = x + dx[dir % 4]

        if layer > ny or ny >= len(arr) - layer or layer > nx or nx >= len(arr[0]) - layer:
            dir += 1
            continue

        arr[y][x], tmp = tmp, arr[y][x]
        y, x = ny, nx

        # 한 사이클이 끝났다면 cycle 증가
        if x == y == layer:
            tmp = arr[layer][layer + 1]
            cycle += 1


def print_arr(arr):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            print(arr[r][c], end=' ')
        print()


solution()