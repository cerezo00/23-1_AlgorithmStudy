#메모리 : 30616KB 시간 : 36ms

import sys

# n : 책의 개수
# m : 한 번에 들 수 있는 책의 개수
# posions : 책의 위치를 입력받아 리스트로 저장
# list1과 list2는 음수와 양수를 구분지어 list1에는 position의 양수 부분만, list2에는 positions의 음수 부분만 저장
# result : 책을 모두 제자리에 나눌 때 드는 최소 걸음 수
n, m = map(int,input().split())
positions = list(map(int, sys.stdin.readline().rstrip().split()))
list1 = []
list2 = []
result = 0

# positions에 0을 추가하고 오름차순 정렬하여
# 0의 위치를 알아낸 후
positions.append(0)
positions.sort()
zIndex = positions.index(0)

# 0의 위치를 기준으로 list1과 list2에 양수와 음수만을 각각 구분지어 저장
list2 = positions[:zIndex]
list1 = positions[zIndex+1:]

# 양수 부분은 내림차순으로 정렬
list1.sort(reverse=True)

# 오름차순 정렬되어 있는 음수 부분 리스트 list2의 원소 값을 
# 전부 절댓값을 씌워 저장한다 
# 이는 양수 내림차순 정렬의 결과와 같아짐
for i in range(len(list2)):
    list2[i] = abs(list2[i])

# list1과 list2 중 원점으로 부터 가장 멀리 떨어져있는 위치가 존재하는 리스트를 tmp1에, 다른 리스트를 tmp2에 저장하는 조건문
# 한 쪽 리스트가 없는 경우를 대비하여 없는 쪽의 리스트는 tmp2에 빈리스트를 저장하고, 있는 쪽의 리스트를 tmp1에 저장하도록 한다.
# list1[0]과 list2[0]을 비교하는 조건문 전에 빈 리스트를 저장하는 조건문이 있어야함에 주의
if len(list1) ==0:
    tmp2 = []
    tmp1 = list2[:]
elif len(list2) == 0:
    tmp2 = []
    tmp1 = list1[:]
elif list1[0] > list2[0]: 
    tmp1 = list1[:]
    tmp2 = list2[:]
else:
    tmp1 = list2[:]
    tmp2 = list1[:]

# 이 문제 풀이 아이디어는 음수 양수 양쪽을 기준으로 가장 멀리 떨어진 부분부터 m 개의 위치에 대해서는
# 책을 두고 다시 원점으로 돌아올 필요가 없다는 것이다.
# 즉, 원점에서 가장 멀리 있는 지점까지 m개의 위치에 대해서는 책을 마지막에 들고가서 차례대로 책을 두고 와야 최소 걸음수로 책을 제자리에 놔둘 수 있다는 것이다.
# 그래서 위의 조건문으로 가장 멀리 있는 지점이 존재해있는 tmp1의 리스트의 첫 번째 값(절댓값 기준으로 내림차순 정렬되어 있으므로)은 
# 곱하기 2 없이 그 값만 한 번 먼저 result에 더해준 후 tmp1을 슬라이싱 
result += tmp1[0]
tmp1 = tmp1[m:]

# 나머지 위치들은 책을 가져다 두고 다시 원점으로 되돌아 와야 하므로
# 남아 있는 위치들이 없어질 때까지 현재 위치의 가장 멀리 떨어진 부분부터 m권씩 책을 제자리에 두고 온다
# -> max(tmp1) *2 
# 두고 온 책들의 위치는 슬라이싱으로 없앰
while True:
    if len(tmp1) ==0:
        break
    result += max(tmp1)  * 2
    tmp1 = tmp1[m:]
    
# tmp2의 리스트에 대해서도 마찬가지로 수행
while True:
    if len(tmp2) == 0 :
        break
    result += max(tmp2) * 2
    tmp2 = tmp2[m:]

    
print(result)