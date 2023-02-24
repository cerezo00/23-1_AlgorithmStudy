#30840	76

import sys
input = sys.stdin.readline


# N : 집의 수
# RGB : 집을 칠하는 비용
N = int(input())

RGB = []

for i in range(N):
    RGB.append(list(map(int, input().strip().split())))

# RGB의 0, 1, 2 의 인덱스의 값에 i번째의 집을 R, G, B로 칠했을 때의 최솟값을 저장해나간다.
for i in range(1,N):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

print(min(RGB[N-1]))