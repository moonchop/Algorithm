import sys

n,m = map(int,sys.stdin.readline().split())
range_list = list(map(int,sys.stdin.readline().split()))
range_list.sort()
d=[]

def dfs():
  if len(d) == m:
    print(" ".join(map(str,d)))
    return
  
  for i in range_list:
    if i not in d:
      d.append(i)
      dfs()
      d.pop()
      
dfs()