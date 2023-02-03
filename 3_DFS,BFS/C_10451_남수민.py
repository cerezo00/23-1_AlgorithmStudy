# 10451. 순열 사이클
# 31256KB, 164ms (main에서 실행시 236mx)

# 접근법
# 1. 모든 숫자는 서로 다른 숫자를 가리킨다.
#   > 모든 숫자는 사이클을 구성한다.
# 2. 모든 숫자를 탐색하며 visited를 이용하여 해결한다.


import sys
input = sys.stdin.readline


def sol():
    testcase = int(input())
    for case in range(testcase):
        # Input 데이터
        size = int(input())
        arr = [0] + list(map(int, input().split()))

        # 방문가능여부, 사이클카운트
        visitable = [True] * (size + 1)
        count = 0

        # 방문가능한 숫자에 대하여 사이클 탐색
        for cur in range(1, size + 1):
            if visitable[cur]:
                visitable[cur] = False
                count += 1

                # DFS와 동일한 기능 수행
                next = arr[cur]
                while visitable[next]:
                    visitable[next] = False
                    next = arr[next]

        print(count)


sol()