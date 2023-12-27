import sys

n = int(sys.stdin.readline())
graph=[]
result=0
temp=0
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))
  
  for row in range(1,n):
    for i in range(len(graph[row])):
      if i==0:
        graph[row][i] = graph[row][i]+graph[row-1][0]
      elif i==len(graph[row])-1:
        graph[row][i] = graph[row][i]+graph[row-1][i-1]
      else:
        graph[row][i] = graph[row][i]+max(graph[row-1][i],graph[row-1][i-1])

  print(max(graph[n-1]))
      


# 1. 행의 최대 값을 골라 2개 중 큰 걸 골라서 더한다.
# 2. 다음 행의 최대값을 골라 그 전 층과 더한다.
# 3. 1번 2번 중 더 큰 걸 선택하여 다시 1번부터 시작한다.
