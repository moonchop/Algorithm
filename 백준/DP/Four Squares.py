import sys, math

input = sys.stdin.readline
N = int(input())

dp = [0,1]

for i in range(2, N+1):
    minValue = sys.maxsize
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j**2])
    dp.append(minValue + 1)

print(dp[N])