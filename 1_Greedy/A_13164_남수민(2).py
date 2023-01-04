# 도출과정
# 1. 각 그룹마다 (가장 큰 사람과 작은 사람의 gap)을 연산
# 2. (가장 큰 사람과 작은 사람의 gap) == (그룹 내 모든 구성원 간 gap) (오름차순 일 때)
# 3. cost == (분리 지점의 gap을 제외한 모든 gap을 더한 것)

# 플로우
# 1. 구성원 간 키 차이를 구하여 정렬
# 2. 가장 큰 (K-1)개를 제외하고 모두 합산
# ㄴ (K-1) : K개의 그룹으로 나누려면 K-1번 분리해야 하므로

# N := 인원수
# K := 그룹 개수
# H := 키 리스트 (오름차순)
N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

# gap := 키 차이 리스트
# 오름차순 정렬
gap = list()
for i in range(N - 1):
    gap.append(H[i + 1] - H[i])
gap.sort()

# cost := 전체비용
# 분리하는 지점의(gap이 가장 큰) gap을 제외하고 모두 합산
cost = 0
for i in range(N - K):
    cost += H[i]

print(cost)
