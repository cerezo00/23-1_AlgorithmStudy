# 13164 행복유치원
# N명 중 K개의 조 -> N-K개 만큼 키 차이 값 계산
N, K = map(int, input().split())   # N : 원생 수, K : 조의 수
height = list(map(int, input().split()))  # height : 원생들의 키를 입력받아 저장할 배열 (오름차순)4
diff = []  # 키 차이 저장할 배열

for i in range(N-1): # 다음 원생과의 키 차이를 diff 배열에 저장
    diff.append(height[i + 1] - height[i]) # 현재 원생의 키와 그 옆 원생의 키의 차이를 원소로 추가
diff.sort()  # 오름차순 정렬

print(sum(diff[:N-K]))  #최소 비용 계산
