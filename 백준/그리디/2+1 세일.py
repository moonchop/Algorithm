import sys

input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

answer = 0
for i,v in enumerate(arr,start=1):
    if i%3 != 0:
        answer+=v
        
print(answer)