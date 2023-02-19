# 42340 672

# 2342 기타레슨
# 가능한 블루레이의 크기 중 최소를 구하는 프로그램

# 블루레이의 개수가 많으면 블루레이 크기를 늘리고,
# 블루레이 개수가 적으면 블루레이 크기를 줄여가며 이분탐색
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int,input().split()))

end = sum(data) # 강의를 하나의 블루레이에 다 담을 수 있을때
start = max(data) # 블루레이가 가질 수 있는 가장 작은 크기

while start <= end:
    mid = (start+end) //2
    cnt = 0
    sum_lesson = 0
    for i in range(n):
        if sum_lesson + data[i] > mid: # 더이상 현재 블루레이에 들어갈 수 없음
            cnt += 1
            sum_lesson = 0

        sum_lesson += data[i] # 아직 들어 갈 수 있으면
    else:
        if sum_lesson: # 남은 강의가 있으면
            cnt += 1

    if cnt <= m : # 블루레이의 크기를 줄여서 개수를 늘린다.
        end = mid -1
    elif cnt > m: # 블루레이의 크기를 늘려서 개수를 줄인다
        start = mid +1

print(start) # 최소크기 이므로 start


