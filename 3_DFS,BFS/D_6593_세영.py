#34264   140

from collections import deque
import sys
input = sys.stdin.readline

# 3차원 배열을 이용하여 푸는 문제로, 이동 방향이 상,하,동,서,남,북의 3차원이므로 
# x, y, z의 3차원에 대하여 이동 배열을 선언
dx, dy, dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]

# bfs로 풀이, 기존 bfs와 진행 방향은 같으나 3차원 배열이라는 점에서는 차이가 있다.
# q를 생성후 현재 z, y, z의 값을 넣고 방문 배열을 True로 처리 해준다.
# 그리고 while 문에서 q가 빌 때까지 상,하,동,서,남,북 에 대하여 이동을 해보는데 
# 이때 범위와 방문여부를 체크하고, 다음 위치가 '.'익나 'E' 일때만 진행할 수 있으므로
# 이 경우에 대해서만 time배열의 값을 1 증가시키고 q에 이동 위치를 넣은 다음 
# 이동한 위치에 대해서도 방문 처리를 해준다.
def bfs():
   q = deque()
   q.append([sz, sx, sy])
   visited[sz][sx][sy] = True
   while q:
      z, x, y = q.popleft()
      for i in range(6):
         nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
         if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny]:
            if m[nz][nx][ny] == '.' or m[nz][nx][ny] == 'E':
               time[nz][nx][ny] = time[z][x][y] + 1
               q.append([nz, nx, ny])
               visited[nz][nx][ny] = True

# L의 값으로 0이 들어올 때까지 반복해서 수행
# m : 지도 map의 형태를 저장할 배열
# time : 탈출하는데 걸리는 시간을 저장할 배열
# visited : 각 층의 각 위치에 대해 방문 여부를 저장할 배열
# 위의 3가지 배열은 문제에서 제시하는 건물의 구조가 3차원 형태이므로 전부 3차원 배열이다.

while True:
   L, R, C = map(int,input().split())
   if L == 0:
      break
   else:
      m = [[] * R for _ in range(L)]
      time = [[[0] * C for _ in range(R)] for _ in range(L)]
      visited = [[[False] * C for _ in range(R)] for _ in range(L)]
      for i in range(L):
         for j in range(R):
            m[i].append(list(map(str,input())))
         input()
      for k in range(L):
         for i in range(R):
            for j in range(C):
               if m[k][i][j] == 'S':
                  sz, sx, sy = k, i, j
               elif m[k][i][j] == 'E':
                  ez, ex, ey = k, i, j
      bfs()

        # time 배열의 값에 따라 출력을 다르게
      if time[ez][ex][ey]:
         print("Escaped in " + str(time[ez][ex][ey]) + " minute(s).")
      else:
         print("Trapped!")