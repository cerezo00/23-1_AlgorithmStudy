#메모리 30840KB, 시간 72ms

N = int(input()) # N : 사람들의 수

times = list(map(int, input().split())) #인출하는데에 걸리는 시간을 입력받아 times 배열에 저장
times.sort() #입력받은 시간들을 오름나춘으로 저장

result = 0 #마지막 사람까지 인출을 완료할 때까지 걸리는 시간을 저장할 변수 result를 선언 후 0으로 초기화 
            #이 변수의 최종값이 이 문제에서 구하고자 하는 최종 답이 된다.

for i in range(N): #사람들의 수 만큼 반복문을 돌며
    result += sum(times[:i+1]) #처음 사람부터 현재 사람까지 걸리는 시간의 합을 result 변수에 슬라이싱을 사용하여 더해감
    
print(result)