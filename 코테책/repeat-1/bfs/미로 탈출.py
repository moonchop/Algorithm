import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().rstrip())))
  
visited = [[False]* m for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  visited[x][y] = 1
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] ==1 and not visited[nx][ny]:
        visited[nx][ny]=1
        graph[nx][ny]+=graph[x][y]
        queue.append((nx,ny))
  return graph[n-1][m-1]

print(bfs(0,0))

