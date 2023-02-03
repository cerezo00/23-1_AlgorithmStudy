# 2583. 영역 구하기
# 31256KB, 48ms

# 접근법
# 1. 주어진 사이즈의 그리드 행렬 선언 (True로 초기화)
# 2. 그리드에 입력받은 사각형을 False로 표시
# 3. True인 영역에 대하여 BFS 수행


import sys
input = sys.stdin.readline


def bfs(y, x):
    area = 1            # 넓이 초기화
    que = [(y, x)]      # 큐에 삽입
    grid[y][x] = False  # 방문 체크
    vec = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while que:
        y, x = que.pop(0)

        for dy, dx in vec:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if grid[ny][nx]:
                    que.append((ny, nx))
                    grid[ny][nx] = False
                    area += 1

    return area


# h, w := Size
# k := 사각형 개수
h, w, k = map(int, input().split())

# grid := 좌표평면
# 좌표평면에 사각형을 False로 표시
grid = [[True] * w for _ in range(h)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())

    for y in range(ly, ry):
        for x in range(lx, rx):
            grid[y][x] = False

# areas := 빈 곳의 넓이 리스트
# 빈 곳을 탐색하여 넓이 계산
areas = []
for y in range(h):
    for x in range(w):
        if grid[y][x]:
            areas.append(bfs(y, x))

print(len(areas))
print(*sorted(areas))