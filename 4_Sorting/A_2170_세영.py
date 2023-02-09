import sys
input = sys.stdin.readline

# N : 선을 그은 횟수
# points : 선을 그을 때 선택한 두 점의 위치 x, y를 저장할 배열
# result : 그은 선의 총 길이
N = int(input())
points = []
result = 0

# 두 점의 위치 x, y를 입력받아 points에 저장한 후 
# x와 y를 순서대로 기준으로 하여 정렬한 배열을 arr 배열에 저장
for i in range(N):
    points.append(list(map(int,input().split())))
arr = sorted(points,key=lambda x : (x[0],x[1]))

# 현재 x값과 r값을 cur과 end에 저장하고, 이 값으로 다음 시작 지점과 현재 끝 부분의 위치를 비교해나감
cur = arr[0][0]
end = arr[0][1]

# 만약 현재 end값, 즉 선의 끝부분의 위치가 다음 선을 그을 x 위치값보다 작다면
# 기존의 선이 끊어지고 새로운 선으로 시작해야 하므로 result에 기존의 선의 길이룰 더하고
# cur은 다음 위치의 x값으로, end값은 다음 위치의 y값으로 업데이트
# 만약 end가 더 크거나 같고, 다음 y 위치가 end보다 크다면 end를 다음 y위치로 변경 
# 선의 길이가 길어진 것이 된다. 
# 만약 end가 더 크거나 같고, 다음 y 위치가 end보다 작다면 현재 그어진 선에 새로운 선이 겹쳐서 포함되는 것이므로
# 아무런 동작을 하지 않아도 된다.
for i in range(len(arr)-1): 
    if end < arr[i+1][0]:
        result+=end-cur
        cur = arr[i+1][0]
        end = arr[i+1][1]
    if end >= arr[i+1][0]:
        if end < arr[i+1][1]:
            end = arr[i+1][1]

# 마지막 그어진 선의 길이를 result에 한번 더 더해주고 출력한다.
result+=end-cur

        

print(result)
