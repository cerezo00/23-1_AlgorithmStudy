# 7795 먹을 것인가 먹힐 것인가
# 메모리 34848KB, 시간 160 ms
# A의 크기가 B보다 큰 쌍 구하기

import sys
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수
for _ in range(T):
    N, M = map(int, input().split())  # N : A 수, M : B 수
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    count = 0 # 쌍의 개수
    A_index, B_index = 0, 0 # A, B 인덱스
    while A_index < N and B_index < M:  # A, B 인덱스가 각각 범위 내
        if A[A_index] > B[B_index]:     # A > B 이면 가능하므로
            B_index += 1                # B 인덱스 + 1
        else:
            A_index += 1                # 불가능이므로
            count += B_index            # B 인덱스 갱신
    if B_index == M: # B 인덱스가 M이 되면 확인이 끝났으므로
        count += B_index * (N - A_index) # A에 남은 인덱스들은 모두 B보다 크므로 더해줌
    print(count) # 쌍의 개수 출력
