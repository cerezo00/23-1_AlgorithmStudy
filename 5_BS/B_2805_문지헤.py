# 143400 4528
#
# 2805 나무 자르기
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에
# 설정할 수 있는 높이의 최댓값을 구하는 프로그램

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    mid = ( start + end ) //2

    log = 0
    for i in tree:
        if i >= mid:
            log += i - mid

    if log >= m:
        start = mid + 1
    else:
        end = mid -1

print(end) # 왜 start는 안되지?