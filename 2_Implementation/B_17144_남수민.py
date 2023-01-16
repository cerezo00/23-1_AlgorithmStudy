# 메모리 : 29964, 시간 : 1548

# 17144 : 미세먼지 안녕!

import sys

INPUT = sys.stdin.readline
VECTOR = [(0, 1), (-1, 0), (0, -1), (1, 0)]


# 문제 해결 함수
def solution():
    # 세로길이, 가로길이, 시간, 방구조 입력
    height, width, time = map(int, INPUT().split())
    room = [list(map(int, INPUT().split())) for _ in range(height)]

    # 입력받은 시간만큼 반복
    for t in range(time):
        spread_dust(room)    # 1. 먼지 확산
        circulate_air(room)  # 2. 공기 순환

    # 먼지의 양을 구하여 출력
    amount_dust = get_amount_dust(room)
    return amount_dust


# 먼지를 확산시키는 함수
def spread_dust(room):
    og_room = list(row[:] for row in room)  # og_room := 방 데이터 사본
    room_size = (len(room), len(room[0]))   # room_size := 방의 크기 (row, col)
    dust_pos = get_dust_pos(room)           # dust_pos := 먼지의 위치

    # 각 먼지에 대하여 확산 수행
    for y, x in dust_pos:
        one_fifth_amount = int(og_room[y][x] / 5)  # one_fifth_amount := 확산되는 먼지의 양

        # 네 방향에 대하여 수행
        for i in range(4):
            ny = y + VECTOR[i][0]
            nx = x + VECTOR[i][1]

            # 범위를 벗어나지 않고, 공기청정기가 없는 위치라면 먼지 전파
            if 0 <= ny < room_size[0] and 0 <= nx < room_size[1] and room[ny][nx] != -1:
                room[ny][nx] += one_fifth_amount  # 확산된 먼지만큼 확산위치 먼지 증가
                room[y][x] -= one_fifth_amount    # 확산된 먼지만큼 기존위치 먼지 감소


# 공기를 순환시키는 함수
def circulate_air(room):
    cleaner_ypos = get_cleaner_pos(room)

    # 공기 순환 (0:윗공기, 1:아랫공기)
    for up_down in range(2):
        dir = 0
        tmp_dust = 0
        y, x = cleaner_ypos[up_down], 1

        # 공기 청정기 위치로 돌아올 때까지 반복
        while not(y in cleaner_ypos and x == 0):
            # 공기 이동 예측 좌표
            ny = y + VECTOR[dir][0]
            nx = x + VECTOR[dir][1]

            # 공기 순환 방향 전환
            if 0 > ny or ny >= len(room) or 0 > nx or nx >= len(room[0]):
                if up_down == 0:
                    dir += 1
                else:
                    dir -= 1
                continue

            # 공기 순환
            room[y][x], tmp_dust = tmp_dust, room[y][x]
            y, x = ny, nx


# 공기 청정기의 위치를 반환하는 함수
def get_cleaner_pos(room):
    for y in range(len(room)):
        if room[y][0] == -1:
            return y, y + 1


# 먼지의 위치를 반환하는 함수
def get_dust_pos(room):
    dust_pos = list()

    for row in range(len(room)):
        for col in range(len(room[0])):
            if room[row][col] > 0:
                dust_pos.append((row, col))

    return dust_pos


# 방에 있는 먼지의 양을 구하여 반환하는 함수
def get_amount_dust(room):
    amount_dust = sum(sum(room[i]) for i in range(len(room))) + 2
    return amount_dust


result = solution()

print(result)
