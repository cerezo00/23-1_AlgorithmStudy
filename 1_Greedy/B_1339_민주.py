# 메모리 30616 KB, 시간 36ms
# 1339 단어 수학
# 0-9 숫자 중 하나로 알파벳 치환
# N개의 단어 -> 그 수의 합 최대
# 가장 큰 자릿수에 위치한 알파벳부터 차례대로 (9부터) 맵핑

N=int(input())  # N : 단어 수
words = []    # 입력한 단어 저장할 배열

for _ in range(N):
  words.append(input())   # 단어 입력하여 words에 저장
result = 0   # 결과값 저장
arr = {}  # 알파벳별로 값들을 저장할 배열

for i in words:         #알파벳별로 값 저장
    sq=len(i)       # 제곱수
    for k in i:
        if k in arr:    # 값이 있으면
            arr[k] += (10 ** (sq - 1))   # 자릿수로 제곱하여 arr에 더함
        else:          # 그렇지 않으면
            arr[k] = (10 ** (sq - 1))    # 그대로 저장
        sq -= 1

arr = sorted(arr.values(), reverse=True)   #내림차순 정렬
z = 9        # 큰 값부터 계산

for num in arr:
  result += num * z    # 값 계산하기
  z -= 1               # 9부터 차례대로
print(result)            # 결과값 출력


