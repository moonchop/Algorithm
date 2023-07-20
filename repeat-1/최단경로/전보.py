from heapq import heappush, heappop
import sys

MAX = int(1e9)

N,M,C = map(int,sys.stdin.readline().split())
graph = [[] * (N+1) for _ in range(N+1)]
distance = [MAX] * (N+1)
total_city=0
total_time=0

for _ in range(M):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  heappush(q,(0,start))
  distance[start]=0
  
  while(q):
    dist, now = heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if distance[i[0]] > cost:
        distance[i[0]] = cost
        heappush(q,(cost,i[0]))
        
dijkstra(C)

for i in range(2,N+1):
  if distance[i] != MAX:
    total_city+=1
    if total_time < distance[i]:
      total_time = distance[i]
      
print(total_city, total_time)