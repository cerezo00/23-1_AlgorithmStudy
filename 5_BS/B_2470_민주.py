# 백준 2470 두 용액
# 메모리 24176 KB, 시간 128 MS
# 산성 양수 알칼리성 음수
# 같은 양의 두 용액을 혼합하여 특성 값이 0에 가장 가까운 용액

import sys
input = sys.stdin.readline

N = int(input()) # 전체 용액 수
arr = list(map(int, input().split())) # 용액 특성값
arr.sort()  # 정렬

start, end = 0, len(arr)-1 # 시작, 끝
result = sys.maxsize

while start < end:
    temp = arr[start] + arr[end] # 두 용액 혼합

    if abs(temp) < result: # result보다 작다면
        result = abs(temp) # 절댓값으로 갱신
        total_result = arr[start], arr[end] # 최종값에 추가
    if result == 0: # 0이 되면 종료
        break
    if temp < 0:    # 음수면
        start += 1  # 시작점 + 1
    else:           # 양수면
        end -= 1    # 끝점 - 1
for i in sorted(total_result):
    print(i, end=' ')          # 두 용액 특성 값 출력
