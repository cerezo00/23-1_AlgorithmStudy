#31256	44

import sys
input = lambda: sys.stdin.readline().rstrip()

L = int(input())
S = list(map(int,input().split()))
n = int(input())



if n in S:
    print(0)
else:
    S.sort()
    result = 0
    i = 0
    start = 0
    end = 0
    for i in range(len(S)):
        if S[i] <= n:
            continue

        if S[i] > n :

            end = S[i] 
            break

    for i in reversed(range(len(S))):
        if S[i] >= n:
            continue

        if S[i] < n :
            start = S[i] 
            break

    result  = (n - start - 1)+((n - start - 1) * (end - n - 1))+(end - n + -1)
    print(result)