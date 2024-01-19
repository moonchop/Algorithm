import sys,heapq

input =  sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
count = 1

def dijkstra(graph,cost,N):
    q = []
    heapq.heappush(q,(graph[0][0],0,0))

    while q:
        now_cost,x,y = heapq.heappop(q)
        if cost[x][y] < now_cost:
            continue
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                cost_sum = now_cost + graph[nx][ny]
                if cost_sum < cost[nx][ny]:
                    cost[nx][ny] = cost_sum
                    heapq.heappush(q,(cost_sum,nx,ny))
    return cost[N-1][N-1]

while True:
    N = int(input())
    if N == 0:
        break
    
    graph = []
    cost = [[sys.maxsize] * N for _ in range(N)]

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    print(f"Problem {count}: {dijkstra(graph,cost,N)}")
    count+=1
