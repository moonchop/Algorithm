import sys,heapq
from collections import defaultdict




min_heap = []
max_heap = []
solved = defaultdict(bool)
answer = []

N = int(sys.stdin.readline())
for _ in range(N):
  a,b = map(int,sys.stdin.readline().split())
  heapq.heappush(min_heap,(b,a))
  heapq.heappush(max_heap,(-b,-a))
  solved[a] = True
  
M = int(sys.stdin.readline())
for _ in range(M):
  m = sys.stdin.readline().split()
  if m[0] == 'add':
    while not solved[-max_heap[0][1]]:
        heapq.heappop(max_heap)
    while not solved[min_heap[0][1]]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap,(int(m[2]),int(m[1])))
    heapq.heappush(max_heap,(-int(m[2]),-int(m[1])))
    solved[int(m[1])] = True
  elif m[0] == 'solved':
    solved[int(m[1])] = False    
  elif m[0] == 'recommend':
    if m[1] == '1':
      while max_heap and not solved[-max_heap[0][1]]:
        heapq.heappop(max_heap)
      print(-max_heap[0][1])
      answer.append(-max_heap[0][1])
    elif m[1] == '-1':
      while min_heap and not solved[min_heap[0][1]]:
        heapq.heappop(min_heap)
      print(min_heap[0][1])
      answer.append(min_heap[0][1])
      
      

    