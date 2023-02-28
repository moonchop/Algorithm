import sys
from collections import deque 


n,m = map(int,sys.stdin.readline().split())
graph = []
ans=0
dx = [-1,1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
    
def bfs(xPos,yPos):
    global ans
    q = deque()
    q.append((xPos,yPos))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<= nx < n and 0<= ny < m:
                if graph[nx][ny]=="L" and visited[nx][ny]==-1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y]+1
                    ans = max(visited[nx][ny],ans)
    return ans


for i in range(n):
    for j in range(m) : 
        if graph[i][j]=="L":
            visited = [[-1]*m for _ in range(n)]
            visited[i][j]=0
            bfs(i,j)
            
print(ans)