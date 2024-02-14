import sys

input = sys.stdin.readline

N = int(input())

# def dfs(n,count):
#     global answer
#     if n > N:
#         return 0
#     if n == N:
#         answer = min(answer,count)
#         return 0
    
#     dfs(n*3,count+1)
#     dfs(n*2,count+1)
#     dfs(n+1,count+1)

d = [0] * (N+1)
for i in range(2,N+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
print(d[N])