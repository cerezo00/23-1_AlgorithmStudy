# 15686. 치킨 배달

import sys
input = sys.stdin.readline


def backtrack(cur_store_idx, num_chosen):
    global min_ch_dist

    if num_chosen == max_store:
        ch_dist = 0
        for hy, hx in house_pos:
            ch_dist += min(abs(hy - sy) + abs(hx - sx) for sy, sx in chosen_store_pos)
        min_ch_dist = min(min_ch_dist, ch_dist)

    for i in range(cur_store_idx, len(store_pos)):
        chosen_store_pos.append(store_pos[i])
        backtrack(i + 1, num_chosen + 1)
        chosen_store_pos.pop()

# size := 지도의 크기
# max_store := 선택할 매장의 수
# maps := 지도 행렬
size, max_store = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(size)]

house_pos = []
store_pos = []
for row in range(size):
    for col in range(size):
        if maps[row][col] == 1:
            house_pos.append((row, col))
        elif maps[row][col] == 2:
            store_pos.append((row, col))

chosen_store_pos = []       # chosen_store := 현재 선택된 매장의 좌표 (임시)
min_ch_dist = float('inf')  # min_ch_dist := 최소 치킨거리

backtrack(0, 0)

print(min_ch_dist)
