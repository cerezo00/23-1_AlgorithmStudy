# 1744. 수 묶기
# 40ms

import sys
input = sys.stdin.readline

size = int(input()) # 1 <= N < 50
array = [[], []]  # -1000 <= a <= 1000
result = 0

# array 입력
for i in range(size):
    a = int(input())

    if a > 0:  # 양수 집합
        if a == 1:  # 단, 1은 예외처리 : (1 * a) < (1 + a)
            result += 1
        else:
            array[0].append(a)

    else:  # 음수 집합
        array[1].append(a)

array[0].sort(reverse=True)  # 양수 : 내림차순
array[1].sort()              # 음수 : 오름차순

# 두 개씩 곱하여 합산
for i in range(2):
    index = 1
    while index <= len(array[i]):
        result += array[i][index-1] * array[i][index]
        index += 2
    # 홀수개 일 경우 남은 하나 처리
    if index == len(array[i]):
        result += array[i][-1]

print(result)