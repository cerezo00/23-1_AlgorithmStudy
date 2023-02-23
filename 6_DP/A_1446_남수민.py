# 1446. 지름길
# 44ms

import sys
input = sys.stdin.readline

num_sc, len_hw = map(int, input().split())
info_sc = [list(map(int, input().split())) for _ in range(num_sc)]

dist = list(range(len_hw + 1))  # dist := 운전거리

for pos in range(len_hw + 1):
    # 현재 pos까지의 운전거리 업데이트
    # -> 지름길을 통해 dist[pos]가 dist[pos]보다 더 작을 수 있으므로
    dist[pos] = min(dist[pos-1] + 1, dist[pos])

    # 지름길의 정보를 받아와서 거리 업데이트
    # 조건1. 시작 지점이 pos이며,
    # 조건2. 도착 지점이 고속도로 내에 있고,
    # 조건3. 지름길 이용시 거리가 감소할 경우
    # -> 지름길은 최대 12개이므로 O(len_hw)의 시간복잡도 유지
    for s, e, len in info_sc:
        if s == pos and e <= len_hw and dist[pos] + len < dist[e]:
            dist[e] = dist[pos] + len

print(dist[len_hw])