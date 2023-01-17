#30616   96

from itertools import combinations

# n : 숫자 게임을 하는 사람의 수
# arr : n명의 5개의 카드 숫자들이 저장되는 배열

n  = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

# best_combi : solution 이라는 함수를 통해 얻어진 각 사람마다 5개의 카드 중 3개를 뽑아 만들어질 수 있는
# 합의 일의 자리 숫자들

best_combi = []

# solution : 5개의 숫자 카드를 넘겨받아 combinations를 이용하여 가능한 3개의 조합을 모드 tmp에 저장한 후
# 모든 조합들의 합을 tmps에 string 형태로 저장한다. 이때 string 형태로 저장한 이유는 인덱싱을 사용하여
# 일의 자리 숫자만을 뽑아내어 sum_tmp에 int로 변환하여 저장한 후 return 하도록 하기 위함이다. 
def solution(lst):
    tmp = combinations(lst,3)
    sum_tmp = []
    for i in tmp:
        #print(i)
        tmps = str(sum(i))
        tmps2 = tmps[(len(tmps))-1]
        sum_tmp.append(int(tmps2))

    return sum_tmp

# n명의 카드들에 대해 solution을 실행하여 best_combi 배열에 가능한 일의자리의 숫자들을 저장
for i in range(len(arr)):
    best_combi.append(solution(arr[i]))

# max_result : best_combi에 들어가 있는 n명의 가능한 일의 자리 숫자들중 가장 큰 값만을 꺼내어 max_result에 저장
max_result = []

for i in range(len(arr)):
    max_result.append(max(best_combi[i]))

# 같은 값을 가졌으면 숫자 번호가 큰 사람의 번호를 출력해야 하기 때문에 뒤에서 부터 가장 큰 값을 찾아
# 찾으면 그 숫자의 번호를 출력하고 break 문으로 빠져나옴

max_answer = max(max_result)
max_reverse = list(reversed(max_result))

for i in range(len(max_reverse)):
    if(max_reverse[i] == max_answer):
        print(len(max_result)-i)
        break

