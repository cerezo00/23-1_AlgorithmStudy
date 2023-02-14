#31256	44

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = []
result = 0
for i in range(N):
    nums.append(int(input()))




if 0 in nums:
    nums.sort()
    zIndex = nums.index(0)
    negatives = nums[:zIndex]
    positives = nums[zIndex+1:]
    negaLen = len(negatives)
    posiLen = len(positives)
    i = 0

    #0이 있고, 음수 개수가 짝수
    if negaLen % 2 == 0:
        while len(negatives) > 1:
            result += negatives[0] * negatives[1]
            negatives = negatives[2:]

        if len(negatives) == 1:
            result += negatives[0]
        while len(positives) > 1:
            positives.sort(reverse=True)
            
            mulVal = positives[0] * positives[1]
            addVal = positives[0] + positives[1]
            if mulVal > addVal:
                result += mulVal
                positives = positives[2:]
            else:
                result += addVal
                positives = positives[2:]

        if len(positives) == 1:
            
            result += positives[0]

    #0이 있고, 음수 개수가 홀수
    else:

        while len(negatives) > 1:
            result += negatives[0] * negatives[1]
            negatives = negatives[2:]

        while len(positives) > 1:
            positives.sort(reverse=True)
            mulVal = positives[0] * positives[1]
            addVal = positives[0] + positives[1]
            
            if mulVal > addVal:
                result += mulVal
                positives = positives[2:]
            else:
                result += addVal
                positives = positives[2:]

        if len(positives) == 1:
            
            result += positives[0]

else:
    nums.append(0)
    nums.sort()
    zIndex = nums.index(0)
    negatives = nums[:zIndex]
    positives = nums[zIndex+1:]
    negaLen = len(negatives)
    posiLen = len(positives)
    i = 0
    #0이 없고, 음수 개수가 짝수
    if negaLen % 2 == 0:
        while len(negatives) > 1:
            result += negatives[0] * negatives[1]
            negatives = negatives[2:]
    
        if len(negatives) == 1:
            result += negatives[0]
        while len(positives) > 1:
            positives.sort(reverse=True)
            
            mulVal = positives[0] * positives[1]
            addVal = positives[0] + positives[1]
            if mulVal > addVal:
                result += mulVal
                positives = positives[2:]
            else:
                result += addVal
                positives = positives[2:]

        if len(positives) == 1:
            
            result += positives[0]
    #0이 없고, 음수 개수가 홀수
    else:

        while len(negatives) > 1:
            result += negatives[0] * negatives[1]
            negatives = negatives[2:]

        if len(negatives) == 1:
            result += negatives[0]

        while len(positives) > 1:
            positives.sort(reverse=True)
            mulVal = positives[0] * positives[1]
            addVal = positives[0] + positives[1]
            
            if mulVal > addVal:
                result += mulVal
                positives = positives[2:]
            else:
                result += addVal
                positives = positives[2:]

        if len(positives) == 1:
            
            result += positives[0]

print(result)

