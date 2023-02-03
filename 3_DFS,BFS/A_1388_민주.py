# 1388 바닥 장식
# 메모리 30748 KB, 시간 36 ms
# 두 개의 '-'가 인접한 같은 행 -> 하나로 취급
# 두 개의 '|'가 인접한 같은 열 -> 하나로 취급

N, M = map(int, input().split())
# 바닥 세로*가로 (N*M)

deck = [list(input()) for _ in range(N)] # 바닥 장식 모양 저장할 배열
cnt = 0  # 필요한 나무 판자 개수 카운트

def dfs(x, y):        # dfs

    if deck[x][y] == '-':   # 바닥 모양이 '-'라면
        deck[x][y] = 1      # 방문 처리
        if y + 1 < M and deck[x][y+1] == '-':  # 양옆 노드가 범위를 벗어나지 않고 - 모양이면
            dfs(x, y+1)      # 재귀 함수 호출

    if deck[x][y] == '|':  # 바닥 모양이 '|'라면
        deck[x][y] = 1     # 방문 처리
        if x+1 < N and deck[x+1][y] == '|':   # 위아래 노드가 범위를 벗어나지 않고 - 모양이면
            dfs(x+1, y)     # 재귀 함수 호출

for x in range(N):
    for y in range(M):
        if (deck[x][y] == '-' or deck[x][y] == '|'): # 방문하지 않은 바닥 장식이 나오면
            dfs(x, y)     # dfs 호출
            cnt += 1      # 카운트

print(cnt)  # 나무 판자 개수 출력

