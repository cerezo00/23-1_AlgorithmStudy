# 백준 14501 퇴사
# 메모리 31256 kb 시간 44 ms
# n일 동안 최대한 많은 상담
# 각 상담 완료 시간, 금액  -> 최대 이익

N = int(input()) # 기간
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split()))) # 상담 소요 기간, 금액
dp = [0]*(N+1)

for i in range(N-1, -1, -1): # 날짜 거꾸로 (일수 제한)
    if i + arr[i][0] > N: # 현재 날짜 + 상담 기간이 N을 넘으면
        dp[i] = dp[i+1]   # 다음 날 값 가져옴
    else:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i+ arr[i][0]])
        # i번째 날에 상담을 안했을 때의 값과 했을 경우 값 중 최댓값 저장
print(dp[0]) # 최대 수익
