# 2251 물통
# 메모리 34208 KB, 시간 64 ms
# A, B는 비어있고 C는 가득 차 있는 상태
# A가 비어있을 때 C에 담겨있을 수 있는 물의 양 모두 구하기
# A->B A->C B->A B->C C->A C->B 경우의 수

import sys
input = sys.stdin.readline
from collections import deque

A, B, C = map(int, input().split())
# 부피 A, B, C 물통
visit = [[0] * 201 for i in range(201)] # 방문 체크
result = [0 for i in range(201)]        # 가능한 물의 양 저장

def bfs():
    q = deque()
    q.append([0, 0, C])                 # 처음 A, B 비어있고 C 가득 차 있는 상태

    while q:
        x, y, z = q.popleft()
        if visit[x][y] == 1:           # 이미 방문했으면 넘기기
            continue
        visit[x][y] = 1                # 방문 처리
        if x == 0:                     # A가 비어있으면 옮길 게 없으므로 가능한 물의 양 체크
            result[z] = 1
        if x + y > B:                  # A -> B B가 가득찰 떄까지
            q.append([x + y - B, B, z])
            # A가 빌 떄까지
        else:
            q.append([0, x + y, z])
        if x + z > C:                  # A -> C C가 가득 찰 때까지 
            q.append([x + z - C, y, C])
            # A가 빌 떄까지 
        else:
            q.append([0, y, x + z])
        if y + x > A:                  # B -> A
            q.append([A, y + x - A, z])
        else:
            q.append([y + x, 0, z])
        if y + z > C:                  # B -> C
            q.append([x, y + z - C, C])
        else:
            q.append([x, 0, y + z])
        if z + x > A:                  # C -> A
            q.append([A, y, z + x - A])
        else:
            q.append([z + x, y, 0])
        if z + y > B:                  # C -> B
            q.append([x, B, z + y - B])
        else:
            q.append([x, z + y, 0])

bfs()       # bfs 호출
for i in range(201):
    if result[i] == 1:    # result = 1이면 (A가 비어있는 상태)
        print(i, end=" ") # C 가능한 양 출력
