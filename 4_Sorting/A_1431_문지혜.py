# 1431 시리얼번호

import sys
input = sys.stdin.readline

n = int(input())
def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result += int(i)
    return result

arr = []
for _ in range(n):
    num = input()
    arr.append(num)

arr.sort(key = lambda x:(len(x), sum_num(x), x))

for i in arr:
    print(i)