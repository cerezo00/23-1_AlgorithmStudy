# 42176 132

# 2470 두 용액
# 0에 가장 가까운 용액을 만들어내는 두 용액 찾기

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
start = 0
end = n-1

ans = abs(arr[start] + arr[end])
final = [arr[start], arr[end]]

while start < end :
    left = arr[start]
    right = arr[end]

    total = left + right
    if abs(total) < ans:
        ans = abs(total)
        final = [left, right]
        if ans == 0:
            break
    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
    if total < 0:
        start += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
    else:
        end -= 1
print(final[0],final[1])