# 187320kb 5360ms
import sys
input = sys.stdin.readline

def binary_search(s,e,nums1,num):
    while s <= e:
        mid = (s+e) //2
        if nums1[mid] == num:
            return 1
        elif nums1[mid] < num:
            s = mid+1
        else :
            e = mid-1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    nums1.sort()
    m = int(input())
    note_2 = list(map(int, input().split()))
    for num in note_2:
        print(binary_search(0, n-1, nums1, num))