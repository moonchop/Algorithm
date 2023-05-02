import sys

visited=[False]*9
visited2=[False]*9

graph=[[],
       [2,3,8],
       [1,7],
       [1,4,5],
       [3,5],
       [3,4],
       [7],
       [2,6,8],
       [1,7]
       ]

def dfs(v):
  visited[v]=1
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(i)


def dfs_stack(v):
  stack=[v]
  visited2[v]=True
  print(v,end=' ')
  while stack:
    v = stack.pop()
    for i in graph[v]:
      if not visited2[i]:
        stack.append(i)
        visited2[i]=True
        print(i,end=' ')
        
dfs(1)
print()
dfs_stack(1)
