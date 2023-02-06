#dfs 방식 풀이

import sys
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())

# 가로 : N
# 세로 : M
# cnt : 한 영역의 칸 개수
# arr : 전쟁터 정보를 입력받아 저장할 배열
# area1 : 내 병사의 위력을 저장할 배열
# area2 : 적국의 병사의 위력을 저장할 배열

result = 0
cnt = 0
arr = []
area1=[]
area2=[]
for i in range(M):
    arr.append(list(sys.stdin.readline().rstrip()))


# 'W' 와 'B' 중 하나를 입력받아 이와 맞는 영역을 dfs로 탐색
# 영역을 넘지 않으면 arr을 1로 체크하고 cnt를 늘려가며 한 영역의 넓이를 세어나감
# 그리고  상, 하, 좌, 우로 dfs를 재귀적으로 호출하여 탐색하여 True를 리턴

def dfs(y,x,c):
    global cnt

    if x <= -1 or y >= M or y <= -1 or x >= N:

        return False
    if arr[y][x] == c:
        arr[y][x] = 1
        cnt+=1

        dfs(y, x + 1,c)
        dfs(y, x - 1,c)
        dfs(y + 1, x,c)
        dfs(y - 1, x,c)
       
        return True

    return False

# 아군의 병력과 적군의 병력을 각각 탐색하여 cnt*cnt의 값을 
# 각각 area1과 area2에 저장
# 한 칸의 위력을 계산하고 저장할 때마다 cnt는 0으로 초기화
for x in range(N):
    for y in range(M):
        if dfs(y,x,'W'):
            area1.append(cnt*cnt)
            cnt = 0

for x in range(N):
    for y in range(M):
        if dfs(y,x,'B'):
            area2.append(cnt*cnt)
            cnt = 0

# 아군의 병력과 적국의 병력의 합을 출력
print(sum(area1), sum(area2))