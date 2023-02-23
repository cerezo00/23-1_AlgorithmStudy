# 1932. 정수 삼각형
# 132ms (non-max 112ms)

import sys
input = sys.stdin.readline

size = int(input())
nums = [list(map(int, input().split())) + [0] for _ in range(size)]

for h in range(1, size):
    for i in range(len(nums[h]) - 1):
        nums[h][i] += max(nums[h-1][i-1], nums[h-1][i])

print(max(nums[-1]))