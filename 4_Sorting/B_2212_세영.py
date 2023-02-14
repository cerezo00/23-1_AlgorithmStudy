import sys
input = lambda: sys.stdin.readline().rstrip()

#32276	48
import sys
input = lambda: sys.stdin.readline().rstrip()

N= int(input())
K = int(input())
senser_posi = list(map(int, input().split()))

senser_posi.sort()


diffs = []
for i in range(N-1):
    diffs.append(senser_posi[i+1]-senser_posi[i])

diffs.sort()

print(sum(diffs[:N-K]))
