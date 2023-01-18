# 1388 바닥 장식
# 메모리 30616 KB, 시간 36 ms
# 두 개의 '-'가 인접한 같은 행 -> 하나로 취급
# 두 개의 '|'가 인접한 같은 열 -> 하나로 취급

N, M = map(int, input().split())
# 바닥 가로*세로 (N*M)

deck = [list(input()) for _ in range(N)] # 바닥 장식 모양 입력
cnt = 0  # 필요한 나무 판자 개수 카운트

def dfs(x, y):        # dfs

    if deck[x][y] == '-':   # 바닥 모양이 '-'라면
        deck[x][y] = 1      # 방문 처리
        Y = y + 1
        if Y < M and deck[x][Y] == '-': # 인접한 같은 행에 '-'가 있다면
            dfs(x, Y)      # 재귀 호출

    if deck[x][y] == '|':  # 바닥 모양이 '-'라면
        deck[x][y] = 1     # 방문 처리
        X = x + 1
        if X < N and deck[X][y] == '|':
            dfs(X, y)     # 재귀 호출

for x in range(N):
    for y in range(M):
        if (deck[x][y] == '-' or deck[x][y] == '|'): # 방문하지 않은 바닥 장식이 나오면
            dfs(x, y)     # dfs 호출
            cnt += 1      # 카운트

print(cnt)  # 나무 판자 개수 출력
