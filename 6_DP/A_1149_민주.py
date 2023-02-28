# 백준 1149 RGB 거리
# 메모리 31388 KB 시간 44 MS
# 집 N개 (1---N) 빨강 초록 파랑 중 하나 색
# 1번 집 색 != 2번 집 색
# N번 집 색 != N-1번 집 색
# i번 집 색 != i-1, i+1번 집 색
# 모든 집 칠하는 최소 비용
import sys
input = sys.stdin.readline
N = int(input()) # 집의 수
arr = []         # 각 집마다 색칠(r,g,b) 비용
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]  # i번째 집 빨간색 칠할 때 최소
    # 이전 값 중 같은 값 제외 최솟값 + 현재 빨강 칠하는 비용
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]  # 초록
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]  # 파랑

print(min(arr[N-1])) # 위에서 구한 값 중 최솟값 출력
