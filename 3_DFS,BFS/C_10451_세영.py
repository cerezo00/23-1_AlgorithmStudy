#31364	600

from sys import stdin

# T : 테스트 케이스 개수
T = int(stdin.readline())

# dfs 방식으로 현재 노드의 번호와 시작 노드 번호가 같은지 탐색
# 만약 현재 노드를 방문한 적이 있으면 continue,
# 없다면 방문 처리 후 현재 노드의 값이 시작 노드 번호가 같으면 순열 사이클 개수를 저장하는 result 값을 1 증가시키고,
# 다르다면 현재 노드와 시작 노드에 대해 dfs를 재귀적으로 호출하여 탐색을 계속한다.
def dfs(cur, start):
    global result
    if visited[cur]:
        return 
    visited[cur] = True

    if(permutation[cur]==start):
        result += 1
        return
    
    dfs(permutation[cur],start)


# N : 순열의 개수
# permutation : 순열을 배열로 저장
# visited : 방문 체크 함수
# 노드의 시작 번호를 1로 맞추기 위하여 1부터 N+1 까지 dfs를 수행
for i in range(T):
    result = 0
    N = int(input())
    permutation = [0]+list(map(int,stdin.readline().split()))
   
    visited = [False] * (N+1)

    for j in range(1,N+1):
        dfs(j,j)

    print(result)