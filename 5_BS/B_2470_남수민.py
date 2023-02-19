# 2470. 두 용액
# 130ms

# 접근법
# 1. 투포인터 문제
#   - left, right의 범위를 좁히면서 해결

# 입력
num_sample = int(input())
sample_list = sorted(list(map(int, input().split())))

# 결과 비교 변수
min_sum = int(2e9)
min_combi = [0, 0]

# 투포인터
l = 0
r = num_sample - 1
while l < r:
    l_sample = sample_list[l]
    r_sample = sample_list[r]
    sum_sample = l_sample + r_sample

    # 최소합 업데이트
    if abs(sum_sample) < min_sum:
        min_sum = abs(sum_sample)
        min_combi = [l_sample, r_sample]

    # 범위 축소
    if sum_sample < 0:
        l += 1
    else:
        r -= 1

print(*min_combi)