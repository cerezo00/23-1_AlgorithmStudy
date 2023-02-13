# 1431. 시리얼 번호
# 44ms

# 접근법
# 1. 파이썬의 다조건 정렬
#   (1) key=lambda x: (func1(x), func2(x), func3(x))
#   (2) array[조건1][조건2][조건3] 일 때, array.sort()
# 2. 정렬 조건에 따라 배열을 생성
#   ㄴ 조건1. 문자 길이 : serial[i][0]
#   ㄴ 조건2. 숫자의 합 : serial[i][1]
#   ㄴ 조건3. 사전 정렬 : serial[i][2]

n = int(input())
serial = [[0, 0, ''] for _ in range(n)]

for i in range(n):
    serial[i][2] = input()  # 입력 및 조건1
    serial[i][1] = sum(int(x) for x in serial[i][2] if x.isdigit())  # 조건2
    serial[i][0] = len(serial[i][2])  # 조건3

serial.sort()  # 정렬

print(*list(zip(*serial))[2], sep='\n')  #출력