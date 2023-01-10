# 13904 과제
# 메모리 30616 KB, 시간 40ms
# 과제 마감일, 과제 점수 -> 받을 수 있는 점수의 최댓값
# 점수 내림차순 정렬 -> 높은 점수는 최대한 기한 마지막날에 수행
# 마감일에 다른 처리해야할 과제가 있다면 그 이전 날 중 수행
import sys
input = sys.stdin.readline

N = int(input())  # 정수 N 입력
arr = []  # 과제 마감일 점수 저장할 배열
result = 0   # 받을 수 있는 점수의 최댓값 저장할 변수
check = [0 for i in range(1001)]  # 과제 처리 완료 여부 확인

for i in range(N):
    d, w = map(int, input().split())   # d:과제 마감일까지 남은 일수, w: 과제의 점수
    arr.append((d, w))     # d,w를 homework에 저장
arr.sort(reverse=True, key=lambda x: x[1])  # 내림차순 정렬

for date, score in arr:   # arr에서 탐색
    while date > 0 and check[date]!=0: # 과제를 할 날짜 탐색
        date -= 1          # 그 이전 날짜로
    if date != 0:         # 가능한 과제가 있다면
        check[date] = True   # 날짜 i에 처리하는 것으로 저장
        result += score   # result에 score값 더함
print(result)  # 최댓값 출력
