import sys

input = sys.stdin.readline

H, W = map(int,input().split())
block = list(map(int,input().split()))

graph = [[False]*W for _ in range(H)]
answer = 0

for i in range(W):
  for j in range(block[i]):
    graph[(H-1)-j][i] = True
  



for i in range(H):
  temp=0
  for j in range(1,W):
    if graph[i][j] == False and graph[i][j-1] == True:
      graph[i][j] = True
      temp+=1
      continue  
    
    if graph[i][j] == True and temp > 0:
      answer += temp
      temp=0
      
print(answer)     