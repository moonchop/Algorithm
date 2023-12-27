import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
visited = [False] * (N+1)
answer = [-1] * (N+1)
graph = [[] for _ in range(N+1)]

def stack(n):
  visited[n]= True
  q=[n]
  while q:
    x = q.pop()
    for i in graph[x]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        answer[i] = x
      
for _ in range(N-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


stack(1)
  
for i in answer[2:]:
  print(i)