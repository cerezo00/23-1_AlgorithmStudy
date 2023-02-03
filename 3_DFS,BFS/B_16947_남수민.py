import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def find_circle_line(start_idx, cur_idx, cnt):
    global is_there_circle

    # 순환선 조건
    # 1. 현재 역이 시작 역과 동일
    # 2. 2곳 이상 방문
    if start_idx == cur_idx and cnt >= 2:
        is_there_circle = True
        return

    visited[cur_idx] = True  # 방문 여부 업데이트

    # 현재 역과 연결된 다음 역 탐색
    for next_idx in line_info[cur_idx]:
        # 다음 역을 방문하지 않았다면, cnt 증가 후 재귀호출
        if not visited[next_idx]:
            find_circle_line(start_idx, next_idx, cnt + 1)
        # 순환선을 조건을 만족했다면, cnt 증가 없이 재귀호출
        elif next_idx == start_idx and cnt >= 2:
            find_circle_line(start_idx, next_idx, cnt)


# 각 역에서 순환선 사이의 거리를 확인
def get_distance_to_circle():
    global check

    queue = deque()

    for i in range(num_station):
        if is_station_in_circle[i]:
            check[i] = 0
            queue.append(i)

    while queue:
        now = queue.popleft()

        for i in line_info[now]:
            if check[i] == -1:
                queue.append(i)
                check[i] = check[now] + 1

    for i in check:
        print(i, end=' ')


num_station = int(input())

# 노선 정보를 배열로 저장
line_info = [[] for _ in range(num_station)]  # line_info := 노선 정보
for _ in range(num_station):
    a, b = map(int, input().split())
    line_info[a-1].append(b-1)
    line_info[b-1].append(a-1)

is_station_in_circle = [False] * num_station  # circle_line_station := 순환선에 속하는지 여부
check = [-1] * num_station  # check := 정답 변수

# 순환선에 속하는 역 탐색
for i in range(num_station):
    # 변수 선언
    visited = [False] * num_station  # visited := DFS 방문 여무
    is_there_circle = False          # is_there_circle := 순환선 여부

    # 현재 역에 대하여 순환선 탐색
    find_circle_line(i, i, 0)

    # 현재 역이 순환선에 속하는지 업데이트
    if is_there_circle:
        is_station_in_circle[i] = True

get_distance_to_circle()