#34200	64

import sys
from collections import deque
input = sys.stdin.readline

# a, b, c : 물통의 부피
# check : 방문 체크 배열
# ans : 가능한 답 저장 배열
# q : bfs에서 사용할 덱 자료구조, 처음 상태인 0,0,c를 저장

a, b, c = map(int,input().split())
check = [[0]*201 for _ in range(201)]
ans = [0  for _ in range(201)]
q = deque()
q.append([0,0,c])

# a, b, c의 물통에서 옮겨담는 가능한 경우의 수는 
# a -> b, a -> c , b -> a, b -> c, c -> a, c -> b 로 총 6개이다.
# q가 빌때까지 현재 각 통에 담긴 물의 양을 하나씩 빼면서
# 방문한 적있으면 continue로 넘기고
# 없다면 방문 체크를 해준 후 a가 비어있으면 ans[z] 의 값을 1로 해줌 -> a가 비어있을 때 세번째 통에 담겨 있는 물의 양을 저장
# 위의 6가지 경우에 따라 물을 옮겨 주며 q에 물의 용량을 추가해나감

def bfs():
 while q:
        x, y, z = q.popleft()
        if check[x][y] == 1: continue
        check[x][y] = 1
        if x == 0: ans[z] = 1

        if x + y > b: q.append([x + y - b, b, z])
        else: q.append([0, x + y, z])

        if x + z > c: q.append([x + z - c, y, c])
        else: q.append([0, y, x + z])

        if y + x > a: q.append([a, y + x - a, z])
        else: q.append([y + x, 0, z])

        if y + z > c: q.append([x, y + z - c, c])
        else: q.append([x, 0, y + z])

        if z + x > a: q.append([a, y, z + x - a])
        else: q.append([z + x, y, 0])
        
        if z + y > b: q.append([x, b, z + y - b])
        else: q.append([x, z + y, 0])

# bfs 함수를 실행 후 가능한 C 물통의 양을 오름차순으로 출력
bfs()

for i in range(201):
    if ans[i] :
        print(i, end=" ")

