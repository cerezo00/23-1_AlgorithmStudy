# 2303 숫자 게임
# 메모리 30616KB, 시간 48ms

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())    # N : 사람 수
high = 0            # 세 사람이 조합한 자신의 일의 자리 수 중 가장 큰 값 저장
result = 0          # 일의 자리가 가장 큰 사람의 번호 저장

for i in range(1, N+1):   # 각 사람별로 카드 세장을 뽑아 일의 자리 최댓값 구하기
    card = list(map(int, input().split()))  # i번째 사람이 가진 카드 입력
    high_digit = 0    # 일의 자리 가장 큰 값

    for k in combinations(card, 3):   # 자신이 가진 카드 중 3개 조합
        high_digit = max(high_digit, sum(k) % 10)
        # high_digit 값과 현재 뽑은 수 합의 일의 자리 수 중 더 큰 값을 high_digit에 저장

    if high_digit >= high:   # high 값과 크거나 같다면 (다른 사람의 값과 비교)
        high = high_digit    # high에 값 저장 (1번 사람부터 계산하므로 이긴 사람이 두 명 이상이여도 큰 번호 출력)
        result = i           # result에 i 저장 (승리한 사람 번호)
print(result)   # 결과 출력
