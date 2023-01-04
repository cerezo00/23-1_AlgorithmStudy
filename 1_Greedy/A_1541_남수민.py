# 접근법
# 1. +, - 만으로 구성
# 2. - 사이에 괄호를 친다.
# 3. 즉 +를 먼저 계산한다.

# eq_plus := -를 기준으로 분할한 +로만 구성된 식
equation = input()
eq_plus = equation.split('-')

# result_plus := 각 eq_plus 식들의 계산 결과
result_plus = list()
for eq in eq_plus:
    result_plus.append(sum(list(map(int, eq.split('+')))))

# result := 결과
# 첫 번째 값에서 나머지 값들을 모두 뺄셈
result = result_plus[0] - sum(result_plus[1:])

print(result)