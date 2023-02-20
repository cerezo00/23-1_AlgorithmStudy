# 백준 2805 나무 자르기
N, M = map(int, input().split())
# N : 나무 수, M : 가져가려는 나무 길이
height = list(map(int, input().split())) # 나무 높이
start, end = 0, max(height) # 시작,끝
result = 0

while start <= end:
    length = 0
    mid = (start + end) // 2
    for i in height:
        if i > mid:
            length += i - mid # 잘랐을 떄 떡의 양
    if length < M:    #  나무 길이가 더 작으면
        end = mid - 1 # 왼쪽 부분 탐색
    else:             # 나무 길이가 더 길면
        result = mid  # 오른쪽 부분 탐색
        # 최대한 덜 잘라야 하므로 result에 갱신 
        start =mid + 1
print(result) # 높이 최댓값 출력
