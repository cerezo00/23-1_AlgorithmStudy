# 플로우
# 1. 각 인원간 키 차이를 계산
# 2. 키 차이가 큰 지점부터 분리지점 저장
# 3. 분리지점을 기준으로 한 그룹씩 cost 계산

# N := 인원수
# K := 그룹 개수
# H := 키 리스트 (오름차순)
N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

# gap := [현재 사람의 번호]와 [이전 사람과의 키 차이] 딕셔너리
# 인덱스를 1부터 시작한 이유는 첫 번째 그룹의 시작지점을 0으로 정의하기 위해서이다.
# ㄴ 1부터 시작 -> (div[i])번째 사람부터 (div[i+1]-1)번째 사람까지 그룹
# ㄴ 0부터 시작 -> (div[i]+1)번째 사람부터 (div[i+1])번째 사람까지 그룹
# ㄴ (div는 그룹을 분리하는 위치 인덱스)
gap = dict()
for i in range(1, N):
    gap[i] = H[i] - H[i - 1]

# gap_s := 딕셔너리 gap를 value를 기준으로 내림차순 정렬
# sorted의 결과 : Dict와 Key,Value 쌍은 Tuple들의 List로 반환된다. (ex. [(1,2), (3,4), (5,6)])
gap_s = sorted(gap.items(), key=(lambda x: x[1]), reverse=True)

# div := 그룹을 분리하는 지점 (모든 그룹의 처음과 끝)
# div로 구간을 지정하기 위해 처음과 끝(0, N)을 추가한다.
# 키 차이가 큰 지점부터 분리지점을 추가한다.
# 앞에서부터 순서대로 분리하기 위해 분리지점을 오름차순 정렬한다.
div = [0, N]
for i in range(K - 1):
    div.append(gap_s[i][0])
div.sort()

# cost := 전체비용 (그룹 별 비용 : 가장 키가 큰 사람과 작은 사람의 차이)
# div의 값들을 기준으로 각 그룹의 마지막에서 처음을 뺄셈 연산한다. (오름차순이므로)
cost = 0
for i in range(K):
    cost += H[div[i + 1] - 1] - H[div[i]]

print(cost)