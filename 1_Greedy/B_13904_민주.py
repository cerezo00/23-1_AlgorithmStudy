# 13904 과제
# 메모리 30616 KB, 시간 36ms
# 과제 마감일, 과제 점수 -> 받을 수 있는 점수의 최댓값

import sys
N = int(sys.stdin.readline())  # 정수 N 입력
homework = []  # 과제 마감일 점수 저장
visit = [False] * 1001  # 과제 완료 여부 확인

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())   # d:과제 마감일까지 남은 일수, w: 과제의 점수
    homework.append((d, w))     # d,w를 homework에 저장

homework.sort(key=lambda x: x[1], reverse=True)  # 내림차순 정렬
result = 0   # 받을 수 있는 점수의 최댓값 저장할 변수

for date, score in homework:   # homework에서 탐색
    i = date
    while i > 0 and visit[i]: # 과제를 할 날짜 탐색
        i -= 1
    if i == 0:         # 과제할 날짜가 없으면
        continue      # 넘기기
    else:             # 과제할 날짜가 있으면
        visit[i] = True   # True로 저장
        result += score   # result에 score값 더함

print(result)  # 최댓값 출력
