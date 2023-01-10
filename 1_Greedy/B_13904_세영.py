#메모리 : 30616KB 시간 : 44ms

import sys

# n : 과제의 수
# tasks : 과제들의 마감기한 d와 과제점수를 입력받아 저장할 2차원 배열
# result : 제출할 과제들의 점수를 저장할 배열 
n = int(sys.stdin.readline().rstrip())
tasks = []
result = []

# tasks 배열 입력 받음. 
for i in range(n):
    tasks.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 마감 기한이 빠른 순서대로 rsult에 넣어가는데, 이때 result의 길이가 
# 비교하는 과제의 마감기한과 같으면, 현재 result에서 가장 작은 값과 현재 과제의 점수와 비교하여
# 현재 과제 점수가 더 크면 result의 min값을 버리고 현재 과제를 선택한다.
# result 배열의 길이가 현재 비교하는 과제의 마감기한까지의 숫자와 같지 않다면
# 버릴 과제 없이 과제를 수행할 수 있다는 것이므로 현재 과제의 점수만 result 배열에 추가한다.
# min_val은 과제를 한 번 비교할 때 마다 현재 result의 최솟값으로 업데이트한다.


# tasks 배열을 과제 마감기한이 빠른 순서대로 정렬
tasks.sort()

# min_val : 현재 result에서 가장 작은 과제 점수의 값
min_val = tasks[0][1]

for i in range(n):
    if(len(result) == tasks[i][0]):
        if(min_val < tasks[i][1]):
            result.remove(min_val)
            result.append(tasks[i][1])
    else:
        result.append(tasks[i][1])
    
    min_val = min(result)
        
# result 배열에 최종 저장된 과제 점수들의 합을 출력
print(sum(result))
