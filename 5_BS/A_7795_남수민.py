# 7795. 먹을 것인가 먹힐 것인가
# 252ms (함수미사용 : 480ms)

# 이걸 대체 왜 이분탐색으로..;; -> 푸는지 몰랐었는데 공부에 도움이 되네요!

# 접근법 ==================================================
# Line 36에 등호를 넣은 이유
# - 자기보다 작은 먹이만 먹을 수 있다
#   => (a <= b)인 경우 업데이트

# Line 39에서 l, m, h 중 h를 참조하는 이유
# - l : 큰 값을 찾을 때 (+1 업데이트 되므로)
# - h : 작은 값을 찾을 때 (-1 업데이트 되므로)
# => 두 상황 모두 등호의 위치가 중요 (a = b인 상황에 대한 대처)

# 최종 BS 알고리즘 Flow (h 관점)
# ㄴ (a < b) : l += 1  ->  h 그대로 유지
# ㄴ (a = b) : h -= 1  ->  작은 값 참조
# ㄴ (a > b) : h -= 1  ->  작은 값 참조
# ========================================================

def BS():
    num_a, num_b = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = sorted(list(map(int, input().split())))

    count = 0

    for a in a_lst:
        h = num_b - 1
        l = 0

        while l <= h:
            m = (l + h) // 2
            if b_lst[m] < a:
                l = m + 1
            elif b_lst[m] >= a:
                h = m - 1

        count += h + 1

    result.append(count)


result = []
for _ in range(int(input())):
    BS()

print(*result, sep='\n')
