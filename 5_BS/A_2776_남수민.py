# 2776. 암기왕
# 7516ms

import sys
input = sys.stdin.readline

for _ in range(int(input())):

    # 수첩1 : BS를 수행하기 위하여 정렬
    size_1 = int(input())
    array_1 = sorted(list(map(int, input().split())))

    # 수첩2
    size_2 = int(input())
    array_2 = list(map(int, input().split()))

    # 정답여부
    check = []

    # BS : 수첩2의 수를 수첩1에서 이분탐색
    for num in array_2:
        l = 0
        h = size_1 - 1

        while l <= h:
            m = (l + h) // 2
            if array_1[m] < num:
                l = m + 1
            elif array_1[m] > num:
                h = m - 1
            else:
                break

        # 정답 여부 추가
        if l > h:
            check.append(0)
        else:
            check.append(1)

    # 결과 출력
    print(*check, sep='\n')