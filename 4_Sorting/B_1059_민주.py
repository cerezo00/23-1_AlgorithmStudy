# 1059 좋은 구간
# 메모리 31256 KB 시간 44 ms
# [A, B] 구간 사이에 집합 S 원소 속하지 않음
# n을 포함하는 구간 수

import sys
input = sys.stdin.readline

L = int(input())   # 집합 S 크기
arr = list(map(int, input().split())) # 집합에 포함된 정수
n = int(input())   # n을 포함해야 함
arr.sort()         # 오름차순 정렬
if n in arr:
    print(0)
else:
    b, a = 0, 0
    for i in arr:       # n과 가장 가까운 두 수 min max에 넣기
        if n > i:
            a = i
        elif i > n and b == 0:
            b = i
    b -= 1 # 경겟값 포함 x
    a += 1
    result = (n - a) * (b - n + 1) + (b - n)
    print(result)
    # 가능한 경우
    # A가 n보다 작다 -> n보다 작은 수 개수 * n보다 크거나 같은 수 개수
    # A가 n -> n보다 큰 수 개수

