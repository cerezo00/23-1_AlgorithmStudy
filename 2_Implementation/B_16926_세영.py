#116856	612 (PyPy3 제출)

import sys
input = sys.stdin.readline

# n , m : n x m 크기
# arr : 배열

n,m,r= map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

# rotate() : 한 번 돌리는 행위를 함수로 선언
# cnt : 한 번 돌릴 때 n과 m중 더 작은 값을 2로 나는 값만큼 돌려준다. 이는 배열이 직사각형 모양일때를 생각하면 된다.
# x, y : 현재 배열에서의 위치 [x][y]

def rotate():

    N, M = n,m
    cnt = min(n,m) // 2
    x, y = 0,0


    while cnt:
        start = arr[x][y]

        for i in range(M-1): #위
            arr[x][y+i] = arr[x][y+i+1]
        
        for i in range(N-1): #오
            arr[x+i][y+M-1] = arr[x+i+1][y+M-1]

        for i in range(M-1): #아래
            arr[x+N-1][y+M-1-i] = arr[x+N-1][y+M-2-i]

        for i in range(N-1): #왼
            arr[x+N-1-i][y] = arr[x+N-2-i][y]
        
        #마지막 값은 처음에 기억해놓은 start값을 넣음
        arr[x+1][y] = start

        #다음 안쪽의 배열을 돌리기 위해 N, M, x, y, cnt의 값을 조정
        N -= 2
        M -= 2
        x += 1
        y += 1
        cnt -= 1

# r만큼 rotate함수를 수행
for i in range(r):
    rotate()

# 돌린 배열을 출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()