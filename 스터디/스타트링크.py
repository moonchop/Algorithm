import sys

input = sys.stdin.readline

total,current,to,up,down = map(int,input().split())
visited = [False] * (total+1)
count = [0] * (total+1)

def bfs(v):
    q=[v]
    visited[v] = True
    while q:
        v = q.pop(0)
        if v == to:
            return count[to]
        for i in (v-down,v+up):
            if  0 < i <= total and not visited[i]:
                visited[i] = True
                count[i] = count[v] + 1
                q.append(i)
    return "use the stairs"

print(bfs(current))
