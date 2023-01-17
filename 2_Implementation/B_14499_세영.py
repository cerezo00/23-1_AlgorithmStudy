#30616	36

# n :
# m :
# k :
# maps :
# directions :

n, m, x, y, k = map(int,input().split())
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))
directions = list(map(int,input().split()))

dice=[0,0,0,0,0,0] # 주사위를 놓고 정면에서 바라봤을 때의 면을 기준으로 순서대로 아랫면, 앞면, 윗면, 뒷면, 왼쪽면, 오른쪽면에 대해 인덱스를 부여

# cur_x, cur_y : 현재 맵 위에서의 주사위의 위치, x와 y로 초기화 시킴
cur_x = x
cur_y = y

# 이동 명령의 수 k 만큼 for문을 수행
# 방향 명령이 동, 서, 남, 북 이렇게 4가지 이므로 이 4가지에 대하여 if문을 사용해 주사위를 굴려줌
# 이때 굴리기 전 만약 굴렸을 대 maps 범위를 나가게 된다면 아무런 행동도 하지 않고 continue문으로 다음 방향 명령을 수행하게 됨

for i in range(k):

    # 방향이 1이라면 주사위를 동쪽으로 굴리는 것이다
    if(directions[i]==1):
        if(cur_y + 1 < m):
            
            # 동쪽으로 굴리게 되면 maps의 배열에서 y값이 변하는 것이므로 cur_y의 값에 1을 더해 위치를 옮겨주고
            cur_y = cur_y+1

            # 주사위를 굴려준다.
            # 동쪽으로 굴리는 상황의 주사위를 생각해보면 아랫면이 오른쪽으로 구르게 되면서 구른 후에 왼쪾면이 되고,
            # 윗면은 오른쪽 면, 왼쪽면은 윗면, 오른쪾면은 아랫면이 된다. 나머지 면은 위치 동일
            dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
            
            # 굴려서 이동한 위치의 maps에 써진 값이 0이면 위치의 maps에 써진 값을 현재 주사위의 아랫면 값으로 복사하고
            if( maps[cur_x][cur_y] == 0):
                maps[cur_x][cur_y] = dice[0]

            # 0이 아니라면 현재 주사위의 아랫면에 현재 maps의 위치에 써진 값을 복사하고
            # maps의 위치에 0을 쓴다
            else:
                dice[0] = maps[cur_x][cur_y]
                maps[cur_x][cur_y] =0

            
            #그리고 현재 주사위의 윗면을 출력
            print(dice[2])
        else: 
            continue

    elif(directions[i]==2):
        
        if(cur_y -1 >= 0):

            cur_y = cur_y-1
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
            if( maps[cur_x][cur_y] == 0):
                maps[cur_x][cur_y] = dice[0]

            else:
                dice[0] = maps[cur_x][cur_y]
                maps[cur_x][cur_y] =0
            print(dice[2])

        else: 
            continue
        
    elif(directions[i]==3):
        
        if(cur_x -1 >= 0):

            cur_x = cur_x -1
            dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
            if( maps[cur_x][cur_y] == 0):
                maps[cur_x][cur_y] = dice[0]

            else:
                dice[0] = maps[cur_x][cur_y]
                maps[cur_x][cur_y] =0
            print(dice[2])
        else: 
            continue

    else:
        
        if(cur_x+1 < n):

            cur_x = cur_x +1
            dice[0], dice[3], dice[1], dice[2] = dice[3], dice[2], dice[0], dice[1]
           
            if( maps[cur_x][cur_y] == 0):
                maps[cur_x][cur_y] = dice[0]

            else:
                dice[0] = maps[cur_x][cur_y]
                maps[cur_x][cur_y] =0
            print(dice[2])      
        else: 
            continue
    
    

       
   