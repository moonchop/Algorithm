import sys

n,m = map(int,sys.stdin.readline().split())
d=[]
def dfs():
  if len(d) == m:
    print(" ".join(map(str,d)))
  for i in range(1,n+1):
    if i not in d:
      d.append(i)
      dfs()
      d.pop()
      
dfs()