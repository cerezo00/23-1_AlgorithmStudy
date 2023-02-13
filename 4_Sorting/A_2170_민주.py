# 2170 선 긋기
# 메모리 238760 KB 시간 4284 ms
# 선 긋기 -> 총 길이 (겹치기 가능)
# 겹치는 부분에서 x, y 갱신

import sys
input = sys.stdin.readline

N = int(input())   # 선을 그은 횟수
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()  # 두 점의 위치

start = arr[0][0]  # 처음 두 점 위치 (start, end)
end = arr[0][1]
result = 0

if len(arr) > 1:
    for x, y in arr[1:]: # 시작점 제외 1부터 x, y 좌표 비교
        if end < y:      # 현재 좌표의 y값이 기준 좌표보다 크면 이을 수 있으므로
            if end < x:  # 현재 좌표의 x값이 기준 좌표보다 크면 겹치지 않으므로
                result += end - start  # 기준 두 점 길이 계산하여 result에 갱신
                start = x # 기준값 x 갱신
            end = y  # 기준값 y 갱신
    result += end - start  # 다 돌고나서 기준점 계산하여 갱신
else:
    result += end - start  # 좌표 하나면 result에 갱신

print(result) # 출력
