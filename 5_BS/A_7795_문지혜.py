# 7795 먹을 것인가 먹힐 것인가
# 34684kb 148ms
# A는 자기보다 크기가 작은 B를 먹는다

# 정렬을 하고 while문을 써서 가지치기를 해줘야 시간초과가 안뜸
import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    cnt = 0
    pair = 0
    a, b = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    arr_a.sort()
    arr_b.sort()

    for i in range(a):
        while True:
            if cnt == b or arr_a[i] <= arr_b[cnt]: # a의 i번째 수가 b의 모든 원소보다 값이 크거나
                # a의 i번쨰 수가 b의 cnt보다 작은 경우 오름차순 정렬되어있으므로 뒤에는 무조건 a의 i번째 보다 작으므로 break
                pair += cnt
                break
            else:
                cnt += 1
    print(pair)
