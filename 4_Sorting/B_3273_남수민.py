# 3273. 두 수의 합
# 80~84ms

import sys
input = sys.stdin.readline

size = int(input())  # 1 <= n <= 10^6
array = sorted(list(map(int, input().split())))  # 1 <= a <= 10^6
X = int(input())  # 1 <= X <= 2 * 10^6

idx_a = 0  # array 탐색 index
pair = []  # a(j)가 될 수 있는 값의 리스트

# a(i)를 찾는 과정
for i in range(size):
    # a < X/2 일 때, pair에 append
    if array[i] < X / 2:
        pair.append(X - array[i])
    # a > X/2 일 떄, 중단
    else:
        idx_a = i
        break

# 최선의 시간복잡도를 위해서는 idx 역순 탐색이 유리
# 할 줄 알았으나 똑같더라 ㅇㅁㅇ,, 왜?
pair = list(reversed(pair))

count = 0          # 조건을 만족하는 쌍 (정답)
idx_p = 0          # pair 탐색 index
len_p = len(pair)  # pair의 길이 (while 조건)

# a(j)를 찾는 과정
# 모든 pair를 탐색할 때까지 반복
while idx_p < len_p and idx_a < size:
    # a < p 일 때, 다음 a에 대하여 비교
    if array[idx_a] < pair[idx_p]:
        idx_a += 1
        continue

    # a == p 일 때, 카운팅
    if array[idx_a] == pair[idx_p]:
        idx_a += 1
        count += 1

    idx_p += 1  # p_idx 증가

print(count)