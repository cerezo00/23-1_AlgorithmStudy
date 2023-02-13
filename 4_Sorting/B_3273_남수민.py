# 3273. 두 수의 합
# 72ms

def sol():
    size = int(input())  # 1 <= n <= 10^6
    array = sorted(list(map(int, input().split())))  # 1 <= a <= 10^6
    X = int(input())  # 1 <= X <= 2 * 10^6

    i = 0         # a(i) 탐색 index
    j = size - 1  # a(j) 탐색 index
    count = 0     # 조건을 만족하는 쌍 (정답)

    while i < j:
        sum_ij = array[i] + array[j]

        if sum_ij < X:
            i += 1

        elif sum_ij > X:
            j -= 1

        else:
            count += 1
            i += 1
            j -= 1

    print(count)


sol()