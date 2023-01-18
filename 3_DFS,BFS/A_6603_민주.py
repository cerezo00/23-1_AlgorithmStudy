# 6603 로또
# 메모리 30616KB, 시간 44ms
# 49개의 수 중 6개 선택
# 49가지 수 중 K개(K>6)를 골라 집합 S 생성 -> 그 수 중에서 번호 선택
# S, K -> 수 고르는 모든 방법을 구하기

def dfs(i, depth):    # dfs 함수
    if depth == 6:    # depth가 6이면 더 이상 원소 추가를 하지 않으므로
        print(*arr)   # arr 출력
        return

    for i in range(i, k):  # i-k 범위에서
        arr.append(S[i])   # arr에 원소 추가
        dfs(i+1, depth+1)  # 현재 인덱스와 depth +1씩 증가
        arr.pop()

while True:
    S = list(map(int, input().split()))   # 집합 S
    k = S.pop(0)    # 첫 번째 수는 k
    arr = []    # 집합 S에서 수를 고르는 방법
    if k == 0:  # 0이 입력되면 종료
        break

    dfs(0, 0)   # dfs 호출
    print()     # 테스트케이스 사이 한 줄 공백
