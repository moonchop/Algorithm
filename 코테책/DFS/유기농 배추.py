import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
result=[]
for i in range(n):
  row, col, k = map(int,sys.stdin.readline().split())
  graph = [[0] * row for _ in range(col)]
  for _ in range(k):
    b,a = map(int,sys.stdin.readline().split())
    graph[a][b] = 1

  count=0

  def dfs(x,y):
    global result
    if x >=col or y >= row or x < 0 or y < 0:
      return False
    
    if graph[x][y] == 1: 
      graph[x][y] = 0
      dfs(x+1,y)
      dfs(x-1,y)
      dfs(x,y+1)
      dfs(x,y-1)
      return True
    return False

  for i in range(col):
    for j in range(row):
      if dfs(i,j) == True:
        count+=1 
  result.append(count)    

for elem in result:
  print(elem)