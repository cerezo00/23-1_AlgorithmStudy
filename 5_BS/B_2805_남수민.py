# 2805. 나무 자르기
#

# collections.Counter 함수
# - 배열의 원소 별 개수를 Counter 타입으로 리턴
# ex) Counter([A, B, B, C, C, C])
#  -> [[A, 1], [B, 2], [C, 3]]

import sys
from collections import Counter

input = sys.stdin.readline

num_tree, req_len = map(int, input().split())
tree_height_list = Counter(map(int, input().split()))

# BS
l = 0
h = max(tree_height_list.items())[0]
while l <= h:
    m = (l + h) // 2

    sum_len = sum((h-m)*i for h,i in tree_height_list.items() if h>m)

    if sum_len >= req_len:
        l = m + 1
    else:
        h = m - 1

print(h)
