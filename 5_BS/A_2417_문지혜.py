# 2417 정수제곱근
# 정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램

#31256kb 44ms
import sys
input = sys.stdin.readline

n = int(input())

s = 0
e = n

while s <= e:
    mid = (s + e) // 2
    if mid ** 2 < n:
        s = mid + 1
    else:
        e = mid - 1

print(s)