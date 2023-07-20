import sys
from heapq import heappush,heappop

MAX = sys.maxsize
n,m = map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline())
distance = [MAX] * (n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))

def dijkstra(start):
  distance[start] = 0
  heap= []
  heappush(heap,(0,start))
  
  while heap:
    dist,now = heappop(heap)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1] 
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heappush(heap,(cost,i[0]))

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2