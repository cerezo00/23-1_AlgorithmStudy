# 1744 수 묶기
# 메모리 31256KB, 시간 44 ms
# 수 묶어서 더하기, 묶은 수는 서로 곱한 후 덧셈
# 양수, 음수 나누기 각각 짝수면 2개씩 곱하고 홀수면 마지막 수 빼고 곱한 후 더해줌

import sys
input = sys.stdin.readline

N = int(input()) # 수 개수
result = 0 # 결과값
plus = [] # 양수
minus = [] # 음수
for _ in range(N):
    num = int(input())   # 수를 입력 받아서
    if num == 1:         # 1일 경우 곱해도 최대가 안되므로 result에 먼저 더해줌
        result += 1
    elif num > 1:        # 양수는 plus 배열에 저장
        plus.append(num)
    else:                # 음수면 minus 배열에 저장
        minus.append(num)

plus.sort(reverse=True)  # 양수는 내림차순 정렬
minus.sort()             # 음수는 오름차순 정렬

if len(plus) % 2 == 0:   # 짝수면 2개씩 곱하면 된다
    for i in range(0, len(plus), 2):
        result += plus[i] * plus[i + 1] # 2개씩 곱해 result에 더함
else:
    for i in range(0, len(plus) - 1, 2): # 홀수일 경우 마지막 수를 제외하고 2개씩 곱해
        result += plus[i] * plus[i + 1]  # result에 더하고
    result += plus[len(plus)-1]          # 마지막 수도 더함

if len(minus) % 2 == 0:
    for i in range(0, len(minus), 2):
        result += minus[i] * minus[i + 1]
else:
    for i in range(0, len(minus) - 1, 2):
        result += minus[i] * minus[i + 1]
    result += minus[len(minus)-1]

print(result) # 결과 출력
