# 17144 미세먼지 안녕!
# 메모리 30684KB , 시간 3988 ms
# 공기청정기 1번 열 설치 (크기 두행)
# (r, c)에 있는 미세먼지 양 A[x][y], 확산되는 양 A[x][y]/5
# (r, c)에 남은 미세먼지 양 = A[x][y] - (A[x][y]/5)*(확산된 방향 개수)

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
# 집의 크기 R*C
# T : 시간 (T초)

A = []
for _ in range(R):
    A.append(list(map(int, input().split())))
# 각 칸의 미세먼지 양 입력

#cnt = 0
cleaner = []
result = 0

for i in range(R):         # 공기 청정기 위치 찾기 (공기청정기가 있는 행의 정보 (위 아래))
    if A[i][0] == -1:      # A 값이 -1 이면 공기청정기가 설치된 곳이므로
        cleaner.append(i)

def dust_spread():             # 미세먼지를 확산시키는 함수

    dx = [1, 0, -1, 0]  # 이동방향 X
    dy = [0, 1, 0, -1]  # 이동방향 Y

    tmp = [[0] * C for _ in range(R)]    # 임시 리스트 (확산이 동시에 진행)

    for i in range(R):
        for j in range(C):       # 모든 행/열 확인
            x, y = i, j
            count = 0            # 확산된 방향 개수

            if A[x][y] == 0:     # 미세먼지가 없는 경우
                continue         # 넘기기
            if A[x][y] == -1:     # 공기청정기가 있는 경우
                tmp[x][y] = -1   # 넘기기
                continue

            for k in range(4):   # 미세먼지가 있는 경우 인접한 4방향 수행
                nx = dx[k] + i
                ny = dy[k] + j
                if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1: # 범위에서 벗어나지 않아야 함
                    count += 1     # 확산된 방향 카운트
                    tmp[nx][ny] += int(A[i][j] // 5)    # 확산되는 미세먼지 양 저장
            tmp[x][y] += int(A[x][y] - (A[x][y] // 5) * count) # tmp에  확산 후 존재하는 미세먼지 양 저장

    for i in range(R):
        for j in range(C):
            A[i][j] = tmp[i][j]     # 임시 리스트를 A에 저장

def cleaner_up():          # 공기청정기 위쪽 반시계 방향으로 작동하는 함수
    # 반시계 방향 공기 순환 -> 동 - 북 - 서 - 남
    dx = [0, -1, 0, 1]  # 이동방향 X
    dy = [1, 0, -1, 0]  # 이동방향 Y

    former = 0  # 이전 좌표
    direct = 0  # 방향
    x, y = cleaner[0], 1  # 공기청정기 위치 (윗부분)

    while True:
        nx = x + dx[direct]    # x방향 이동위치
        ny = y + dy[direct]    # y방향 이동위치

        if x == cleaner[0] and y == 0:      # 다시 처음 위치가 되면 종료
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:   # 범위를 벗어난다면
            direct += 1    # 방향 바꾸고 넘기기
            continue

        A[x][y], former = former, A[x][y]   # 두 좌표 바꾸기
        x = nx
        y = ny

def cleaner_down():      # 공기청정기 아래쪽 시계 방향으로 작동하는 함수
    # 시계 방향 공기 순환 -> 동 - 남 - 서 - 북
    dx = [0, 1, 0, -1]  # 이동방향 X
    dy = [1, 0, -1, 0]  # 이동방향 Y

    former = 0
    direct = 0
    x, y = cleaner[1], 1      # 공기청정기 위치 (아랫부분)

    while True:
        nx = x + dx[direct]     # x방향 이동위치
        ny = y + dy[direct]     # y방향 이동위치
        if x == cleaner[1] and y == 0:     # 다시 처음 위치가 되면 종료
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:      # 범위를 벗어난다면
            direct += 1       # 방향 바꾸고 넘기기
            continue

        A[x][y], former = former, A[x][y]     # 두 좌표 바꾸기
        x = nx
        y = ny


# T초 후 A[]의 미세먼지 양 합산
for _ in range(T):    # T초까지 진행
    dust_spread()     # 미세먼지 확산
    cleaner_up()     # 공기순환 (위쪽)
    cleaner_down()   # 공기순환 (아래쪽)

for i in range(R):        # 미세먼지 양 result에 저장
    for j in range(C):
        if A[i][j] > 0:  # 미세먼지가 존재한다면
            result += A[i][j]  #  result에 합산

print(result)          # 결과 출력
