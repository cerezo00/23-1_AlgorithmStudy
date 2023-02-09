# 1449 수리공 항승
# 메모리 31256 KB, 시간 44ms

import sys
input = sys.stdin.readline

N, L = map(int, input().split())   # N : 물이 새는 곳 개, L : 테이프 길이
arr = list(map(int, input().split())) # arr[] : 물이 새는 곳 위치
arr.sort()  # 물이 새는 곳 위치 오름차순 정렬
visit = [0 for _ in range(10000)]  # 방문 체크
count = 0  # 필요한 테이프 최소 개수

for i in arr:     # 물이 새는 곳 위치 오름차순으로 확인
    if visit[i] == 1:  # 방문했으면 테이프를 이미 붙였으므로 넘기기
        continue
    else:              # 방문 안했으면 count +1
        count += 1
        for j in range(L):  # 이때 테이프로 커버 가능하면
            visit[i+j] = 1  # 테이프를 붙이고 방문 처리

print(count)   # 출력
