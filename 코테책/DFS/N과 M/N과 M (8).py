import sys

n,m = map(int,sys.stdin.readline().split())
range_list = list(map(int,sys.stdin.readline().split()))
range_list.sort()
d=[]

def dfs(k):
  if len(d) == m:
    print(" ".join(map(str,d)))
    return
  
  for i in range(k,n):
    d.append(range_list[i])
    dfs(i)
    d.pop()
    
dfs(0)