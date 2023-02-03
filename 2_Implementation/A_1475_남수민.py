# 메모리 : 30616KB, 시간 : 40ms

# 문제 1475 : 방 번호

# 접근법
# 1. 목표
#   > 가장 많이 등장한 숫자의 개수를 출력하는 문제
# 2. 조건
#   > 6과 9는 상호 보완 가능. 즉 6과 9는 개수를 공유한다.
#     ㄴ ((num6 + num9) / 2)  <  num6, num9  <  ((num6 + num9) / 2 + 1)

import math

# room_nbr := 방 번호의 숫자 리스트
room_nbr = list(map(int, input()))

# nmrc_frqnc := 번호[0-9]의 빈도수 리스트
# 각 번호의 출현 빈도수를 저장
nmrc_frqnc = [0] * 10
for nmrc in room_nbr:
    nmrc_frqnc[nmrc] += 1

# 접근법에서 구한 방식대로 6과 9의 개수 공유
nmrc_frqnc[6] += nmrc_frqnc.pop()
nmrc_frqnc[6] = math.ceil(nmrc_frqnc[6] / 2)

# result := 가장 많이 등장한 숫자의 개수
# 빈도수 배열을 정렬하여 가장 큰 값을 저장
result = sorted(nmrc_frqnc)[-1]

print(result)