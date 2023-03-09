import sys


n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
dp=[]
index=m
for i in range(n):
  dp.append(arr[i*m:index])
  index+=m

for j in range(1,m):
  for i in range(n):
    if i == 0:
      dp[i][j] += max(dp[i][j-1],dp[i+1][j-1])
    elif i == n-1:
      dp[i][j] += max(dp[i][j-1],dp[i-1][j-1])
    else:
      dp[i][j] += max(dp[i][j-1],dp[i-1][j-1],dp[i+1][j-1])
      

result=0
for i in range(n):
  result = max(result,dp[i][m-1])
print(result)