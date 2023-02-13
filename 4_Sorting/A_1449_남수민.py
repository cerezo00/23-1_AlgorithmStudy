# 1449. 수리공 항승
# 36ms

num_hole, len_tape = map(int, input().split())
pos_hole = list(map(int, input().split()))
pos_hole.sort()

# 첫 번째 테이프의 시작지점과 끝지점 초기화
start = pos_hole[0]
end = pos_hole[0] + len_tape
count = 1

# 각 지점에 대해
# 1. 테이프의 범위에 속하면 continue
# 2. 테이프의 범위를 벗어나면 새로운 테이프 시작
for i in range(num_hole):
    if start <= pos_hole[i] < end:
        continue
    else:
        start = pos_hole[i]
        end = pos_hole[i] + len_tape
        count += 1

print(count)