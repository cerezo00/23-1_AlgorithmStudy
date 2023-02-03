# 10451 순열 사이클
# 사이클이 존재할 때, 해당 사이클의 크기를 구하는 문제
# 31348kb 588ms
import sys
sys.setrecursionlimit(10**7)

def dfs(x):
    visited[x] = True # 방문 체크
    number = numbers[x] # 다음 방문 장소
    if not visited[number] : # 다음 방문 장소를 방문하지 않았으면
        dfs(number)

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [0] + list(map(int, input().split())) # 여기서 0을 하나 더 왜만들지?
    visited = [True] + [False] * n
    result = 0

    for i in range(1,n+1):
        if not visited[i] : # 방문하지 않았다면
            dfs(i)
            result += 1
    print(result)
