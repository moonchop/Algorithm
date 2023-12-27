N = int(input())
arr =  list(map(int,input().split()))
visited = [False] * (N)
index = 0
answer=[]

while True:
  
  popped = arr[index]
  arr[index] = 0
  visited[index] = True
  answer.append(index+1)
  count = abs(popped)
  
  if False not in visited:
    break
  
  if popped > 0:
    while count > 0:
      index = (index+1) % N 
      
      if arr[index] != 0:
        count -= 1
  else:
    while count > 0:
      index -= 1
      if index < 0:
        index = N-1
      
      if arr[index] != 0:
        count -= 1
      
      
