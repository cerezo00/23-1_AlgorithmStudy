# 메모리 : 30616KB, 시간 : 40ms

# 문제 13335 : 트럭

# 접근법
# 1. 유형 : 시뮬레이션 : 상황의 흐름을 순서대로 작성
# 2. 목표 : 마지막 트럭이 다리를 건넜을 때의 시간
# 3. 조건 : 다리 위 트럭의 무게 합이 다리의 최대하중을 초과할 수 없다.
#   > (현재 하중 + 다음 차의 무게)  <  최대 하중
# 4. 접근법
#   1) loop 조건
#     a) loop 마다 1턴씩 진행 (X)
#       > 최악의 경우 (n=1000, w=100, l=1, a=[1, 1, ...]) 시간복잡도는 O(nm) = 100,000
#     b) loop 마다 1대씩 입장 (O)
#       > 최악의 경우 시간복잡도는 o(n) = 1,000
#   2) 데이터 관리
#     a) FIFO 큐(list) 사용 (X)
#       > append, pop 사용 시 연산량이 많아짐 (각 명령 : O(n))
#     b) 변수와 리스트(초기화 된) 사용 (X)
#       > 변수명, 인덱스를 통해 직접 접근 (각 명령 : O(1))

# num_truck := 트럭의 수
# len_bridge := 다리의 길이
# max_load := 다리의 최대 하중
# weights := 각 트럭의 무게 리스트
num_truck, len_bridge, max_load = map(int, input().split())
weights = list(map(int, input().split()))

turn = 0       # 현재 단위시간
cur_load = 0   # 다리의 현재 하중
first_idx = 0  # 다음 퇴장할 차의 idx
next_idx = 0   # 다음 입장할 차의 idx
enter_turn = [-1] * num_truck  # 각 차들의 입장 시간

# 각 Loop 마다 트럭 1대씩 입장 (트럭의 수만큼 반복)
while next_idx < num_truck:

    # 만약 현재 턴에 제일 앞차가 다리에서 내린다면
    # 현재 차 퇴장 후 무게, 선두idx 업데이트
    if enter_turn[first_idx] + len_bridge == turn:
        cur_load -= weights[first_idx]
        first_idx += 1

    # 다음 차가 다리에 입장할 수 있다면
    # 다음 차 입장 후 무게, 입장시간, 다음idx 업데이트
    if cur_load + weights[next_idx] <= max_load:
        cur_load += weights[next_idx]
        enter_turn[next_idx] = turn
        next_idx += 1
    # 다음 차가 다리에 입장할 수 없다면
    # 제일 앞 차가 내릴 시간으로 스킵
    else:
        turn = enter_turn[first_idx] + len_bridge - 1

    # 턴 업데이트
    turn += 1

# result := 모든 트럭이 다리를 지나가는 시간
# 현재 턴 + 다리의 길이(방금 입장한 차가 다리를 건너는데 걸리는 시간)
result = turn + len_bridge

print(result)
