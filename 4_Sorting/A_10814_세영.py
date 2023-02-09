#59588	380

import sys
input = sys.stdin.readline

# N : 회원의 수
# users : 회원의나이, 이름 가입 순서를 순서대로 저장할 배열 
N = int(input().strip())

users = [[0]*3 for _ in range(N)]

# 회원의 나이, 이름, 가입 순서를 저장
for i in range(N):
    users[i][0], users[i][1] = map(str, input().split())
    users[i][0] = int(users[i][0])
    users[i][2] = i

#나이, 가입 순서를 차례대로 기준으로 하여 정렬
users.sort(key=lambda x:(x[0],x[2]))

# 나이와 이름만 출력
for i in range(N):
    print(users[i][0], users[i][1])