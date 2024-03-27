import sys
from heapq import heappush,heappop

input = sys.stdin.readline

MAX = sys.maxsize
n,m = map(int,input().split())
distance = [MAX] * (m+1)
graph=[[] for _ in range(m+1)]

for i in range(m):
    graph[i].append((i+1, 1))
    
for _ in range(n):
  a,b,c = map(int,input().split())
  if b > m:
    continue
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
        
dijkstra(0)

print(distance[m])