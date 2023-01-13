# 4096KB	92ms

import sys
from collections import deque
input = sys.stdin.readline

# n : 다리를 건너는 트럭의 수
# w : 다리의 길이
# l : 다리의 최대하중
# trucks : 트럭들의 무게
# answer : 트럭들이 전부 다리를 건너는 최단시간
# bridge : 다리를 나타내는 queue, 이때 길이를 다리의 길이인 w만큼 0으로 채움

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

answer = 0
bridge = deque([0 for _ in range(w)])

# 트럭의 원소가 전부 사라질 때까지 아래의 과정을 반복한다.
# 다리의 맨 앞에 있는 트럭을 제거해주고, 제거해 준 후의 다리위의 트럭의 개수가 w 미만일 때 원소를 추가하는데,
# 이때 다리의 원소들의 합이 추가할 트럭의 무게와 합했을 때 다리의 최대 하중인 l을 넘지 않을 때에만 추가한다. 
# 만약 l을 넘는다면 트럭이 아닌 0을 추가하여 다리의 길이를 유지해준다.
# 위 과정을 한 번 반복할 때마다 answer에 1을 더해준다.
# 반복문이 종료될 때 w를 한 번 더 더해주는 이유는 while문이 마지막에 진입한 트럭이 진입할 때 종료, 즉 아직 다리를 건너지 못한 상태에서 졸료되었기 때문에
# 마지막 트럭이 다리를 지나갈 때 까지의 시간을 더해주는 것이다.

while trucks:
    bridge.popleft()
    if len(bridge) < w:
        if sum(bridge) + trucks[0] <= l:
            truck = trucks.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)
    answer += 1
answer += w
print(answer)