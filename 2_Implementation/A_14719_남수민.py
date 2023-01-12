# 메모리 : 30616KB, 시간 : 44ms

# 문제 14719 : 빗물

# 접근법
# 1. 목표 : 고일 수 있는 물의 최댓값
# 2. 웅덩이의 형성 조건
#   > 양 옆에 현재 위치보다 높은 벽이 있어야 함
#   > min(왼쪽벽, 오른쪽벽)이 현재 위치보다 높다면, 두 값의 차이만큼 깊이가 생김

# h(w)_world := 세계의 세로(가로) 길이
# hs_block := 왼쪽부터 블럭이 쌓인 높이 리스트
h_world, w_world = map(int, input().split())
h_block = list(map(int, input().split()))

# amount := 고일 수 있는 물의 최댓값
amount = 0

# 각 열에 대하여 물이 얼만큼 쌓일 수 있는지 계산
for x in range(1, w_world - 1):

    # max_lh(rh) := 왼쪽(오른쪽)의 최대 높이
    max_lh = max(h_block[:x])
    max_rh = max(h_block[x + 1:])

    # depth := 현재 위치의 깊이 (가능한 웅덩이의 깊이)
    depth = min(max_lh, max_rh) - h_block[x]

    # 만약 깊이가 있다면 깊이만큼 합산
    if depth > 0:
        amount += depth

print(amount)