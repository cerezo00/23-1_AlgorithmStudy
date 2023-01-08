# 메모리 30616 KB, 시간 36ms 
# 1339 단어 수학
# 가장 큰 자릿수에 위치한 알파벳부터 차례대로 (9부터) 맵핑
N=int(input())
words = []    # 입력한 단어 저장할 배열
for _ in range(N):
  words.append(input())   # 단어 입력하여 words에 저장

dict = {}  # 딕셔너리 초기화

for word in words:           # 딕셔너리에 알파벳별로 값 저장
  square = len(word) - 1     # 1의 자리는 0제곱이므로 -1
  for i in word:
    if i in dict:            # 값이 있다면
      dict[i] += pow(10, square) # 자릿수로 제곱하여 dict에 저장
    else:                    # 값이 없다면
      dict[i] = pow(10, square)  # 그대로 저장
    square -= 1              # square에서 -1 (제곱근)

dict = sorted(dict.values(), reverse=True)    #내림차순 정렬
result = 0   # 결과값 저장
k = 9        # 큰 값부터 계산

for value in dict:
  result += value * k    # 값 계산하기
  k -= 1
print(result)


