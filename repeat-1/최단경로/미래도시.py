import sys
from heapq import heappush, heappushpop

n, m = map(int,sys.stdin.readline().split())
MAX = int(1e9)

graph = [[MAX] * (n+1) for _ in range(n+1) ]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0
      
for _ in range(m):
  a, b = map(int,sys.stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1
  
X, K = map(int,sys.stdin.readline().split())

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
      
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if graph[i][j] == MAX:
#       print(-1)
#     else:
#       print(graph[i][j],end=' ')
#   print()
  
  
result = graph[1][K]+graph[K][X]
if result == MAX:
  print(-1)
else:
  print(result)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5