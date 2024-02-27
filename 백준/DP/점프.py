import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
answer =0 

# def dfs(x,y):
#     global answer
#     if x >= N or y >= N:
#         return
#     if graph[x][y] == 0:
#         answer +=1
#         return
    
#     dfs(x,y+graph[x][y]) 
#     dfs(x+graph[x][y],y)

# dfs(0,0)
# print(answer)

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            break
        if graph[i][j]+i < N:
            dp[i+graph[i][j]][j] += dp[i][j]
        if graph[i][j]+j < N:
            dp[i][j+graph[i][j]] += dp[i][j]
        
        
        
print(dp[-1][-1])
        