# 16926 배열 돌리기
# 배열을 반시계방향으로 r번 회전 시키기

n, m, r = map(int, input().split())
arr = [] # 배열 받을 리스트
for _ in range(m): # 이차원 배열로 받기
    arr.append(list(map(int, input().split())))

# 바꿀 좌표를 계산하고 그 좌표의 값을 저장해놓고 이전 좌표의 값을 계산된 좌표의 값에 넣는 식으로 계산하였다.
# 하나의 사각형을 다 돌렸으면 안쪽 사각형으로 들어간다.
for _ in range(r): # 반복문을 r번 돌리면서
    for i in range(min(n,m)//2): # 사각형의 개수만큼 반복문을 돈다.
        s_x, s_y = i, i # x, y 는 돌려지는 배열중 가장 첫번째 배열 인덱스
        s_value = arr[s_x][s_y] # 초기값 설정

        for j in range(i + 1, n - i):  # 좌 : x값이 증가하고 y는 그대로
            s_x = j
            prev_value = arr[s_x][s_y]
            arr[s_x][s_y] = s_value
            s_value = prev_value

        for j in range(i + 1, m - i):  # 하 : x 값은 그대로, y값만 증가한다.
            s_y = j
            prev_value = arr[s_x][s_y]
            arr[s_x][s_y] = s_value
            s_value = prev_value

        for j in range(i + 1, n - i):  # 우 : x값이 감소하고, y 값은 그대로
            s_x = n - j - 1
            prev_value = arr[s_x][s_y]
            arr[s_x][s_y] = s_value
            s_value = prev_value

        for j in range(i + 1, m - i):  # 상 : x값은 그대로, y값이 감소한다.
            s_y = m - j - 1
            prev_value = arr[s_x][s_y]
            arr[s_x][s_y] = s_value
            s_value = prev_value

## 최종값 출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()