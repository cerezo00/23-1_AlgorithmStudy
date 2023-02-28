# 백준 1932 정수 삼각형
# 메모리 35744 kb 시간 140 ms
# 위층에서 시작, 아래 대각선 수 중 하나 선택하여 내려옴 -> 선택된 수의 합이 최대가 되는 경로
import sys
input = sys.stdin.readline

n = int(input())  # 삼각형 크기
arr = []          # 정수 삼각형
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):    # 행
     for j in range(0, i+1): # 열
        if j == 0:  # 0번열 더하기
            arr[i][0] = arr[i][j] + arr[i-1][0]
        elif i == j:  # 마지막 열 더하기
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = arr[i][j] + max(arr[i-1][j-1], arr[i-1][j]) # j-1/j 중 최댓값 갱신

print(max(arr[n-1]))

