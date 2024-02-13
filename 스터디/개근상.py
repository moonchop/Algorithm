import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N)]


def dfs(day,late,abs):
    if late >= 2 or abs >= 3:
        return 0
    if day == N:
        return 1
    if dp[day][late][abs] == -1:
        dp[day][late][abs] = (dfs(day + 1, late, 0) 
                              + dfs(day + 1, late + 1, 0) 
                              + dfs(day + 1, late, abs + 1))
    return dp[day][late][abs]

print(dfs(0,0,0) % 1000000)