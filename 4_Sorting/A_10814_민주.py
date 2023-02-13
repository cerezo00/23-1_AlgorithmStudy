# 10814 나이순 정렬
# 메모리 52420 KB 시간 272 ms
# 나이순, 나이가 같으면 가입한 순
# 입력이 가입한 순서로 주어짐

import sys
input = sys.stdin.readline
N = int(input())  # N : 회원의 수
arr = []          # arr : 회원의 나이 이름

for i in range(N):
    age, name = map(str, input().split()) # 나이 이름 입력
    arr.append((int(age), name)) # 배열에 추가 int(age)

arr.sort(key = lambda x : x[0])	 # 나이순으로 정렬
for i in range(N):
    print(arr[i][0], arr[i][1])  # 나이 이름 한 줄에 출력
