#메모리 30616KB, 시간 36ms

N= int(input()) # N : 사람들의 수
times = list(map(int,input().split())) #인출하는데에 걸리는 시간을 입력받아 times 배열에 저장
 
times.sort() #입력받은 시간들을 오름나춘으로 저장

total_time = 0 # total_time : 현재 순서 사람이 걸리는 시간 
result = 0 # result : 마지막 사람까지 인출을 완료할 때까지 걸리는 시간
            #이 변수의 최종값이 이 문제에서 구하고자 하는 최종 답이 된다.

for i in times: #정렬된 시간들을 하나씩 반복문을 통해 가져온다.
    total_time = total_time + i # 현재 순서의 사람이 걸리는 시간 = (앞 순서의 사람들이 걸린 총 시간) + (자신이 인출하는데 걸리는 시간)
                                # 이 값은 그대로 뒷 순서의 사람들이 걸린 총 시간이 된다.

    result += total_time #그리고 이 total_time 값을 result 변수에 더해나간다.

print(result)
