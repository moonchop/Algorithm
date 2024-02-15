import sys

input = sys.stdin.readline

N = int(input())


def dfs(target, n):
    global answer
    if n > target:
        return 0
    if n == target:
        answer += 1
        return answer
    
    dfs(target,n+1)        
    dfs(target,n+2)        
    dfs(target,n+3)        
for _ in range(N):
    n = int(input())
    answer = 0
    dfs(n, 0)
    print(answer)