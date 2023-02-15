# 2776 암기왕
# 186312kb 6356ms
# `수첩1’에 있으면 1을, 없으면 0을 출력하는 프로그램

import sys
input = sys.stdin.readline


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    # 찾은 경우 중간점의 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

t = int(input())
for _ in range(t):
    n = int(input())
    note_1 = list(map(int, input().split()))
    note_1.sort()
    m = int(input())
    note_2 = list(map(int, input().split()))
    for num in note_2:
        result = binary_search(note_1, num, 0, n-1)
        if result == None:
            print(0)
        else:
            print(1)
