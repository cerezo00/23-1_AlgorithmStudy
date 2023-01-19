#30616	236

import sys
from itertools import combinations

input = sys.stdin.readline

# N : N * N 의 도시 크기
# M : 최대 M개의 치킨집만 남겨둘 수 있음
# arr : 도시 전체의 위치 정보
# chickens : 모든 치킨 짐의 위치 정보
# house : 모든 집의 위치 정보

N, M = map(int,input().split())
arr = []  
chickens = [] 
house= [] 

# 도시 정보를 입력받음과 동시애 치킨 집의 위치 정보와 집의 위치 정보를 
# 각각 chickens와 house 배열에 추가한다.

for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(N):
        if arr[i][j]== 2:
            chickens.append([i,j])
        if arr[i][j] == 1:
            house.append([i,j])

# Point_distance : 특정 집의 위치에서 가장 가까운 치킨집과의 거리를 return
def Point_distance(lst,x1,y1):
    points = lst[:]
    min_dis = abs(x1-points[0][0])+abs(y1-points[0][1])
    for i in range(1,len(points)):
        temp =abs(x1-points[i][0])+abs(y1-points[i][1])
        if(min_dis > temp):
            min_dis = temp
        else:
            continue
    return min_dis

# 치킨집의 위치 정보가 담겨있는 chickens 배열에서 최대 M개의 조합을 꺼내어 
# 모든 조합에서의 치킨 거리를 계산하여 치킨 거리를 최솟값으로 업데이트 해나간다.
def min_distance():
    
    min_distances= 99999
    
    tmp = list(combinations(chickens,M))

    for i in range(len(tmp)):
        min_sum = 0
        for j in range(len(house)):
            min_temps = Point_distance(tmp[i],house[j][0],house[j][1])
            min_sum += min_temps
        if(min_distances > min_sum):
            min_distances=min_sum

    print(min_distances)

min_distance()
