import copy
import sys
sys.setrecursionlimit(10**6)
N = int(input())
colors = []

result1 = 0
result2=0 

for i in range(N):
    colors.append(list(input()))

colors2 = copy.deepcopy(colors)

for i in range(N):
    for j in range(N):
        if colors2[i][j] == 'G':
            colors2[i][j] = 'R'

def dfs(x,y,color):
    if x <= -1 or x >= N or y <= -1 or y >= N:

        return False

    
    if colors[x][y] == color:
        colors[x][y] = 1
        dfs(x, y + 1,color)
        dfs(x, y - 1,color)
        dfs(x + 1, y,color)
        dfs(x - 1, y,color)
        return True
    return False

def dfs2(x,y,color):
    if x <= -1 or x >= N or y <= -1 or y >= N:

        return False

    
    if colors2[x][y] == color:
        colors2[x][y] = 1
        dfs2(x, y + 1,color)
        dfs2(x, y - 1,color)
        dfs2(x + 1, y,color)
        dfs2(x - 1, y,color)
        return True
    return False




for i in range(N):
    for j in range(N):
        if dfs(i,j,'R')  or dfs(i,j,'G') or dfs(i,j,'B'):
            result1 += 1 

for i in range(N):
    for j in range(N):
        if dfs2(i,j,'R') or dfs2(i,j,'B'):
            result2 += 1



print(result1, result2)
