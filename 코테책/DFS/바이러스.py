import sys

n= int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False]*(n+1)
count=0
for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[a][b] = graph[b][a] = 1

def dfs(v):
  global count
  visited[v]=True
  count+=1
  for i in range(1,n+1):
    if visited[i]==False and graph[v][i]:
      dfs(i)
      
dfs(1)
print(count-1)
  
  