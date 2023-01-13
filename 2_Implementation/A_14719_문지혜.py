## 14719 빗물
## 비가 오면 블록 사이에 빗물이 고인다
## 고이는 빗물의 총량 구하기

h, w = map(int,input().split())  ## 2차원 세계의 세로, 가로
blocks = list(map(int, input().split()))  ## 블록이 쌓인 높이

# 양쪽에 더 높은 블록이 존재하면 빗물이 고인다.
## 자기 자신을 둘러싼 왼,오른쪽 중 더 낮은 블록까지 빗물이 고이다.
## 블록을 기준으로 코드를 짜야함
result = 0 # 빗물의 고인 양

for i in range(1, w-1): # 맨 왼쪽과 맨 오른쪽에는 고일 수 없다.
    left_max = max(blocks[:i]) # 처음부터 i까지 중 제일 높은 블록
    right_max = max(blocks[i+1:]) # i 다음부터 끝가지 중 제일 높은 블록

    lower_one = min(left_max, right_max) # 이 둘 중 작은 블럭을 선택한다.

    if blocks[i] < lower_one : # 현재 블록이 lower_one 보다 작아야 빗물이 고인다.
        result += lower_one - blocks[i]

print(result)