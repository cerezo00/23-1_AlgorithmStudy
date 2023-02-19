# 백준 2343 기타 레슨
# 메모리 42340 KB 시간 216MS
# 블루레이 길이 최소

N, M = map(int, input().split())
# N : 강의의 수 M : 블루레이 개수
lesson = list(map(int, input().split())) # 강의 길이
result = 0
start, end = max(lesson), sum(lesson) # 시작, 끝

def binary_search(start, end, arr):
    while start <= end:
        mid = (start + end) // 2
        count = 0 # 블루레이 개수
        temp = 0  # 현재 누적 블루레이 길이

        for i in arr:
            if temp + i > mid: # 누적 길이가 mid보다 크면 (더이상 불가능)
                count += 1 # 카운트
                temp = 0   # 초기화
            temp += i # 현재 길이 누적
        if temp: # temp에 값이 있으면
            count += 1 # 카운트
        if count > M:  # 블루레이 개수가 넘어가면  (오른쪽 탐색)
            start = mid + 1 # 시작점 중간지점 + 1
        else:
            end = mid - 1 # 왼쪽 탐색
            result = mid  # result에 mid 갱신
    print(start)

result = binary_search(start, end, lesson) # 이진 탐색
