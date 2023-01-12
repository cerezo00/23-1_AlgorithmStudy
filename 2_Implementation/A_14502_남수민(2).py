from itertools import combinations

# 상수선언
EMPTY = 0  # object code
WALL = 1   # object code
VIRUS = 2  # object code
VECTOR = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 변위


# object의 좌표를 리스트로 반환
def get_object_pos(map, object):
    object_pos = []

    # 맵의 모든 칸에 대하여 object의 좌표 획득
    for y in range(height):
        for x in range(width):
            if map[y][x] == object:
                object_pos.append((y, x))

    return object_pos


def solution(height, width, map):
    empty_pos = get_object_pos(map, EMPTY)  # empty_pos := 빈 칸의 좌표 리스트
    virus_pos = get_object_pos(map, VIRUS)  # virus_pos := 바이러스의 좌표 리스트
    min_virus_zone = height * width         # max_safezone := 바이러스영역의 최솟값

    # pair := 벽을 세울 빈 칸의 좌표 3개를 선택하는 모든 조합
    for pair in combinations(range(num_empty_pos), 3):
        
        map_copy = [row[:] for row in map]  # map_copy := 시뮬레이션을 진행할 맵의 복사본
        
        # 선택된 좌표 3곳에 벽을 세움
        for pos in pair:
            y, x = empty_pos[pos]
            map_copy[y][x] = 1
        
        virus_zone = 0                                    # virus_zone := 바이러스영역 넓이
        virus_pos_queue = [(n, m) for n, m in virus_pos]  # virus_pos_queue := 전파할 바이러스의 좌표
        
        # 바이러스 전파 알고리즘
        while virus_pos_queue:
            # 전파할 바이러스의 좌표 하나 선택
            y, x = virus_pos_queue.pop()
            
            # (가지치기) 현재 시도에서 바이러스영역의 넓이가 최소넓이를 초과한다면 종료
            if virus_zone > min_virus_zone:
                break
            
            # 상하좌우에 대하여 다음 조건에 충족한다면 전파
            # 조건 1. 맵의 범위를 벗어나지 않는다.
            # 조건 2. 해당 위치가 비어있다.
            for dy, dx in VECTOR:
                nx = x + dx
                ny = y + dy
                if 0 <= ny < height and 0 <= nx < width and map_copy[ny][nx] == EMPTY:
                    virus_zone += 1                   # 바이러스영역 넓이 증가
                    map_copy[ny][nx] = 2              # 맵(사본)의 현재 위치에 바이러스 입력
                    virus_pos_queue.append((ny, nx))  # 전파할 바이러스 목록(큐)에 추가

        # 바이러스영역의 최솟값 업데이트
        min_virus_zone = min(min_virus_zone, virus_zone)

    return min_virus_zone


# height, width := 연구실의 세로, 가로 길이
# map_original := 연구실의 원본 지도
height, width = map(int, input().split())
map_original = [list(map(int, input().split())) for _ in range(height)]

# num_empty_pos := 빈 공간의 수
num_empty_pos = sum([map_original[row].count(EMPTY) for row in range(height)])

# min_virus_zone = 바이러스영역의 최솟값
min_virus_zone = solution(height, width, map_original)

# safe_zone := 안전영역의 넓이 = 최초 빈 칸의 넓이 - 바이러스영역 넓이 - 새롭게 세운 벽의 수
safe_zone = num_empty_pos - min_virus_zone - 3

print(safe_zone)
