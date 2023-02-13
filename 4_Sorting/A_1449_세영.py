#31256	44

import sys
input = sys.stdin.readline

# N : 물이 새는 곳의 개수
# L : 테이프의 길이
N , L = map(int,input().split())

# water : 물이 새는 곳의 위치를 저장할 배열
water = list(map(int,input().split()))

# water을 오름차순으로 정렬 -> 맨 왼쪽부터 테이프를 하나하나씩 붙여가기 위함
# cnt : 필요한 테이프의 개수
water.sort()
cnt = 1

# 물을 막을 때 적어도 현재 위치의 좌우 0.5만큼 간격을 줘야하므로 테이프를 붙이기 시작할 
# 처음 위치 start를 water 배열의 첫 번째 원소값에서 0.5를 빼준 값으로 초기화
start = water[0] - 0.5

# 물이 새는 곳의 위치의 수 -1 만큼 
# 현재 시작 위치 start에서 테이프 길이를 더한 값을 curLen에 저장하여
# 만약 다음 물이 새는 위치보다 더 크면 현재 테이프 하나로도 구멍이 막아진다는 뜻이므로 continue로 계속해서 비교 진행
# 만약 더 작다면 새로운 테이프로 막아야하므로 start를 다음 물이 새는 위치의 -0.5의 위치로 바꿔주고
# 테이프의 개수를 1개씩 늘려간다.
for i in range(len(water)-1):
    curLen = start + L
    if curLen > water[i+1]:
        continue
    else:
        start = water[i+1] - 0.5
        cnt += 1

print(cnt)


