#31604KB	88ms

import sys
input = sys.stdin.readline

# h : 2차원 세계의 세로 길이
# w : 2차원 세계의 가로 길이
# blocks : 블록이 쌓인 높이가 저장된 배열
# arr : h * w 크기의 2차원 세계(배열)
# check : block이 막혀있는지 체크할 bool 변수
# result : 고이는 빗물의 총량 

h,w= map(int, input().split())
blocks = list(map(int, input().split()))
arr = [[0]*w for _ in range(h)]
check = False
result = 0

# 블럭이 쌓여있는 공간을 2차원 세계에 1로 표시
for i in range(w):
    for j in range(blocks[i]):
        arr[h-j-1][i] = 1

# 블록이 쌓여있는 2차원 세계에서 아래층부터 한 줄 한 줄 고일 수 있는 부분을 체크해가면서 고이는 빗물의 양을 카운트한다.
# 한 층에서 고인 빗물의 값을 저장할 tmp 변수를 선언하여 다음 줄로 올라갈 때마다 0으로 초기화 해준다.
# 블록이 양쪽으로 막혀있어야 그 가운데에 빗물이 고일 수 있므으몰 check 변수도 다음 줄로 올라갈 때마다 False로 초기화 해준다.
# 안쪽의 반복문에서 한 줄마다 고이는 물의 양을 체크하게 되는데, w의 길이동안 1칸씩 이동하면서 블록을 만나면, 즉 2차원 세계 배열의 값이 1이면
# 현재 check 변수의 값을 확인한다. 블록을 만났는데 현재 check의 값이 False라면 지금부터 다음 블록을 만날 때까지 빗물이 고일 수 있으므로 check변수의 값을 True로 바꿔준다.
# 만약 현재 칸의 값이 0이라면 벽이 아닌 부분이므로 빗물이 고일 수 있다. 하지만 현재 위치에서 왼쪽에 블록이 없다면 고일 수 없는 환경이므로 check 변수의 값을 확인하여
# True일 때만 tmp의 값을 1 증가시킨다.
# 그리고 현재 값이 1이고, 즉 블록을 만났을 때 check 변수가 True라면 한 블록과 한 블록의 쌍이 만들어 졌다는 것이고, 이는 그 사이에 물이 고일 수 있다는 것이므로
# 그 사이에 고인물이 저장되어 있는 tmp값을 result에 더해주고 tmp값을 다시 0으로 초기화 해준다.
# 위의 체크 과정을 반복해 빗물이 고일 수 있는 환경을 체크하여 한 줄 한 줄 고인 빗물의 칸 수를 result에 저장해주면 된다. 
for i in reversed(range(h)):
    tmp = 0
    check = False
    for j in range(w):
        if( arr[i][j] == 1 and check == False):
            check = True
        elif (arr[i][j]== 0 and check == True):
            tmp += 1
        elif ( arr[i][j] == 1 and check == True):
            result += tmp
            tmp = 0 
        else:
            continue
print(result)
