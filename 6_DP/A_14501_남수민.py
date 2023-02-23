# 14501. 퇴사
# 40ms

import sys
input = sys.stdin.readline

num_day = int(input())
schedule = [list(map(int, input().split())) for _ in range(num_day)]

# Bottom-Up
# 첫 번째 날부터 순서대로 가능한 경우의 수를 탐색
dp_1 = [0 for _ in range(num_day + 1)]
for today in range(num_day):
    for next_day in range(today + schedule[today][0], num_day + 1):
        if dp_1[next_day] < dp_1[today] + schedule[today][1]:
            dp_1[next_day] = dp_1[today] + schedule[today][1]

print(dp_1[-1])


# Top-Down
# 마지막 날부터 순서대로 오늘 상담을 받는 것이 좋을지 판단
dp_2 = [0 for _ in range(num_day + 1)]
for today in range(num_day - 1, -1, -1):
    if today + schedule[today][0] > num_day:
        dp_2[today] = dp_2[today+1]
    else:
        dp_2[today] = max(dp_2[today+1], dp_2[today + schedule[today][0]] + schedule[today][1])
    print(dp_2)

print(dp_2[0])