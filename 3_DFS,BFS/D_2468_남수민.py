# 2468. 안전영역
# 1380ms

import sys
INPUT = sys.stdin.readline
VECTOR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

size = int(INPUT())
graph = [list(map(int, INPUT().split())) for _ in range(size)]

max_num_safe = 0
for h in range(101):
    num_safe = 0
    visitable = [[1] * size for _ in range(size)]

    for r in range(size):
        for w in range(size):
            if graph[r][w] > h and visitable[r][w]:
                num_safe += 1

                visitable[r][w] = 0
                que = [(r, w)]

                while que:
                    y, x = que.pop(0)

                    for dy, dx in VECTOR:
                        ny, nx = y + dy, x + dx

                        if 0 <= ny < size and 0 <= nx < size:
                            if visitable[ny][nx] and graph[ny][nx] > h:
                                visitable[ny][nx] = 0
                                que.append((ny, nx))
    if num_safe > max_num_safe:
        max_num_safe = num_safe

print(max_num_safe)
