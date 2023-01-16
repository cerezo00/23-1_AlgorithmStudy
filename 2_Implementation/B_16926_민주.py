# 16926 배열 돌리기 1
# 메모리 116884KB, 시간 560ms (pypy3)
# 배열 R번 회전 (반시계)
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
# N*M : 배열의 크기, R : 수행해야 하는 회전의 수
A = []     # 배열 A
for _ in range(N):
    A.append(list(map(int, input().split())))    # 배열 A 원소 입력

# 바깥쪽 사각형 -> 안쪽 사각형
def rotate():  # 배열 회전 
    for k in range(min(N, M) // 2):  # 범위 : 사각형 수
        x, y = k, k
        tmp = A[x][y]  # 임시로 좌표 저장할 배열 생성 (초기값)

        for j in range(k + 1, N - k):  # 왼쪽 (X값 증가, Y 고정)
            x = j  # x 좌표가 j이면
            former = A[x][y]  # 이전 좌표를 former에 저장
            A[x][y] = tmp  # A에 바꾼 좌표 저장
            tmp = former  # 바꾼 좌표를 이전 좌표에 저장

        for j in range(k + 1, M - k):  # 아래쪽 (X값 고정, Y값 증가)
            y = j
            former = A[x][y]
            A[x][y] = tmp
            tmp = former

        for j in range(k + 1, N - k):  # 오른쪽 (X값 감소, Y값 고정)
            x = N - j - 1
            former = A[x][y]
            A[x][y] = tmp
            tmp = former

        for j in range(k + 1, M - k):  # 위쪽 (X값 고정, Y값 감소)
            y = M - j - 1
            former = A[x][y]
            A[x][y] = tmp
            tmp = former

for _ in range(R):    # R번 회전 
    rotate()

for i in range(N):
    for j in range(M):
        print(A[i][j], end=' ')        #결과 원소 출력
    print()
