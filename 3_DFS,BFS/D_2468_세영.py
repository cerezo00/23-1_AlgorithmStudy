#31256   732

import sys

# arr : n X n 의 2차원 배열
# cnt : 안전 영역의 개수
# dx, dy : 방향 이동 배열

n=int(sys.stdin.readline().rstrip())
arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cnt=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# dfs() : stack을 이용하여 dfs 수행
# q 배열 (stack) 을 선언 후 현재 위치인 x,y를 저장
# q가 빌 때까지 x, y를 꺼내면서 dx, dy를 이용하여 상, 하, 좌, 우를 이동 
# 이동한 위치가 배열의 범위를 넘어가지 않고, 방문한적이 없으며 물의 높이보다 위치의 높이가 높으면
# 방문 체크한 후 q에 배열을 추가하여 dfs를 수행
def dfs(x, y, nn):
    q = []
    q.append((x,y))
    while q:
        x,y = q.pop()
        for i in range(0, 4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if(visit[nx][ny]==0 and arr[nx][ny]>nn):
                    visit[nx][ny]=1
                    q.append((nx,ny))

# max(map(max,arr)) -> 2차원 배열에서 최댓값 찾는 코드
# land : 물 높이에 따른 안전 영역의 개수를 저장 
# visited : 방문 체크 배열
# visited 배열을 체크하고, 물높이를 0부터 arr 배열의 최댓값까지 1씩 증가시켜가며
# 방문하지 않았고, 해당 영역의 높이가 물 높이보다 크면 방문 체크하고 dfs함수 수행, land 값을 1씩 증가
# 그리고 현재 land 값이 cnt값보다 크면 cnt 값을 land 값으로 업데이트
for number in range(max(map(max, arr))):
    land=0
    visit = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if visit[i][j]==0 and arr[i][j]>number:
                visit[i][j]=1
                dfs(i, j, number)
                land+=1
    if land>cnt:
        cnt=land


print(cnt)