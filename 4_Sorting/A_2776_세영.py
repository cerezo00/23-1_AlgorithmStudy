
import sys
input = sys.stdin.readline

T = int(input().strip())

def BS(arr, length, target):

    left = 0 
    right = length-1

    while left<=right:
        mid = (left+right)//2
 
        if arr[mid] == target:
            return True
        elif arr[mid]>target:
            right = mid-1

        else :
            left = mid+1

    return False

for i in range(T):
    N = int(input().strip())
    note1 = set(list(map(int,input().split())))
    M = int(input().strip())
    note2 = list(map(int,input().split()))
    note1.sort()
    
    for j in note2:
        if BS(note1,N,j):
            print(1)
        else:
            print(0)

