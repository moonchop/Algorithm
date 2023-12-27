import heapq

N = int(input())

arr=[]

for _ in range(N):
  for i in list(map(int,input().split())):
    if len(arr) >= N:
      heapq.heappush(arr,i)
      heapq.heappop(arr)
    elif len(arr) < N:
      heapq.heappush(arr,i)

print(heapq.heappop(arr))