import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

arr.sort()

answer = 0

# if N % 2 == 0:
#   for i in range(N//2):
#     answer = max(answer,arr[i]+arr[N-i-1])
    
# else:
#   answer = arr[-1]
#   for i in range(N//2):
#     answer = max(answer,arr[i]+arr[N-i-2])
    

# print(answer)



if N%2 != 0:
  answer = arr.pop()
  N-=1
for i in range(N//2):
    answer = max(answer,arr[i]+arr[N-i-1])
    
print(answer)