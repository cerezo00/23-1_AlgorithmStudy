# 15686 치킨배달
# 메모리 30616 KB, 시간 600ms
# 0은 빈칸, 1은 집, 2는 치킨집
# 치킨 거리 = (r1, c1) - (r2, c2) = |r1 - r2| + |c1 - c2|
# 치킨집 개수 최대 M개, 도시 치킨 거리가 가장 작게 되도록

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 크기 N*N  M : 최대 치킨집 개수
info = [list(map(int, input().split())) for _ in range(N)] # 도시 정보
# 0은 빈칸, 1은 집, 2는 치킨집
house = []    # 집
chicken = []  # 치킨집
result = 10000 # 치킨 거리 최솟값

for i in range(N):
    for j in range(N):
        if info[i][j] == 1:        # 1이면 집이므로
            house.append((i, j))   # house에 추가
        elif info[i][j] == 2:      # 2이면 치킨집이므로
            chicken.append((i,j))  # chicken에 추가

for i in combinations(chicken, M): # 치킨집 M개 조합
    tmp = 0
    for j in house:
        distance = 999  # 치킨 거리
        for k in i:
            distance = min(distance, abs(k[0] - j[0]) + abs(k[1] - j[1]))
            # 저장되어있는 치킨 거리와 현재 인덱스에서 계산한 치킨 거리 중 더 작은 값을 distance에 저장
        tmp += distance
    result = min(result, tmp) # 저장되어있는 값과 현재 계산한 tmp값 중 더 작은 값을 result에 저장

print(result)  # 최소거리 출력
