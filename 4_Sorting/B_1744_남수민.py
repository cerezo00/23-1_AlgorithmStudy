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

    # 양수 집합 입력
    # 단, 1은 예외처리 : (1 * a) < (1 + a)
    if a > 0:
        if a == 1:
            result += 1
        else:
            array[0].append(a)
    # 음수 집합 입력
    else:
        array[1].append(a)

array[0].sort()
array[1].sort()

# 양수 집합 계산
pn_idx = len(array[0]) - 2
while pn_idx >= 0:
    result += array[0][pn_idx+1] * array[0][pn_idx]
    pn_idx -= 2
# 홀수개 일 경우 남은 하나 처리
if pn_idx == -1:
    result += array[0][0]

# 음수, 0 집합 계산
nn_idx = 1
while nn_idx < len(array[1]):
    result += array[1][nn_idx-1] * array[1][nn_idx]
    nn_idx += 2
# 홀수개 일 경우 남은 하나 처리
if nn_idx == len(array[1]):
    result += array[1][-1]

print(result)