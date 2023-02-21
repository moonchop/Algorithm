import sys

n,m = map(int, sys.stdin.readline().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
    

def dfs(x,y):
    if x < 0 or x >=n or y < 0 or y >= m:
        return False
    if graph[x][y]==1:
        return False
    
    graph[x][y]=1
    # if x-1 >= 0 or y-1 >=0 or x+1 < n or y+1 < m:
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True


result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)