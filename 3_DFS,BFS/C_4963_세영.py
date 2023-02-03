#31540	80


import sys

# 다른 문제와 dfs 작동방식은 동일하나, 이 문제에서는 대각선 방향으로 이어져 있어도
# 하나의 연결된 섬으로 보므로 이를 고려하여 dfs를 8번 재귀호출 해준다.
def dfs(x,y):


    if x <= -1 or x >= h or y <= -1 or y >= w:

        return False

    if maps[x][y] == 1:
        maps[x][y] = 2

        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x+1, y + 1)
        dfs(x-1, y - 1)
        dfs(x + 1, y-1)
        dfs(x - 1, y+1)
       
        return True


    return False

# w와 h의 값으로 0이 들어올 때까지
# 지도를 입력받아 maps 배열에 넣고 이 배열의 0,0 부터 dfs를 해나가며
# 섬의 개수인 result를 세어나간다.
while True:
    result = 0
    w, h = map(int,input().split())
    if w == 0 and h==0:
        break
    maps=[]
    for i in range(h):
        maps.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    for i in range(h):
        for j in range(w):
            if dfs(i,j):

                result += 1

    print(result)