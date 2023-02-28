#34044	212

# n : 정수 삼각형의 크기
# dp : 입력 받은 정수 삼각형을 저장할 배열
n = int(input())

dp = []

for i in range(n):
    dp.append(list(map(int,input().split())))

# 삼각형의 맨 위 부터 아래로 탐색
# 현재 삼각형의 위치에서 밑으로 갈 수 있는 선택지의 값을 더해나가면서 해당 경로까지의 정수의 합을 저장해나감
# 이때 맨 처음과 마지막에 오는 숫자는 바로 위의 숫자를 더해주고, 나머지는 본인의 왼쪽 대각선, 오른쪽 대각선의 값 중 더 큰 것을 골라
# 더해 나가면 된다. 
for i in range(1,n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i][j]+dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+dp[i][j]

print(max(dp[n-1]))

