# 1303. 전쟁 - 전투
# 72ms

VECTOR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

h, w = map(int, input().split())
maps = [list(input()) for _ in range(h)]

power = {'W': 0, 'B': 0}
for row in range(h):
    for col in range(w):
        if maps[row][col]:
            size = 1
            team = maps[row][col]
            maps[row][col] = False
            que = [(row, col)]

            while que:
                y, x = que.pop(0)

                for dy, dx in VECTOR:
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < h and 0 <= nx < w:
                        if maps[ny][nx] == team:
                            size += 1
                            que.append((ny, nx))
                            maps[ny][nx] = False

            power[team] += size ** 2

print(*power.values())