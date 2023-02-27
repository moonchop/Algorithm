import sys
from collections import deque

n = int(sys.stdin.readline())

graph =[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,1,-1]
results=[]


def bfs(xPos,yPos):
    count = 1
    q = deque()
    q.append((xPos,yPos))
    graph[xPos][yPos]=0
    while q:

        x,y=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny]=0
                    q.append((nx,ny))
                    count+=1
    results.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
results.sort()
print(len(results))
for i in results:
    print(i)