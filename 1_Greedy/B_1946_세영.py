#메모리 : 50428KB 시간 : 5104ms 

# 문제를 풀이하기에 앞서, 이 문제는 입력값이 큰 문제로, input()을 이용해 입력을 받으면 시간초과가 발생한다.
# 그러므로 sys 모듈을 불러와 sys.stdin.readline()으로 입력을 받아야 함에 주의.
import sys

# t : 테스트 케이스의 수
t = int(sys.stdin.readline().rstrip())

# n : 지원자의 수
# socres : 1열에 각 지원자들의 서류심사 성적의 순위를, 2열에 각 지원자들의 면접 성적 순위를 저장한 2차원 배열
# cnt : 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수

# 아 문제의 해결 아이디어는 우선 서류심사 성적 순위로 정렬하면 면접 성적의 순위는 본인의 앞 순서의 면접 성적과만 비교하면 된다는 것이다.
# 서류심사 성적 순위가 본인보다 앞인 사람들 중에서 면접 성적이 본인보다 더 높은 사람이 한 명이라도 있으면 부적절한 지원자로 간주하면 된다.
# 그래서 서류심사 성적을 기준으로 오름차순 정렬 후, 면접 성적 순위에 대해서 
# 현재 비교하는 지원자의 앞 사람들중 가장 낮은 순위를 기억하여 이 순위보다 현재 비교하는 지원자의 면접심사 순위가 더 낮다면,
# 본인 보다 서류심사 순위도 높고, 면접심사 순위도 높은 사람이 존재한다는 뜻이므로 채용할 수 있는 신입사원의 수를 1씩 빼나간다.

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    scores = []
    cnt = n
    for j in range(n):
        scores.append(list(map(int, sys.stdin.readline().rstrip().split())))

    scores.sort()
    min_val = scores[0][1]

    for k in range(1,n):
        if min_val < scores[k][1]:
            cnt -= 1
        else:
            min_val = scores[k][1]
    print(cnt)