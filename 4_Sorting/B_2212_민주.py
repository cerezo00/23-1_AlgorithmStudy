# 2212 센서
# 메모리 32276 KB, 시간 48 ms
# 센서들이 일직선 상에 오름차순 정렬 -> 집중국 개수로 구역을 나누면 구역에서 센서들의 차가 집중국
import sys
input = sys.stdin.readline

N = int(input()) # 센서 개수
K = int(input()) # 집중국 개수
arr = list(map(int, input().split())) # 센서 좌표
arr.sort() # 오름차순 정렬

diff = [] # 센서들의 차
for i in range(1, N):
    diff.append(arr[i] - arr[i-1])
diff.sort() # 오름차순 정렬
print(sum(diff[:N - K])) # 길이 합 최솟값
