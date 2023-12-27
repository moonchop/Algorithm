import sys

MAX = sys.maxsize
n, m = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph=[[] for i in range(n+1)]
distance = [MAX] * (n+1)
visited = [False] * (n+1)


for _ in range(m):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
  

def shortest():
  index = 0 
  min_value = MAX
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  visited[start] = True
  distance[start] = 0
  for i in graph[start]:
    distance[i[0]] = i[1]
  
  for i in range(n-1):
    now = shortest()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if distance[j[0]] > cost:
        distance[j[0]] = cost
        # distance[now] = distance[j[0]]

dijkstra(start)


for i in range(1,n+1):
  if distance[i] == MAX:
    print("MAX")
  else:
    print(distance[i])



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