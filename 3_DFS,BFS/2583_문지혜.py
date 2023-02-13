# 2583 영역 구하기
#  직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지,
#  그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력

## 왜자꾸 틀리는거지ㅜㅜ??
import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경
input = sys.stdin.readline


def dfs(y,x):
    graph[y][x] = 1 # 방문 처리
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0: # 빈곳이면
            dfs(ny, nx)
            cnt += 1

# 입력
m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)] # 0으로 초기화한 배열 생성
# graph에 직사각형 그리기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1 # 직사각형을 1로 채워준다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

for y in range(m):
    for x in range(n):
        cnt = 1
        if graph[y][x] == 0: # 빈곳이므로 result에 추가해줘야함
            dfs(y, x)
            result.append(cnt)



print(len(result))
print(*sorted(result))