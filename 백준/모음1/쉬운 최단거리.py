import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int,input().split())
visited = [[False] * M for _ in range(N)]
graph = []
q = []
x_2 = -1
y_2 = -1
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    arr = list(map(int,input().split()))
    arr = [-1 if x==1 else x for x in arr]
    if 2 in arr:
        x_2 = i
        y_2 = arr.index(2)
    graph.append(arr)

def bfs(x,y):
    visited[x][y] = True
    q = deque([(x,y,0)])
    graph[x][y] = 0
    while q:
        x, y, z = q.popleft()
        for coord in range(4):
            nx = x+dx[coord]
            ny = y+dy[coord]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == True:
                continue
            if graph[nx][ny] != -1:
                continue
            visited[nx][ny] = True
            q.append((nx,ny,z+1))
            graph[nx][ny] = z+1
bfs(x_2,y_2)

for i in graph:
    print(*i)
            