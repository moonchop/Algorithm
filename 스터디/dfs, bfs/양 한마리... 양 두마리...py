import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x,y):
    if x >= h or y >= w or x < 0 or y < 0:
        return False
    if arr[x][y]=='#':
        arr[x][y] = '.'
        
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        
        return True
    return False

N = int(input())

for _ in range(N):
    arr=[]
    h, w = map(int,input().split())
    answer = 0

    for _ in range(h):
        arr.append(list(input().rstrip()))
        
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                answer+=1
                
    print(answer)