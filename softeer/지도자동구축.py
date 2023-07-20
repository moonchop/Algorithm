import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    dp[i] = (dp[i-1] * 2)
print((dp[-1]+1)*(dp[-1]+1))
