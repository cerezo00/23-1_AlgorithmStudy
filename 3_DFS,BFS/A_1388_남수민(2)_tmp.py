def dfs(x,y):
    if graph[x][y] == '-':
        graph[x][y] = 1
        Y = y+1
        if Y < M and graph[x][Y] == '-':
            dfs(x, Y)

    if graph[x][y] == '|':
        graph[x][y] = 1
        X = x + 1
        if X < N and graph[X][y] == '|':
            dfs(X, y)
        
N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]
count = 0

for x in range(N):
    for y in range(M):
        if (graph[x][y] == '-' or graph[x][y] == '|'):
            dfs(x,y)
            count += 1
        
print(count)
        
