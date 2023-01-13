## 14502 연구소
# 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다.
# 새로 새울 수 있는 벽의 개수는 3개, 꼭 3개를 세워야한다.
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
# 안전 영역 크기의 최댓값을 구하는 프로그램
from collections import deque
import copy

# 상하좌우 인접한 빈칸으로 이동하므로 bfs를 사용
# 바이러스 위치를 전부 큐에 넣고 while queue를 돌린다.
# 벽 3개 세운 후 바이러스를 퍼트려서 0이 몇개 있는지 check


# bfs : 바이러스를 퍼트리고 안전영역 크기 재기
# 바이러스는 상하좌우로 이동하므로 d라는 변수 생성
# 큐를 만든다음, 테스트할 map을 <<깊은 복사>> 해준다. 2(바이러스)가 위치한 곳을 큐에 넣어준다.
# lab을 그대로 사용할 경우 바이러스 이동시 0을 2로 변경할텐데 다시 0으로 되돌릴 수 없어서 테스트용 맵을 만들어야만 함
# 상하좌우 좌표 생성 후 좌표값이 영역 내부인지, 0인지 체크한 다음 testmap[dr][c] 를 2로 바꿔주고, 큐에 좌표를 넣어준다.
d = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    queue = deque()
    # queue에 2의 위치를 전부 append
    test_map = copy.deepcopy(lab)
    for i in range(n):
        for k in range(m):
            if test_map[i][k] ==2 :
                queue.append((i,k))
    while queue:
        r,c = queue.popleft() # 큐에 가장 앞에 있는 값을 r,c로 지정

        for i in range(4): # 상하좌우 이므로 반복문 4번 돈다 ..?
            dr = r + d[i][0]
            dc = c + d[i][1]
            if (0<=dr<n) and (0<=dc<m):
                if test_map[dr][dc] == 0:
                    test_map[dr][dc] =2
                    queue.append((dr,dc))

    global result
    count = 0 # 수 세기
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 0:
                count += 1

    result = max(result, count)

def make_wall(count):
    if count ==3: ## count 가 3인지 체크하고 3이면 bfs를 호출한다.
        bfs()
        return
    for i in range(n):
        for k in range(m): # 0을 만날 때마다 지도의 값을 1로 변경(벽)
            if lab[i][k] == 0:
                lab[i][k] = 1
                make_wall(count+1) ##  make wall을 재귀호출하면서 count를 1 증가시킨다.
                lab[i][k] = 0 ## 밖으로 나왔을 땐 다시 빈칸으로 만들어준다.


n, m= map(int,input().split()) # 지도의 세로, 가로
lab = [list(map(int,input().split())) for _ in range(n)]

result = 0
make_wall(0)
print(result)