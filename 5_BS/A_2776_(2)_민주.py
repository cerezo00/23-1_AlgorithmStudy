# 2776 암기왕
# 메모리 214396 KB 시간 1624 ms
# 수첩 1 : 실제로 하루 동안 본 정수
# 수첩 2 : 봤다고 주장하는 수
# 수첩 2 작성 순서대로 수첩 1에 있으면 1 없으면 0 출력

import sys
input = sys.stdin.readline
T = int(input())  # 테스트케이스 수

for _ in range(T):
    N = int(input())  # N : 수첩 1 정수 개수
    note1 = set(map(int, input().split()))  # 수첩 1 (중복 제거)
    M = int(input())  # M : 수첩 2 정수 개수
    note2 = list(map(int, input().split())) # 수첩 2
    for num in note2:  # 수첩 2 숫자 순서대로
        if num in note1: # 수첩 1에 있는 숫자이면 
            print(1)     # 1 출력
        else:            # 그렇지 않으면 0 출력 
            print(0)

