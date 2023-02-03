#34108	140

import sys
from collections import deque

input = sys.stdin.readline

# A, B : 스카이 콩콩의 힘
# N, M : 동규와 주미의 현재 위치 (시작과 도착 위치)
A, B, N, M= map(int,input().split())

# visited : 돌다리 방문 여부 check하는 배열. 
visited = [0] * (100000+1)

# bfs 함수에서 deque 자료구조를 이용하여 주어진 8가지 방법을 골라 M에 도착할 때까지 너비우선탐색을 수행한다.
# 현재 돌다리 위치 x에서 +1, -1, +A, +B, -A, -B, *A, *B 의 8가지 방법을 전부 해보면서 
# 돌다리의 범위를 넘지 않고, 방문하지 않은 돌다리면 현재 방문한 돌다리에 +1을 해주어 값을 업데이트하고 
# q에 next_step을 넣어준다. 
# 위의 과정을 반복하여 M에 도착했을 시 반복문을 멈추고, vitied[M]의 값을 출력한다.
def bfs(x):
    global A,B
    q=deque()
    q.append(x)
    visited[x] = 0

    while q:
        x = q.popleft()
        if x == M:
            break
        for next_step in (x+1,x-1,x+A,x+B,x-A,x-B,x*A,x*B):
            if 0 <= next_step <= M and not visited[next_step]:
                visited[next_step] = visited[x] + 1
                q.append(next_step)
                

bfs(N)

print(visited[M])