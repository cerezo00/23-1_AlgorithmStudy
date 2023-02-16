#2417
#31256	44

import sys
input = sys.stdin.readline

n = int(input().strip())


left = 0 
right = n
result = []


while left<=right:
    q = (left+right)//2
    tmp = q * q
    if tmp < n:
        left = q + 1
    else :
        result.append(q)
        right = q-1

print(result[-1])