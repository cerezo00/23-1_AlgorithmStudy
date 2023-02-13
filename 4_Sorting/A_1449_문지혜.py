# 1449 수리공 항승
# 테이프의 최소 개수

# 항승이는 항상 물을 막을 떄, 적어도 그 위치의 좌우 0.5 만큼 간격을 줘야 물이 다시는 안샌다고 생각
# 테이프 자를 수 없고 겹쳐서 붙이는 것도 가능

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
data = list(map(int, input().split()))

# 물이 새는 위치 오름차순 정렬
data.sort()

# 테이프를 붙이는 시작지점
start = data[0]
# 필요한 테이프 개수
count = 1

# 물이 새는 곳의 위치를 차례대로 받으면서
for location in data[1:]:
    # 테이프를 붙이는 범위 내에 물이 새는 곳이 있으면
    if location in range(start, start+1):
        # 기존 테이프 사용
        continue
    else:
        start = location
        count += 1

print(count)
