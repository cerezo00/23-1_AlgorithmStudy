# 1339 단어수학 : 메모리 30616KB 시간 36ms

# 접근법
# 1. 각 알파벳이 등장하는 자릿값의 합을 value[26] 리스트에 저장한다.
#   ㄴ 알파벳이 frequency 정보도 함께 저장된다.
# 2. 가장 큰 value 값을 갖는 알파벳부터 높은 숫자를 부여한다.
#   ㄴ value 리스트를 내림차순 정렬하고,
#   ㄴ 원소에 (9 ~ 1)를 곱셈

# N := 단어의 개수
# words := 단어 리스트
# value := 알파벳 별 자릿값 총합
N = int(input())
words = list(input() for _ in range(N))
value = list([0] * 26)

# digit := 자릿수
# 각 단어에 대하여, 한 글자씩 순회하며 value 계산
# 몇자리인지 모르기 때문에 단어를 역정렬하여, 1의 자리부터 계산
#  ㄴ ex) ABC -> CBA -> C=1, B=10, A=100 (digit = 1->10->100)
for word in words:
    digit = 1
    for char in reversed(word):
        value[ord(char) - ord('A')] += digit
        digit *= 10

# result := 결과값
# value가 큰 순서대로 (9 ~ 1)을 부여하기 위해 내림차순 정렬
# 즉, result에 (value * 부여된 숫자)를 누적합한다.
value.sort(reverse=True)
result = 0
for i in range(10):
    if value[i] == 0:  # 가지치기
        break
    result += value[i] * (9-i)

print(result)