#31256	44

# N : 지름길의 개수
# D : 도로의 길이
# li : 시작위치, 도착위치, 지름길의 길이를 저장할 배열
# dp : 최단 거리 저장 배열
N, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [i for i in range(D+1)]

# 도로의 길이만큼 반복문을 돌면서
# 현재 위치에서 한 칸 전의 위치의 저장된 최단 거리의 값이 더 작다면 현재 위치의 dp 배열의 값을 (한 칸 전 위치의 dp 배열의 값) + 1 로 바꾸고
# 현재 위치에 지름길이 있다면 지름길로 건너간 곳의 원래 테이블 값과 지름길로 건너가기 전의 테이블 값+지름길의 거리 중 
# 더 작은 값으로 건너간 곳의 값을 바꾼다. 
for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1]+1)
    for s, e, d in li:
        if i == s and e <= D and dp[i]+d < dp[e]:
            dp[e] = dp[i]+d
print(dp[D])