#메모리 : 30616KB, 시간 : 36ms

#백준 1339번, 단어 수학
#

# n : 단어의 개수
# words : 입력받은 알파벳을 숫자로 변환한 값을 저장한 리스트 -> 'A'부터 0의 값을 배정받아 저장됨, 'GCF'의 경우 : [6, 2, 5]의 형태로 저장
# alpha : 알파벳 리스트

n= int(input())
words = [list(map(lambda x: ord(x)-65, input().strip())) for i in range(n)]
alpha = [0]*26

#입력받은 문자열 순서대로 하나씩  비교해가며
for i in range(n):
    j = 0
    #그 문자열의 맨 끝 부터 10의 제곱수만큼 곱해서 alpha 배열에 추가
    for k in words[i][::-1]:
        alpha[k] += (10 ** j)
        j += 1

#alpha 배열을 내림차순으로 정렬 -> 값이 가장 큰 값부터 9의 숫자를 배당해줘야 하기때문
alpha.sort(reverse=True)

answer = 0
cnt = 9

for i in range(26):
    #툭정 인덱스 값이 0이 되면 그 다음부터 인덱스가 전부 0이므로 반복문 종료
    if alpha[i] == 0:
        break
    #9부터 차례대로 값을 할당하여 숫자의 합을 더해나감
    answer += cnt * alpha[i]
    cnt -=1

print(answer)