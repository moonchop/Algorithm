import sys

n,m = map(int,sys.stdin.readline().split())
range_list = list(map(int,sys.stdin.readline().split()))
range_list.sort()
d=[]
result={}
visited=[False] * (n+1)
def dfs(k):

  if len(d)==m:
    temp = ' '.join(map(str,d))
    if temp not in result:
      result[temp] = 1
      print(temp)
    return
  for i in range(k,n):
      d.append(range_list[i])
      dfs(i)
      d.pop()
      
dfs(0)


