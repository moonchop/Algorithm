import sys

input = sys.stdin.readline

X, Y = map(int,input().split())
x, y, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(X)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 북동남서
answer = 0

while True:
  if graph[x][y] == 0:
    answer += 1
    graph[x][y] = 2
  
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx >= X or ny >= Y or nx < 0 or ny < 0:
      continue
    if graph[nx][ny] == 0:
      break
  else:
    #0이 없는 경우
    nx = x+dx[(d+2) % 4]
    ny = y+dy[(d+2) % 4]
    if nx >= X or ny >= Y or nx < 0 or ny < 0 or graph[nx][ny] == 1:
      break
    x, y = nx, ny
    continue
  
  #0이 있는 경우
  d = (d+3) % 4
  nx = x+dx[d]
  ny = y+dy[d]
  if graph[nx][ny] == 0:
    x, y = nx, ny

print(answer)

# 북(0) -> 서(3)
# 서(3) -> 남(2)
# 동(1) -> 북(0)
# 남(2) -> 동(1)

