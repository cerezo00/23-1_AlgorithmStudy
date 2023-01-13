#147056KB	3808ms

import sys
input = sys.stdin.readline

# n * m : 연구소의 크기
# arr : 초기 연구소 맵을 저장할 배열
# tmp : 벽을 설치한 후의 맵을 저장할 배열
# answer : 안전 영역의 최대 크기
# dx, dy : 상, 하, 좌, 우의 4가지 방향에 대한 배열

n,m=map(int,input().split())
arr = []
tmp = [[0]*m for _ in range(n)]
answer = 0

for i in range(n):
    arr.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 바이러스를 가능한 방향으로 계속해서 퍼뜨려 나가는 함수로,
# dx, dy를 이용하여 바이러스가 퍼질 수 있는 경우에 한해
# 현재 배열의 값을 2로 바꾸고 그 자리에서 재귀적으로 바이러스를 퍼뜨려 나간다.
def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx <n and ny >= 0 and ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx,ny)

# 현재 맵에서의 안전 영역의 개수를 계산하는 함수로,
# 현재 배열의 값이 0이면 안전 영역이므로 이 영역의 개수를 구해 리턴한다.
def get_result():
    result = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] ==0:
                result += 1
    return result

# dfs를 이용해 울타리를 설치해가면서 (모든 가능할 경우의 수를 다 따져가며 울타리를 설치해 보는 것이다.) 
# 이 울타리 설치의 경우의 안전 영역의 개수를 계산해나간다.
# 만약 현재 울타리를 설치할 경우가 저장되어 있는 answer의 값보다 크다면 그 값으로 answer를 업데이트 해 나간다
def dfs(cnt):
    global answer
    # 울타리 설치가 3개가 완료된 경우 현재 맵 상태를 저장
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = arr[i][j]
        # 울타리 설치 후 그 상태에서 바이러스를 전파 시키고
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i,j)
        #전파가 완료된 상태에서 안전 영역의 개수를 구해 현재 answer의 값과 비교해 더 큰 값으로 업데이트 해 나간다.
        answer = max(answer,get_result())
        return
    # 울타리의 개수가 3이 아니라먄 울타리를 계속 설치해 나가야 하므로
    # 빈공간에 울타리를 설치해 준다.
    for i in range(n):
        for j in range(m):
            if arr[i][j] ==0:
                arr[i][j]  = 1 
                cnt += 1
                dfs(cnt)
                arr[i][j] = 0
                cnt -= 1


dfs(0)
print(answer)