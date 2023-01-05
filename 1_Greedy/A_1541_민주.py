temp = list(input().split('-')) # -를 기준으로 분할, +로만 구성된 식

result = sum(list(map(int, temp[0].split('+')))) # + 계산하여 result에 저장

for i in range(1, len(temp)):  # 반복문 범위 1부터 temp 길이 끝까지
	tmp = list(map(int, temp[i].split('+')))
	result -= sum(tmp)
print(result)
