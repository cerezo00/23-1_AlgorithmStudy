# 4963. 섬의 개수
# 31256KB, 48ms (76ms)

# 접근법
# 1. 하나의 섬은 육지가 대각선으로 배치될 수 있음
#   > Vector를 대각선을 포함한 8가지를 고려


import sys
input = sys.stdin.readline

result = []


def sol():
    while True:
        w, h = map(int, input().split())

        if not w:
            break

        maps = [list(map(int, input().split())) for _ in range(h)]

        num_island = 0
        vector = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for r in range(h):
            for c in range(w):
                if maps[r][c]:
                    num_island += 1
                    maps[r][c] = 0
                    que = [(r, c)]

                    while que:
                        y, x = que.pop(0)

                        for dy, dx in vector:
                            ny, nx = y + dy, x + dx

                            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                                continue

                            if maps[ny][nx]:
                                maps[ny][nx] = 0
                                que.append((ny, nx))

        result.append(num_island)


sol()
print(*result, sep='\n')
