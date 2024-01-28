import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
answer = []
for _ in range(N):
  M,N,K = map(int,input().split())

  graph = [[0] * M for _ in range(N)]
  visited = [[False] * M for _ in range(N)]


  for _ in range(K):
    x,y = map(int,input().split())
    graph[y][x]=1

  def dfs(y,x):
    if x >= M or x < 0 or y >= N or y <0:
      return False
    if graph[y][x] == 1 and not visited[y][x]:
      visited[y][x] = True
      graph[y][x]=0
      dfs(y,x+1)
      dfs(y,x-1)
      dfs(y-1,x)
      dfs(y+1,x)
      return True
    return False
    
  result = 0 
  for i in range(N):
    for j in range(M):
      if not visited[i][j]:
        if(dfs(i,j)):
          result +=1
          
  answer.append(result)
  
for answer in answer:
  print(answer)
        
  