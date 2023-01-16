# 30616kb 44ms

# 14499 주사위 굴리기
# r: 북쪽으로부터 떨어진 칸의 개수 , c: 서쪽으로부터 떨어진 칸의 개수
# 처음 주사위에는 모든 면에 0이 적혀져있다.

# 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
# 주사위는 지도의 바깥으로 이동시킬 수 없다.
# 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성
n, m, x, y, k = map(int, input().split())

board = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]
# dice[0] : 윗면, dice[1] : 뒷면, dice[2] : 오른쪽면, dice[3] : 왼쪽면, dice[4] : 앞면, dice[5] : 밑면
def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in range(n):
    board.append(list(map(int, input().split())))
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
comm = list(map(int, input().split()))
# 주사위 값 초기화
nx, ny = x, y
for i in comm:
    nx += dx[i-1]
    ny += dy[i-1]
    # 범위 밖으로 넘어가면 그 값을 뺴준다.
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])

