## 메모리 : 30616 kb, 시간 : 44ms

## 13335 트럭
## 하나의 차선으로 된 다리를 n개의 트럭이 지나감
## 트럭의 순서는 바꿀 수 없으며, 무게는 서로 같지 않을 수 있다.
## 다리 위에는 w 대의 트럭만 동시에 올라갈 수 있다.
## 다리 길이 : w 단위길이
## 각 트럭은 하나의 단위시간에 하나의 단위길이만큼만 이동할 수 있다.
## 동시에 다리 위에 올라가는 트럭 무게 함 <= 최대 하중 L
## 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge =[0] * w ## w만큼의 다리길이
weight, time = 0, 0 ## 현재 다리위의 무게, 시간 초기화

while True:
    out = bridge.pop(0)  # 방금 다리를 건넌 트럭은 다리에서 제거
    weight -= out  # 방금 다리를 건넌 트럭의 무게를 다리 위 무게에서 제거

    if trucks:  # 넘어올 트럭이 남아있을 때
        if weight + trucks[0] <= l : # 다리 하중을 견딜 수 있으면
            bridge.append(trucks[0]) # 다리를 건너려는 트럭 다리에 추가
            weight += trucks[0] # 현재 다리위에 무게도 추가
            trucks.pop(0)
        else : # 다리 하중을 견딜 수 없으면
            bridge.append(0) # 0을 추가해서 다리 위에 트럭을 먼저 보냄
    time += 1 # 조건과 상관없이 시간은 흐른다.

    if not bridge: # 다리 위에 트럭이 다 지나가면
        break # 반복문 종료

print(time)