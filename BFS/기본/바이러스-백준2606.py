from collections import deque
import sys

n = int(sys.stdin.readline())
v = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(v):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited[1]=1

Q=deque([1])

while Q:
    c=Q.popleft()
    print(c)
    for i in graph[c]:
        if visited[i]==0:
            Q.append(i)
            visited[i]=1
print(sum(visited)-1)
