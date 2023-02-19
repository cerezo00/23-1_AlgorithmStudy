# 2417 정수 제곱근
# 메모리 31388 KB 시간 40 ms
# q^^2 >= n인 가장 작은 음이 아닌 정수 q 출

n = int(input())  # 정수 n
start, end = 0, n # 시작점 끝점

while start <= end:
    mid = (start + end) // 2  # 중간 지점을 구해
    if mid ** 2 >= n:         # 중간지점 제곱값이 n보다 크거나 같으면 중간지점의 왼쪽 부분이므로
        end = mid -1          # 끝점은 중간 지점 - 1
    else:
        start = mid + 1       # n보다 작으면 오른쪽 부분이므로 시작점은 중간 지점 + 1

print(start)  # 출력
