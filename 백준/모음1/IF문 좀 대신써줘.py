import sys

input = sys.stdin.readline

N, M = map(int, input().split())
name_arr = []
num_arr = []
# candi_arr = []

def binary_search(target):
    start = 0
    end = N-1
    
    while start <= end:
        mid = (start+end)//2
        if target <= num_arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return end+1
            

for _ in range(N):
    a, b = input().split()
    name_arr.append(a)
    num_arr.append(int(b))
    
for _ in range(M):
    n = int(input())
    print(name_arr[binary_search(n)])