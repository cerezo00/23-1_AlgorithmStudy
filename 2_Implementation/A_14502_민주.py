# 14502 연구소
# 메모리 140368KB 시간 2376ms
# 바이러스 전파 함수, 안전영역 찾는 함수 (dfs)
# 빈 칸에 벽을 치는 경우의 수를 찾으며 안전영역 크기 검사
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치

N, M = list(map(int, input().split()))   # N : 지도의 세로 크기, M : 가로 크기
array = []         # 초기 지도 모양을 저장하는 배열
result = 0         # 안전 영역 크기 최댓값

for i in range(N):
    array.append(list(map(int, input().split())))   # 초기 지도 모양 배열에 입력

def virus(array, x, y):    # 각 바이러스 사방으로 전파 (dfs)
    #global N, M
    dz = ((1, 0), (-1, 0), (0, 1), (0, -1))   # 이동 방향

    for d in dz:
        dx = x + d[0]
        dy = y + d[1]

        if dx < 0 or dx >= N or dy < 0 or dy >= M:   # 상하좌우로 퍼질 수 있는 경우 넘기기
            continue
        if array[dx][dy] == 1:   # 1이면 넘기기
            continue

        if array[dx][dy] != 2:   # 2가 아니면 (즉 0)
            array[dx][dy] = 2    # array에 2 저장 (= 바이러스 퍼짐)
            virus(array, dx, dy)  # virus 재귀적 수행

def dfs(wall, array):   # 벽 설치, 안전영역 크기 계산
    global result

    if wall == 3:     # 벽 3개를 모두 세웠을 떄
        tmp_array = [i[:] for i in array]   # 현재 맵 상태 저장

        for i in range(N):
            for j in range(M):
                if array[i][j] == 2:
                    virus(tmp_array, i, j)   # 각 바이러스의 위치에서 전파 진행
        safe_area = 0

        for i in range(N):
            for j in range(M):
                if tmp_array[i][j] == 0:    # 현재 배열 값 = 0 -> 안전영역 크기 계산
                    safe_area += 1
        result = max(result, safe_area)     # 안전 영역의 최댓값 계산
        # 현재 안전영역의 크기가 저장된 result보다 크면 현재 크기를 result에 새로 저장

    else:                            # 벽이 3개 모두 세워지지 않았다면 빈 공간에 설치
        for i in range(N):
            for j in range(M):
                if array[i][j] == 0:
                    wall += 1
                    array[i][j] = 1
                    dfs(wall, array)
                    array[i][j] = 0
                    wall -= 1

dfs(0, array)

print(result)
