# 2212. 센서
# 44ms

# 접근법
# 1. 일직선 상의 노드를 가까운 거리의 노드끼리 그룹화
# 2. 인접한 노드 간의 거리를 정렬하여 해결

def sol():
    num_sensor = int(input())
    num_center = int(input())
    pos_sensor = list(map(int, input().split()))
    pos_sensor.sort()

    gap_sensor = []
    for i in range(num_sensor - 1):
        gap = pos_sensor[i+1] - pos_sensor[i]
        gap_sensor.append(gap)

    gap_sensor.sort()

    # 이거 왜 [:1-num_sensor]는 안됨..?
    result = sum(gap_sensor[:num_sensor-num_center])
    print(result)


sol()