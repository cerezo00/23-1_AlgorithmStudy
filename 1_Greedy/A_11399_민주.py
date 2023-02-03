# 11399 ATM
# 각 사람이 돈을 인출하는데 필요한 시간의 합이 최솟값
# -> 인출 시간이 적게 걸리는 사람부터 정렬 (오름차순)

N = int(input())   # N : 사람의 수
P = list(map(int, input().split()))  # P : 각 사람이 돈을 인출하는데 걸리는 시간을 저장하는 배열
P.sort()  # 오름차순 정렬
result = 0  # result : 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

for i in range(1, N+1):
    result += sum(P[0:i]) # 각 사람이 인출하는데 걸리는 시간의 합을 더해나감 (0번째부터 i번째 수까지)

print(result)   # 결과값 출력

