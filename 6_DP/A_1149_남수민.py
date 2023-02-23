# 1149. RGB거리
# 44ms (76ms)

import sys
input = sys.stdin.readline

num_house = int(input())
rgb_cost = [list(map(int, input().split())) for _ in range(num_house)]

for i in range(1, num_house):
    rgb_cost[i][0] += min(rgb_cost[i-1][1], rgb_cost[i-1][2])
    rgb_cost[i][1] += min(rgb_cost[i-1][0], rgb_cost[i-1][2])
    rgb_cost[i][2] += min(rgb_cost[i-1][0], rgb_cost[i-1][1])

print(min(rgb_cost[-1]))