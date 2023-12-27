# import heapq
# import sys

# heap = []
# answer = []

# N = int(sys.stdin.readline())

# for i in range(N):
#   n = int(sys.stdin.readline())
#   if n == 0:
#     if len(heap) < 1:
#       print(0)
#       continue
#     print(-heapq.heappop(heap))
#   else:
#     heapq.heappush(heap,-n)


import heapq
import sys
heap = []
answer = []

N = int(sys.stdin.readline())

for i in range(N):
  n = int(sys.stdin.readline())
  if n == 0:
    if len(heap) < 1:
      answer.append(0)
      continue
    answer.append(-heapq.heappop(heap))
  else:
    heapq.heappush(heap,-n)

for i in answer:
  print(i)