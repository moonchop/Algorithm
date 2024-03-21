import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]
s = []
q = deque()
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs_temp(n):
    visited[n] = True
    s.append(n)
    
    while s:
        popped = s.pop()
        print(popped, end = ' ')
        for i in sorted(graph[popped],reverse=True):
            if not visited[i]:
                s.append(i)
                visited[i] = True

def dfs(n):
    visited[n] = True
    print(n,end=' ')
    for i in sorted(graph[n]):
        if not visited[i]:
            dfs(i)
    return
    
    

def bfs(n):
    visited[n] = False
    q.append(n)
    
    while q:
        popped = q.popleft()
        print(popped, end = ' ')
        for i in sorted(graph[popped]):
            if visited[i]:
                q.append(i)
                visited[i] = False


dfs(V)
print()
bfs(V)