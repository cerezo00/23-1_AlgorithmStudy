# 6987 웓드컵
# 메모리 30616KB, 시간 36 ms
# 6개국 조별리그 : 총 15경기
# -1 씩 dfs, 15번 모두 돌린 후 전체 승무패 합 0 되는지 확인
# 결과 각 나라별로 쪼개서 담기(3) -> 경기 가능한 조합 생성 -> 라운드 돌 면서 값 빼줌

import sys
input = sys.stdin.readline
from itertools import combinations

def dfs(depth):
    global result
    if depth == 15:  # 15경기까지 도달하면
        result = 1   # 결과 1 저장
        for i in country_arr:
            if i.count(0) != 3:  # 승무패 값이 남아있다면 (contry_arr의 0 값이 3개가 아니면)
                result = 0       # 결과 0 저장
                break
        return

    t1, t2 = match[depth] # 경기 조합 (15경기)
    for x, y in ((0, 2), (1, 1), (2, 0)):  # 각 경기의 승무패
        # 승 -1 -> 패 -1
        # 무 -1 -> 무 -1
        if country_arr[t1][x] > 0 and country_arr[t2][y] > 0: # 값이 남아있다면
            country_arr[t1][x] -= 1
            country_arr[t2][y] -= 1
            dfs(depth + 1)
            country_arr[t1][x] += 1
            country_arr[t2][y] += 1

for _ in range(4):
    arr = list(map(int, input().split()))   # 각 나라의 결과 입력
    country_arr = [arr[i:i + 3] for i in range(0, 16, 3)] # 나라별로 쪼개서 저장
    match = list(combinations(range(6), 2)) #  가능한 경기 조합 모두 생성
    result = 0  # 각 결과가 가능한지 여부 저장 (0 또는 1)
    dfs(0)    # dfs 호출
    print(result, end=" ") # 결과 출력
print()
