import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse=True)

answer = arr[0]

for i in range(1,N):
    answer+=arr[i]/2


if int(answer)-answer !=0:
    print(float(answer))
else:
    print(int(answer))
    
print("%g"%answer)