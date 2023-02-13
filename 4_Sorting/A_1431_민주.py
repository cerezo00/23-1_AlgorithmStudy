# 1431 시리얼 번호
# 메모리 31256KB 시간 44ms
# 시리얼 번호 순서대로 정렬
# 1. 길이가 짧은 것부터
# 2. 자리수 합이 작은 것부터hh
# 3. 사전순

import sys
input = sys.stdin.readline

N = int(input())       # N : 기타의 개수
serial_number = []     # 시리얼 번호 N개
for _ in range(N):
    serial_number.append(input().rstrip())

def sum_digit(k):      # 자릿수 합 계산
    digit = 0          # 자릿수 저장
    for i in k:
        if i.isdigit(): # 수가 숫자이면
            digit += int(i) # 자리수 합에 추가
    return digit       # 반환

serial_number.sort(key=lambda x:(len(x), sum_digit(x), x))
# sort 정렬 (길이 순, 자릿수 합 순, 사전 순)

for i in serial_number:
    print(i)             # 한 줄씩 출력
