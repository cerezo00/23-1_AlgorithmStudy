# 1059. 좋은 구간
# 44ms

# 접근법
# 1. 경우의 수 계산 문제
# 2. (row ~ N) * (N ~ high) - 1
#   ㄴ -1을 하는 이유 : (N, N)을 제거
# 3. array에 '0' 추가
#   ㄴ N은 S[0]보다 작을 수 있기 때문에 하한을 지정

size = int(input())
array = sorted([0] + list(map(int, input().split())))
N = int(input())

result = 0
for i in range(size + 1):
    # array에 N이 있다면 "좋은 구간" 조건 위배
    if array[i] == N:
        break
    # N보다 큰 원소를 발견했다면 (high = i), (low = i-1)
    # 경우의 수 계산
    elif array[i] > N:
        result = (N - array[i-1]) * (array[i] - N) - 1
        break

print(result)