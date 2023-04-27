import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().rstrip())))

def dfs(x,y):
  if x < 0 or y < 0 or x >=n or y>=m:
    return False
  if graph[x][y]==0:
    graph[x][y]=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

  check=False
  stack=deque()
  stack.append((x,y))
  while stack:
    x,y = stack.pop()
    for i in range(4):
      nx = x +dx[i]
      ny = y +dy[i]
      if nx < 0 or ny < 0 or nx >=n or ny>=m:
        continue
      if graph[nx][ny]==0:
        print(graph,stack)
        check=True
        # graph[x][y] = 1
        stack.append((x,y))
  return check
result=0
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      isIce = dfs(i,j)
      if isIce == True:
        result+=1
print(result)
