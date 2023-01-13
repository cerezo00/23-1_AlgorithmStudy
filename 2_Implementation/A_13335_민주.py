# 13335 트럭
# 메모리 30616KB 시간 68ms
# 다리 위 트럭의 무게의 합과 이동하려는 트럭의 무게 합이 최대 하중보다 작거나 같으면 트럭을 추가하고
# 그렇지 않다면 다리에 빈 공간을 추가한다. (다리 길이 유지)
import sys
input = sys.stdin.readline

n, W, L = map(int, input().split())    # n : 트럭 수, W : 다리 길이, L : 최대 하중
a = list(map(int, input().split()))    # a : n개의 트럭의 무게를 저장할 배열
bridge = [0 for _ in range(W)]         # 다리 칸 길이
count = 0                              # 최단 시간

while bridge:
    count += 1                  # 1번 수행할 때마다 시간이 1씩 걸림
    bridge.pop(0)               # 다리의 칸 하나 줄임
    if a:
        if sum(bridge) + a[0] <= L:      # 현재 다리 위 트럭의 무게 + 이동하려는 트럭의 무게의 합이 다리 최대 하중보다 작거나 같으면
            bridge.append(a.pop(0))      # 트럭을 다리 칸 위에 추가
        else:                            # 하중보다 크다면
            bridge.append(0)             # 트럭을 다리 위에 올릴 수 없으므로 다리에 빈 공간 추가

print(count)   # 최단 시간 출력

