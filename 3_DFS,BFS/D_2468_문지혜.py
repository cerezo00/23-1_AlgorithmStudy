# 2468 안전 영역
# 장마철에 내리는 비의 양에 따라 일정 높이 이하의 모든 지점은 물에 잠긴다.
# 장마철에 물에 잠기지 않는 안전한 영역의 최대 가수

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph=[]
max_num = 0
result = 1
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 지역의 높이를 리스트로 입력받으면서 가장 큰 값을 찾음.
for i in range(n):
    low = list(map(int,input().split()))
    graph.append(low)
    for j in low:
        if j > max_num:
            max_num = j

def dfs(x,y,num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
            if graph[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx,ny,num)

for i in range(max_num):
    visited=[[0]*n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k]==0:
                cnt+=1
                visited[j][k] = 1
                dfs(j,k,i)
    result = max(result, cnt)

print(result)
