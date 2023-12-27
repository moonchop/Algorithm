import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

dp = [0] *(n)
dp[0]=1
for i in range(1,n):
  if arr[i] <= arr[i-1]:
    dp[i]=dp[i-1]+1
  else:
    dp[i]=dp[i-1]
print(n-dp[n-1])