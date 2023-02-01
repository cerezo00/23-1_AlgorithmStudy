#32484	72

import sys
sys.setrecursionlimit(10**6)

# M x N 크기의 모눈종이
# K : 모눈종이에 칠해진 직사각형들의 개수
# arr : 모눈종이 좌표를 저장할 배열
# result : 분리되어 나누어지는 영역의 개수
# cnt : 각 영영의 넓이, 즉 모눈종이 한 칸의 개수를 카운트하는 변수
# rects : 직사각형들의 꼭짓점 좌표값을 저장할 배열
# area : 각 영역들의 넓이를 저장할 배열

M,N,K=map(int,input().split())
arr=[[0]*M for _ in range(N)]
result = 0
cnt = 0
rects = []
area=[]

# 직사각형들의 꼭짓점 좌표를 입력받아 rects에 저장
for i in range(K):
    rects.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 직사각형의 꼭짓점 좌표를 이용하여 모눈종이 배열에 직사각형 부분은 2로 색칠
for x1,y1,x2,y2 in rects:
    for i in range(y2-y1):
        for j in range(x2-x1):
            arr[x1+j][y1+i]=2


# 직사각형이 아닌 영역의 부분을 dfs를 이용하여 탐색해나가는데 이떼 아닌 부분을 탐색할 때마다 cnt를 1씩 증가시켜 
# 영역의 크기를 구함

def dfs(x,y):
    global cnt

    if x <= -1 or x >= N or y <= -1 or y >= M:

        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        cnt+=1

        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
       
        return True


    return False

#dfs 함수를 활용하여 영역의 개수를 구ㅎㅏ면서 cnt의 값을 area 배열에 저장해나감
for i in range(M):
    for j in range(N):
        if dfs(j,i):
            result += 1
            area.append(cnt)
            cnt = 0

# 영역의 개수롸 정렬한 area 배열의 원소 값을 출력 
print(result)
area.sort()
print(*area)