import sys

n, m = map(int,sys.stdin.readline().split())
x,y,direction = map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
  arr.append(list(map(int,sys.stdin.readline().split())))

# 북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]
result=1
dup_count=0
arr[x][y]=2
# 1. 4번 반복한다.
# 1-1. 바다면 turLeft해서 다시 확인한다.
# 1-2. 육지면 위치를 옮기고,그 자리를 0에서 1로 바꾼다.
# 2. 다 바다면 direction은 유지하고, 한칸 뒤로 가서 1단계를 반복한다.
# (단, 뒤쪽방향이 바다인 칸이면 실행을 종료한다)

def turnLeft():
  global direction
  direction-=1
  if direction == -1:
    direction = 3
    
while True:
  turnLeft()
  nx = dx[direction] + x
  ny = dy[direction] + y
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    break
  print(nx,ny)
  if arr[nx][ny]==0:
    arr[nx][ny]=2
    x = nx
    y = ny
    result+=1
    dup_count=0
    continue
  else:
    dup_count+=1
  
  # 모두 갈 수 없는 경우
  if dup_count==4:
    nx = x - dx[direction]
    ny = y - dy[direction]

    if arr[x][y]==0:
      x=nx
      y=ny
    else:
      break
    dup_count=0
    
print(result)