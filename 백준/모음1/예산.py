import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
M = int(input())

arr.sort()
total = sum(arr)

if total <= M:
    print(arr[-1])
else:
    for i,v in enumerate(arr):
        M -= v
        if M <= (N-(i+1))*v:
            print((M+v)//(N-i))
            break