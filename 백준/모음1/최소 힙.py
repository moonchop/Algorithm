import sys, heapq

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
  n = int(input())
  if n == 0:
    print(0) if len(arr) == 0 else print(heapq.heappop(arr))
  else:
    heapq.heappush(arr,n)
  
  
