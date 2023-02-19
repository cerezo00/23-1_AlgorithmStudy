# 2417. 정수제곱근
# 40ms

# 접근법
# 1. 기본 BS 유형
# 2. 조건 : 같은(X) 같거나 큰(O)
# 3. 경우의 수
#    마지막 루프 (low = mid = high)에서 mid가
#   1) 제곱근 보다 1↓ 작음 -> low가 업데이트(+1)
#   2) 제곱근 보다 1↓ 큼  -> high가 업데이트(-1)
# 4. 가능한 솔루션
#   ㄴ 조건이 "같거나 큰"이므로 +1만큼 업데이트되는 low를 출력한다.

# 사실 어려웠어

num = int(input())

l = 0
h = num

while l <= h:
    m = (l + h) // 2  # mid 계산

    if m ** 2 < num:  # low, high 업데이트
        l = m + 1
    else:
        h = m - 1

print(l)