# 3273 두 수의 합
# 메모리 42176 KB, 시간 92 ms
# ai + aj = x 만족하는 쌍 수
import sys
input = sys.stdin.readline

n = int(input()) # 수열 크기
arr = list(map(int, input().split())) # 수열이 포함하는 수
x = int(input())
arr.sort()  # 오름차순 정렬

i, j = 0, n - 1
count =  0 # 쌍 수 카운트
while i < j:
    if arr[i] + arr[j] <= x:  # x보다 작거나 같으면
        if arr[i] + arr[j] == x: # 같으면 만족하므로
            count += 1           # 카운트
        i += 1  # 작으면 i + 1
    else:      # x보다 크면
        j -= 1 # j -1

print(count) # 개수 출력
