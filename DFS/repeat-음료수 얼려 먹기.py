# -*- coding: utf-8 -*- 
import sys
n,m = map(int,sys.stdin.readline().split())

graph=[[int(i) for i in sys.stdin.readline().strip()] for _ in range(n)]
    
def dfs(x,y):
    if x >= n or y >= m or x < 0 or y < 0:
        return False
    
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return False    

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1
            
print(result)