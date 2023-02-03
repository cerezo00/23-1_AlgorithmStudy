#30616	40

# n x m 크기의 바닥
# room : 바닥 장식을 담을 배열
n, m = map(int,input().split())
room=[]

for i in range(n):
    room.append(list(input()))

# cnt : 필요한 나무 판자의 개수
# check : 나무 판자의 개수를 확인해갈 bool 변수
cnt = 0
check = False

# 가로 방향으로 위에서부터 한 줄씩 '-' 모양의 바닥 장식의 개수를 세어나감
for i in range(n):
    # 새로운 줄마다 check변수 초기화
    check = False
    for j in room[i]:
        #현재 바닥 장식이 '-'이고 check 변수가 True이면 
        #계속해서 판자의 길이를 넓혀나감 (continue)
        if(j=='-' and check==True):
            continue
        #현재 바닥 장식이 '-'이고 check 변수가 False이면 
        #지금부터 새로운 가로방향의 나무 판자가 시작되는 것이므로 check변수를 True로 바꿔줌
        elif(j=='-' and check==False):
            check = True
        #현재 바닥 장식이 '|'이고 check 변수가 True이면 
        #계속 세어 왔던 가로방향의 나무 판자가 끝나고 세로 방향의 나무 판자가 시작된 것이므로 
        #cnt 를 +1 해주고 다시 가로 방향의 나무 판자를 세어나가기 위하여 check변수를 False로 바꿔줌
        elif(j=='|' and check == True):
            cnt += 1
            check = False
        #현재 바닥 장식이 '|'이고 check 변수가 False이면 
        #가로 방향의 바닥 장식을 찾아나감 (continue)
        else:
            continue
    #한줄이 끝나는데 이때 check가 True이면 cnt를 +1
    if(check == True):
        cnt+=1

# 세로 방향으로 왼쪽 줄부터 한 줄씩 '|' 모양의 바닥 장식의 개수를 세어나감
# 방법의 위의 for문과 동일
for i in range(m):
    check = False
    for j in range(n):
        tmp = room[j][i]
        if(tmp=='|' and check==True):
            continue
        elif(tmp=='|' and check==False):
            check = True
        elif(tmp=='-' and check == True):
            cnt += 1
            check = False
        else:
            continue
    if(check == True):
        cnt+=1

print(cnt)