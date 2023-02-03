#30616	40

from itertools import combinations

#combinations 함수를 활용하여 6개의 정수를 뽑아 뽑은 조합들을 모두 출력
while True:
    arr = list(map(int,input().split()))
    k = arr [0]
    numbers = arr[1:]
    if (k == 0):
        break

    tmps = list(combinations(numbers,6))
    
    for i in tmps:
        for j in i:
            print(j, end=" ")
        print()

    print()
