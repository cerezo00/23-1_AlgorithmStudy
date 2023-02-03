# 14719 빗물
# 메모리 시간
# 현재 블록의 왼쪽 오른쪽 블록이 모두 현재 블록보다 높아야 빗물이 고일 수 있음
# 빗물이 고이는 양 = 왼쪽/오른쪽 중 더 작은 높이 - 현재 높이
# 첫 번째와 마지막 블록은 빗물이 고이지 않으므로 제외 (1, W-1)

import sys
input = sys.stdin.readline

H, W = map(int, input().split())    # H : 세로 길이, W : 가로 길이
height = list(map(int, input().split()))   # 블록이 쌓인 높이 W개
total = 0   # 고이는 빗물의 총량

for i in range(1, W-1):       # 반복문 1부터 W-1까지 수행 (처음과 끝에는 빗물이 고이지 않음)
    left_height = max(height[ :i])   # 현재 i번째 블록의 왼쪽에서 최대 높이를 저장
    right_height = max(height[i+1: ])  # 현재 i번째 블록의 오른쪽에서의 최대 높이를 저장
    if min(left_height, right_height) > height[i]:  # 둘 중 작은 값이 현재 블록보다 크다면
        total += min(left_height, right_height) - height[i]   # 고이는 총량에 왼쪽/오른쪽 중 더 작은 높이 - 현재 높이
print(total)
