# 메모리 : 30616, 시간 100

# 2303 : 숫자 게임

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]
max_units = [0] * n

for i in range(n):
    for pair in combinations(cards[i], 3):
        units = sum(pair) % 10
        if units > max_units[i]:
            max_units[i] = units

result = n - list(reversed(max_units)).index(max(max_units))
print(result)