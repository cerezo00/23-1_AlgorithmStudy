#34820	128

import sys, re
input = sys.stdin.readline

# N : 기타의 개수
# serials : 시리얼 번호를 저장할 배열
N = int(input())
serials  = []

# N번에 걸처 시리얼 번호를 입력 받은 후 시리얼 번호에서
# 숫자만 추출하여 numbers에 저장
# numbers의 각자리 숫자들을 더하여 sums에 저장 후 
# serials 배열에 입력받은 시리얼 번호 원문, 시리얼 번호의 길이, sums를 차례대로 append
for i in range(N):
    Snumbers=input().strip()
    numbers = re.sub(r'[^0-9]', '', Snumbers)
    sums = 0
    for j in range(len(numbers)):
        sums += int(numbers[j])
    serials.append([Snumbers, len(Snumbers),sums])

# 전부 저장한 serials에 대하여 길이, sums의 값, 시리얼 번호의 사전 순서를 기준으로 
# 차례로 정렬하여 result 배열에 저장
result = sorted(serials,key=lambda x : (x[1],x[2],x[0]))

# 정렬된 시리얼 번호들의 원래 시리얼 번호만 차례대로 출력
for i in result:
    print(i[0])