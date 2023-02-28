# 백준 1446 지름길
# 메모리 31256 KB 시간 44 MS
# 고속도로 길이 D KM 지름길 일방통행 -> 운전 거리 최솟값
import sys
input = sys.stdin.readline

N, D = map(int, input().split()) # 지름길의 개수 / 고속도로의 길이
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split()))) # 지름길 시작 위치, 도착 위치, 지름길의 길이
dist = [i for i in range(D+1)] # 최단거리 저장

for i in range(D+1): # 0부터 D까지
    dist[i] = min(dist[i], dist[i-1]+1) # 지름길 거리와 고속도로 거리 비교하여 최솟값을 저장
    for start, end, short in arr:    # 지름길마다 최단거리 찾기
        if i == start and end <= D and dist[i] + short < dist[end]: # 지름길이 더 짧다면 갱신
            dist[end] = dist[i] + short
print(dist[D]) # 최솟값 출력

