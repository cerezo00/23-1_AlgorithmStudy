# 30616kb 84ms
# 2303번 숫자게임
# 일의 자리가 가장 크게 5장의 카드 중 3개를 고른다. 일의 자리가 가장 큰 사람을 출력

from itertools import combinations

n = int(input())
answer =[]

for i in range(n):
    numbers = list(combinations(list(map(int, input().split())),3))
    score = 0
    for number in numbers:
        tmp = sum(number)%10
        score = max(score, tmp)
    answer.append((score, i+1))

## 2차원 배열 정렬
# 우선 일의자리수가 가장 큰 사람을 뽑는데 만일 가장 큰수가 두명 이상이면 번호가 가장 큰 사람의 번호를 출력하므로
# 일의자리수 : 내림차순 정렬, 순서 : 내림차순 정렬 필요
# x: ( ) 의 괄호안에 튜플 형식으로 집어넣는다. 이 때 -를 하게되면 역으로 정렬시킬 수 있다.
# 여기서는 0번째 인덱스에 대해 내림차순 정렬 한 뒤, 동일 값의 경우 내림차순으로 재정렬

answer = sorted(answer, key=lambda x: (-x[0], -x[1]))
print(answer[0][1])
