import sys

n = int(sys.stdin.readline())
v = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(v):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
dfs(1)

print(sum(visited)-1)