# 1946 신입사원 : 메모리 35124 시간 2228ms

# 접근법
# 1. 모든 사람과 비교하여 Score1, Score2 중 적어도 하나가 다른 사람보다 높음
#    => A가 B보다 Score1, Score2가 모두 낮으면 불합격
# 2. N명의 사람을 각각 (N-1)명과 비교 (O(N^2)의 시간복잡도)
# 3. Score1에 대하여 오름차순 정렬
#    => Score2에 대해서만 비교하면 됨
#    => Score1은 당연히 앞사람보다 낮으니,Score2는 반드시 앞사람보다 높아야 함

# sys.stdin.readline() := 개행문자를 포함하여 한 줄씩 입력을 받는 함수
# input과의 차이점
# - input : 사용자가 문자를 입력할 때마다 하나씩 버퍼에 저장
# - readline : 데이터가 한 번에 버퍼에 저장 (속도에서 우위)
import sys
input = sys.stdin.readline

# test_case := 테스트 케이스 횟수
test_case = int(input())

for case in range(test_case):

    # num := 인원 수
    # ranks := 각 인원의 S1, S2 순위 (각 점수에서 순위는 유일하다)
    # S1을 기준으로 정렬 => 2차원 배열을 사용해야 한다.
    # ㄴ S1을 인덱스로 사용함으로써 1차원 배열 사용
    num = int(input())
    ranks = [0] * num
    for _ in range(num):
        score1, score2 = map(int, input().split())
        ranks[score1 - 1] = score2

    # pass_count := 합격자 수
    # least_rank := 다음 사람이 최소한 넘어야 하는 순위 (합격자 중 가장 높은 순위)
    # ㄴ S1을 기준으로 정렬하였으므로, S1은 반드시 앞사람보다 낮기 때문에
    #    S2는 반드시 앞 사람들보다 높아야 한다. => S2만 비교한다.
    pass_count = 1
    least_rank = ranks[0]
    for rank in ranks[1:]:
        if rank < least_rank:
            pass_count += 1
            least_rank = rank

    print(pass_count)