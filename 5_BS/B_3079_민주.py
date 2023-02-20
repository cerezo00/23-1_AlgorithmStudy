# 3079 입국 심사
# 메모리 35108 KB, 시간 1036 MS
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# N : 입국심사대 수 M : 사람 수
T = [int(input()) for _ in range(N)]

start, end = 0, min(T)*M   # 0, 최대 시간
result = 0

while start <= end:
    total = 0 # mid 시간 동안 검사 가능한 사람 수
    mid = (start + end) // 2

    for time in T:          # 걸리는 시간마다
        total += mid // time # mid// 심사대 시간

    if total >= M:       # 사람 수보다 크거나 같으면 심사가 가능하므로
        end = mid - 1    # 더 왼쪽에서 탐색
        result = mid
    else:                # 사람 수보다 작으면 불가능하므로
        start = mid + 1  # 더 오른쪽에서 탐색
print(result) # 최솟값 출력 
