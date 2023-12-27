import sys
import heapq

N = int(sys.stdin.readline())

arr=[]

for _ in range(N):
  num_case = (int(sys.stdin.readline()))
  
  if num_case == 0:
    if arr:
      print(arr)
      abs_num, num = heapq.heappop(arr)
      # print(num)
    else:
      print(0)
  else:
    heapq.heappush(arr,(abs(num_case),num_case))

