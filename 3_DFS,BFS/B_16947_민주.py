# 16947 서울 지하철 2호선
# 메모리 시간

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())                 # N : 역의 개수
info = [[]*N for _ in range(N)]  # 구간 정보
cycle_station = [0] * N          # 순환역 (방문X = 0, 방문O = 1, 순환역 = 2)
distance = [0] * N               # 역과 순환선 사이 거리
q = deque()                      # 큐 생성

def dfs(now,cnt):                # 순환역 찾기
    if cycle_station[now] == 1:       # 방문한 노드 중
        if cnt - distance[now] >= 3:  # 거리 차가 3 이상이면
            return now                # 순환역에 속하므로 현재 역 번호 반환
        else:
            return -1                 # 그렇지 않으면 -1

    cycle_station[now] = 1            # 방문 체크
    distance[now] = cnt               # 역과 순환 역 사이 거리에 cnt 저장

    for i in info[now]:
        start = dfs(i, cnt + 1)       # 재귀 호출 (cnt +1)
        if start != -1:               # 리턴값이 -1이 아니면 순환역에 속하므로
            cycle_station[now] = 2    # 2 저장 (순환역 O)
            if now == start:          # 현재 역과 시작역이 같으면 이 이후로는 순환역이 아니므로
                return -1             # -1 반환
            else:
                return start          # start 반환
    return -1

for _ in range(N):
    x, y = map(int, input().split())  # 구간 정보 입력
    info[x-1].append(y-1)
    info[y-1].append(x-1)
dfs(1, 0)

for i in range(N):
    if cycle_station[i] == 2:        # 순환역이면
        q.append(i)                  # 큐에 추가
        distance[i] = 0              # 거리에 0 저장
    else:                            # 순환역이 아니면
        distance[i] = -1             # 거리에 -1 저장

while q:
    current = q.popleft()    # q에 저장된 첫 번째 값 pop
    for i in info[current]:
        if distance[i] == -1:       # 방문 X
            q.append(i)
            distance[i] = distance[current] + 1  # 거리는 현재 역까지의 거리 + 1
print(*distance) # 결과값 출력
