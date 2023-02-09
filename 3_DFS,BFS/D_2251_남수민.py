# 2251. 물통
# 44ms

# 접근법
# 1. 가능한 모든 물의 이동에 대하여 너비탐색 (6가지)
# 2. checked를 통해 새로운 상태에서만 탐색
# 3. 옮길 수 있는 물의 양 = min(물의양(from), 남은공간(to))

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())  # a, b, c := 각 컵의 용량
capacity = (a, b, c)                 # capacity := 컵의 용량 (tuple)

queue = [[0, 0, c]]    # queue := 너비탐색 중인 컵 상태 (list<list>)
checked = [(0, 0, c)]  # checked := 체크완료한 컵 상태 (list<tuple>)

case = []  # case := 가능한 결과 (list)

# BFS 수행
while queue:
    cur_state = queue.pop()  # cur_state := 현재 상태

    # x의 물을 y로 옮기는 모든 경우의 수
    for x, y in ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)):

        # x가 비어있을 경우 continue
        if not cur_state[x]:
            continue

        # amount := 옮길 수 있는 물의 양
        amount = min(cur_state[x], capacity[y] - cur_state[y])

        # next_state := 물을 옮긴 상태
        next_state = cur_state[:]
        next_state[x] -= amount
        next_state[y] += amount

        # 만약 첫 등장한 비율이라면
        # 1. checked 업데이트
        # 2. BFS queue에 추가
        # 3. a가 비어있다면 case에 추가
        if next_state not in checked:
            checked.append(next_state)
            queue.append(next_state)
            if not next_state[0]:
                case.append(next_state[2])

case.sort()
print(' '.join(map(str, case)))