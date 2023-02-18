# 2343. 기타 레슨
# 172ms

# 접근법
# 1. 이분탐색 방법
#   - 구해야 하는 것 : 디스크의 최소 길이
#   - 디스크의 최소 길이를 기준으로 이분탐색 징행
# 2. 이분탐색 조건
#   1) 모든 영상을 담는데 필요한 디스크(size=m)의 개수를 계산
#   2) 보유 중인 디스크가 부족하면 디스크 용량 UP (l 업데이트)
#      보유 중인 디스크가 넉넉하면 디스크 용량 DOWN (h 업데이트)

import sys
input = sys.stdin.readline


# disk의 size가 mid 일 때
# 모든 영상을 담는데 필요한 disk의 개수를 반환하는 함수
def get_req_num_disk(size_disk):
    req_num_disk = 1
    total_len_video = 0

    for len_video in len_video_list:
        total_len_video += len_video
        if total_len_video > size_disk:
            total_len_video = len_video
            req_num_disk += 1

    return req_num_disk


# 입력
num_video, num_disk = map(int, input().split())
len_video_list = list(map(int, input().split()))

# BS
l = max(len_video_list)
h = 1000000000  # 1e9
while l <= h:
    m = (l + h) // 2

    # disk가 넉넉하면 h
    #        부족하면 l 업데이트
    if num_disk >= get_req_num_disk(m):
        result = m
        h = m - 1
    else:
        l = m + 1

# 정답 출력
print(l)