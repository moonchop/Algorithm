
n_ = int(input())
answer = []

for _ in range(n_):
  arr=[]
  count=0
  N, M = map(int,input().split())
  arr = list(map(int,input().split()))

  index = M

  if len(arr) == 1:
    answer.append(1)
    continue
  
  while True:
    if len(arr) < 2:
      count+=1
      break
    if arr[0] >= max(arr[1:len(arr)]):
      arr.pop(0)
      count+=1
      if index == 0:
        break
      else:
        index-=1
    else:
      arr.append(arr.pop(0))
      if index==0:
        index = len(arr)-1
      else: index-=1
    
  answer.append(count)

for i in answer:
  print(i)

