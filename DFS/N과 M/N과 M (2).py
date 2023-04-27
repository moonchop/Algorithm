import sys

n,m = map(int,sys.stdin.readline().split())
d=[]
def dfs(k):
  if len(d) == m:
    print(" ".join(map(str,d)))
  for i in range(1,n+1):
    if i not in d and k < i:
      d.append(i)
      dfs(i)
      d.pop()
      
dfs(0)