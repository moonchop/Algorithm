import sys

n,m = map(int,input().split())

graph=[]

for _ in range(n):
  graph.append(list(map(int,input())))


dx=[-1,1,0,0]
dy=[0,0,1,-1]

result=0

def dfs(x,y):
  global result
  
  if graph[x][y]==0:
    graph[x][y]=1
  
  if x < 0 or y < 0 or x >= n or y >= m:
    return
  for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx < 0 or ny < 0 or nx >=n or ny>=m:
        continue
      if graph[nx][ny] == 1:
        continue
      graph[nx][ny]=1
      dfs(nx,ny)
  result+=1
  print(graph,result)

dfs(0,0)
print(result)