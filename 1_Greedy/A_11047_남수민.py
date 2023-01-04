# 접근법
# 1. 동전을 액면가를 기준으로 내림차순 정렬
# 2. (금액/액면가)의 몫만큼 count를 증가시키고
# 3. 나머지 금액에 대하여 한 단계 낮은 액면가로 반복

# N := 동전 종류 개수
# K := 목표 금액
# A := 동전의 종류
N, K = list(map(int, input().split()))
A = list()
for _ in range(N):
    A.append(int(input()))
A.sort(reverse=True)

# count := 동전의 개수
# K / a의 몫만큼 count 증가
# K / a의 나머지에 대하여 다음 동전으로 반복
count = 0
for a in A:
    count += K // a
    K %= a

print(count)