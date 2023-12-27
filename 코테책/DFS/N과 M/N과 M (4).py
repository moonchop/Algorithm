import sys

n,m = map(int,sys.stdin.readline().split())

d=[]
def dfs(k):
  if len(d)==m:
    print(" ".join(map(str,d)))
    return
  for i in range(k,n+1):
      d.append(i)
      dfs(i)
      d.pop()
      
dfs(1)