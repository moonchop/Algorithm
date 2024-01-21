import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

def dfs(n,target,distance,visited):
    visited[n] = True
    if n == target:
        print(distance)
        return
    
    for i in graph[n]:
        if visited[i[0]] == False:
            dfs(i[0],target,distance+i[1],visited)
            visited[i[0]] = False

def stack(n,target,distance,visited):
    visited[n] = True
    stk = [(n,0)]
    while stk:
        
        popped = stk.pop()
        if popped[0] == target:
            return popped[1]
        
        for i in graph[popped[0]]:
            if not visited[i[0]]:
                stk.append((i[0],i[1]+popped[1]))
                visited[i[0]] = True
                # distance+=i[1]
    


for _ in range(N-1):
    a, b, distance = map(int,input().split())
    graph[a].append((b,distance))
    graph[b].append((a,distance))


for _ in range(M):
    distance = 0
    visited = [False]*(N+1)
    n, target = map(int,input().split())
    # (dfs(n,target,distance,visited))
    print(stack(n,target,distance,visited))
    
    
