import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+2)

# def fibo(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
    
#     return fibo(n-1) + fibo(n-2)

# print(fibo(N))

dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[-2])