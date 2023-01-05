# 11047 동전 0
# K를 동전 가치가 큰 종류부터 채워가야 함
# 현재 가치의 합을 현재 동전 종류로 나누어 count값에 더함

N, K = map(int, input().split())  # N : 가지고 있는 동전 종류 수, K : 가치의 합
result = 0  # K원을 만드는 데 필요한 동전 개수의 최솟값

A = [int(input()) for i in range(N)]   # 동전의 가치 N개 입력받아 배열 A에 저장 (오름차순)

A.sort(reverse=True)  # A를 내림차순 정렬
# 최소로 동전을 사용하려면 동전 가치가 큰 값부터 가치에 더해야가야 함 -> 내림차순 정렬

for i in A:
    result += K // i  # 현재 가치의 합 K를 현재 원소로 나눈 몫을 result에 저장
    K = K % i        # K에 K를 현재 원소로 나눈 나머지 저장

print(result)  # K를 만드는데 필요한 동전 개수의 최솟값 result 출력
