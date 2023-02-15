# 2776 암기왕
# 메모리 185296 KB 시간 5504 ms
# 수첩 1 : 실제로 하루 동안 본 정수
# 수첩 2 : 봤다고 주장하는 수
# 수첩 2 작성 순서대로 수첩 1에 있으면 1 없으면 0 출력

import sys
input = sys.stdin.readline

def binary_search(arr, k):
    start, end = 0, len(arr) - 1  # 시작점, 끝점
    while start <= end:
        mid = (start + end) // 2  # 중간지점 값
        if arr[mid] == k:         # 중간지점 = 찾는 수
            return 1              # 1 반환
        elif arr[mid] > k:        # 중간지점 > 찾는 수 -> 수가 더 왼쪽에 있으므로
            end = mid - 1         # 끝점 = 중간 - 1
        else:                     # 중간지점 < 찾는 수 -> 수가 더 오른쪽에 있으므로
            start = mid + 1       # 시작점 = 중간 + 1
    return 0

T = int(input())  # 테스트케이스 수

for _ in range(T):
    N = int(input())  # N : 수첩 1 정수 개수
    note1 = list((map(int, input().split()))) # 수첩 1
    note1.sort() # 정렬
    M = int(input())  # M : 수첩 2 정수 개수
    note2 = list(map(int, input().split())) # 수첩 2
    for num in note2: # 수첩 2 숫자 순서대로
        print(binary_search(note1, num)) # 이진탐색하여 출력



