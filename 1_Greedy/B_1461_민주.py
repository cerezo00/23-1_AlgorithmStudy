# 1461 도서관
# 메모리 30616 KB, 시간 36ms
# 현재 위치 0, 책들을 모두 제자리에 놔두는 최소 걸음 수
# 책의 개수 N, 한 번에 들 수 있는 책의 개수 M, 책의 위치 입력 -> 최소 걸음 수 출력
# 책의 위치 양수, 음수로 나누어 생각
# 마지막에 제자리에 두는 책은 원점으로 돌아올 필요가 없으므로 마지막은 가장 멀리 떨어져 있는 위치로 -> 가장 먼 책의 위치 찾기
import sys

N, M = map(int, sys.stdin.readline().split())      # N : 책의 개수, M : 한 번에 들 수 있는 책의 개수
location = list(map(int, sys.stdin.readline().split()))  # location : 책의 좌표
plus_walk = []  # 책의 위치 양수값 저장할 배열
minus_walk = [] # 책의 위치 음수값 저장할 배열
max_walk = 0  # 가장 멀리 떨어진 책의 위치
min_walk = 0 # 최소 걸음 수

for i in location:    # 양수 좌표 / 음수 좌표 배열을 나누어 저장
    if i > 0:
        plus_walk.append(i)   # 양수 좌표 plus_walk 배열에 저장
    else:
        minus_walk.append(i)  # 음수 좌표 minus_walk 배열에 저장

    if abs(i) > abs(max_walk):  # 가장 멀리 떨어진 책의 위치 찾기
        max_walk = i            # max_walk에 저장

plus_walk.sort(reverse=True)   # 양수 좌표 내림차순 정렬
minus_walk.sort()              # 음수 좌표 오름차순 정렬

for j in range(0, len(plus_walk), M):  # 양수 좌표에 있는 책 M권을 제자리에 둔다.
    if plus_walk[j] != max_walk:       # 가장 멀리 떨어진 책 제외
        min_walk += plus_walk[j]       # 최소 걸음 수에 저장

for k in range(0, len(minus_walk), M): # 음수 좌표에 있는 책 M권을 제자리에 둔다.
    if minus_walk[k] != max_walk:     # 가장 멀리 떨어진 책 제외
        min_walk += abs(minus_walk[k]) # 음수 값이므로 절댓값을 붙여 최소 걸음 수에 저장

min_walk *= 2     # 왕복하여 이동하므로 2를 곱셈
# 제일 멀리 있는 책을 놔둔다.
min_walk += abs(max_walk)   # 제외했던 가장 멀리 떨어진 책 위치 더함 (왕복 X 한 번만 더함)
print(min_walk)   # 최소 걸음 수 출력
