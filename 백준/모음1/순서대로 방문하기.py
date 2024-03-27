import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []
points = []
count=0

def dfs(now, pointIdx):
  global count
  if now == points[pointIdx]:
    if pointIdx == m-1:
      count += 1
      return
    else:
      pointIdx+=1
  
  x, y = now
  visited[x][y] = True
  
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    
    if 0<= nx < n and 0<= ny < n and visited[nx][ny] == False and graph[nx][ny] == 0:
      dfs((nx,ny),pointIdx)
  visited[x][y]=False
  return

for _ in range(n):
  graph.append(list(map(int,input().split())))

for _ in range(m):
  x, y = map(int,input().split())
  points.append((x-1,y-1))

visited = [[False]*n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dfs(points[0],0)

print(count)