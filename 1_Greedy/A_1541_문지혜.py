## 메모리 30616KB 시간 36ms

math = input().split('-')  ## 최솟값을 만들기 위해서는 - 를 기준으로 괄호를 치면 된다.
num = []  #'-'로 나눈 항들의 합을 저장할 리스트

for i in math: ## 반복문으로 식을 돌면서
    sum = 0
    tmp = i.split('+') ## 덧셈을 먼저 하기 위해 '+'를 기준으로 split
    for j in tmp: ## split 한 리스트의 각 요소들을 더한다.
        sum += int(j)
    num.append(sum) ## 각 항의 연산 결과(덧셈)을 num 에 저장

n=num[0]  ## 식의 제일 처음은 숫자로 시작하므로 0번째 값에서 나머지 값을 빼준다.

for i in range(1, len(num)):  ## 1번째 값부터 n에서 빼준다.
    n -= num[i]

print(n)

