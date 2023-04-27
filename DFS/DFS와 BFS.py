import sys

n,m,v = map(int,sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)] 

result=[]
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = graph[b][a] = 1
visited = [False] * (n+1)
def dfs(v):
  visited[v] = 1
  print(v, end=' ')
  for i in range(1,n+1):
    if visited[i]==0 and graph[v][i]:
      dfs(i)

def bfs(v):
  visited[v] = 0
  queue = [v]
  while queue:
    v = queue.pop(0)
    print(v,end=' ')
    for i in range(1,n+1):
      if visited[i]==1 and graph[v][i]:
        queue.append(i)
        visited[i]=0
  
dfs(v)   
print()
bfs(v)