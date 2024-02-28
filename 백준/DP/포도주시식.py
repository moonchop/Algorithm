import sys

input = sys.stdin.readline

N = int(input())

graph = [int(input()) for _ in range(N)]
graph.insert(0,0)
dp = [0] * (N+1)

dp[1]=graph[1]
if N > 1:
    dp[2]=graph[1]+graph[2]

for i in range(3,N+1):
    dp[i] = max(dp[i-1],dp[i-2]+graph[i], graph[i]+graph[i-1]+dp[i-3])

print(dp[-1])