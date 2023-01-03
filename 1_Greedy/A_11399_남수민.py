# 접근법
# 가장 빠른 사람부터 시작한다.
# ㄴ 대기시간 총합 == (t1 * n) + (t2 * (n-1)) + ...
#    ㄴ (t1 * n) : 1번 사람의 소요시간을 n명이 대기
#    ㄴ (t2 * (n-1)) : 2번 사람의 소요시간을 (n-1)명이 대기 (1번 사람은 끝났으므로)
#    ㄴ ...반복...

# reduce() := 누적집계함수
from functools import reduce

# N := 사람 수
# P := 소요시간 리스트
# 소요시간을 오름차순 정렬
N = int(input())
P = list(map(int, input().split()))
P.sort()

# 처음에 접근한 공식에 따라 각 사람의 대기시간 총합을 계산
result = 0
for x in range(N):
    result += P[x] * (N - x)

# reduce(계산식, 초기값) 사용시 더 복잡해짐
# ㄴ 계산식 : lambda r, x: r + (P[x] * (N - x)), range(N)
#   ㄴ 첫 번째 인자 (r) : 누적 저장되는 값
#   ㄴ 두 번째 인가 (x) : range(N) : 소요시간 인덱스
#   ㄴ 계산식 : r + (P[x] * (N - x)) : 이전 값 + 현재 사람 떄문에 발생하는 전체소요시간
# ㄴ 초기값 : 0
# result = reduce(lambda r, x: r + (P[x] * (N - x)), range(N), 0)

print(result)

