# 35108 1332
# 3079 입국심사
# 상근이와 친구들이 심사를 받는데 걸리는 최솟값 구하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = []
for _ in range(n):
    time.append(int(input()))

start = min(time)
end = max(time) * m
ans = end

while start <= end:
    mid = (start+end) // 2
    total = 0 # mid 시간동안 감사할 수 있는 총 사람의 수

    for i in range(n):
        total += mid // time[i]

    if total >= m:
        end = mid -1
        ans = min(mid, ans) # 왜하는거지
    else:
        start = mid + 1

print(ans)