# 12761 돌다리
# 메모리 42212 KB, 시간 200ms

from collections import deque

A, B, N, M = map(int, input().split())
# A, B : 스카이 콩콩 힘
# N, M : 동규, 주미 현재 위치

cnt = dict()  # 각 돌의 최소 이동 횟수
cnt[N] = 0    # 동규 위치에서 이동 횟수 0으로 시작
queue = deque([N])  # N에서 시작

def bfs():    # bfs
    while queue:
        now = queue.popleft()
        for i in {1, -1, A, -A, B, -B}:    # +- 1, +- A, +- B 이동 시
            tmp = now + i                  # 현재 위치에서 현재 인덱스만큼 이동한 값 저장
            if 0 <= tmp <= 100000 and tmp not in cnt:  # 범위에서 벗어나지 않고 아직 방문하지 않은 위치라면
                cnt[tmp] = cnt[now] + 1    # 이동 횟수에 추가
                queue.append(tmp)

        for i in {A, B}:  # A배나 B배의 위치로 이동
            tmp = now * i    # 배로 이동하므로 현재 위치에 현재 인덱스만큼 곱함
            if 0 <= tmp <= 100000 and tmp not in cnt:  # 범위에서 벗어나지 않고 아직 방문하지 않은 위치라면
                cnt[tmp] = cnt[now] + 1    # 이동 횟수에 추가
                queue.append(tmp)

        if M in cnt:  # M에 도착하면
            print(cnt[M])  # M으로 가는 최소 이동 횟수 출력
            break  # 종료

bfs()   # 함수 호출
