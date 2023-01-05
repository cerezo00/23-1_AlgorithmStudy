# 1541 잃어버린 괄호
# 최솟값을 만드려면, - 부호를 기준으로 괄호 치기
# - 부호를 기준으로  분할, - 부호 등장 전 수들은 + 부호 기준으로 분할 후 더하여 result에 저장
# for문) + 부호를 기준으로 분할하여 수를 더하고, 더한 값을 result에서 뺄셈

x = (input().split('-'))   # -를 기준으로 분할, +로만 구성된 식

result = sum(map(int, x[0].split('+')))   # +를 기준으로 분할하여 덧셈 계산 -> result에 저장

for i in range(1, len(x)):  # 반복문 1부터 끝까지
	result -= sum(map(int, x[i].split('+')))  # +부호를 기준으로 분할하여 수를 더한 값을 result에서 빼기 
print(result)   # 최솟값 출력 
