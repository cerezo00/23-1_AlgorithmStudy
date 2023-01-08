# 13904 과제 : 메모리 30616KB, 시간 36ms

# 접근법
# 1. 방향 수립
#    : 점수의 최댓값을 찾는 문제 -> "점수"를 기준으로 해결
# 2. 조건 적용
#   1) 점수만 고려 (마감일 조건 X)
#      : 점수를 내림차순 정렬하여 고점부터 합산
#   2) 마감일 고려
#      : 과제를 가능한 최대한 늦게 수행
#      -> 과제를 수행할 때는 자신보다 마감일이 짧은 과제만 고려하면 됨
#         (마감일이 더 긴 과제는 다음날 수행해도 되므로)
# 3. 구현
#   1) (마감일, 점수) DataSet을 점수를 기준으로 내림차순 정렬한다.
#   2) 점수가 높은 순서대로 가능한 제일 마지막 날에 수행한다.
#   3) 마감일에 다른 과제가 있다면, 그 전날 중 비어 있는 날에 수행한다.

# num := 과제의 수
num = int(input())

# homework := 과제 별 마감일, 점수] 리스트
# Tip : append() 보다 인덱스 접근의 속도가 더 빠르다.
homework = [0] * num
for i in range(num):
    homework[i] = list(map(int, input().split()))

# 점수의 최댓값을 구해야 하므로 점수에 대하여 내림차순 정렬
homework.sort(key=lambda x: x[1], reverse=True)

# score_by_day := {날짜: 점수} 딕셔너리
# ㄴ [1] 첫째날 점수, [2] 둘째날 점수, ...
score_by_day = dict()

# deadline := 과제 마감일
# score := 점수
for deadline, score in homework:
    # day := 현재 과제를 수행할 날짜
    #    ex) deadline == 4일 경우 최소한 넷째날 까지는 수행해야 한다.
    # 만약 day번째 날에 다른 과제를 해야한다면, 하루씩 앞당기면서 빈 날짜 탐색
    for day in range(deadline, 0, -1):
        if not(day in score_by_day):
            score_by_day[day] = score
            break  # 빈 날짜를 찾았으므로 반복문 탈출

# result := 각 날짜 별 획득한 점수의 총합
result = sum(score_by_day.values())
print(result)
