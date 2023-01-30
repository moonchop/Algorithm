import sys

import heapq

heap=[]
result=[]
heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)
heapq.heappush(heap,3)

for i in range(len(heap)):
  result.append(heapq.heappop(heap))

print(result)