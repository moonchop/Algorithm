import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
visited = [False] * (N+1)
answer = [-1] * (N+1)
# visited[1] = True
graph = [[] for _ in range(N+1)]

def search(n):
  visited[n] = True
  for i in graph[n]:
    if visited[i] == False:
      answer[i] = n
      search(i)
      
      
for _ in range(N-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


search(1)
  
for i in answer[2:]:
  print(i)