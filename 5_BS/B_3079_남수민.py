# 3079. 입국심사

import sys
input = sys.stdin.readline

num_way, num_people = map(int, input().split())
pass_time_list = [int(input()) for _ in range(num_way)]

l = min(pass_time_list) * num_people
r = max(pass_time_list) * num_people

while l <= r:
    m = (l + r) // 2
    tot_people = 0

    for i in range(num_way):
        tot_people += m // pass_time_list[i]

    if tot_people >= m:
        r = m - 1
    else:
        l = m + 1

print(l)
