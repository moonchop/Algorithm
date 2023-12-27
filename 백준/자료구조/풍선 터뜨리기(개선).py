from collections import deque

N = input()
q = deque(enumerate(map(int,input().split())))


answer = []
while q:
  idx, value = q.popleft()
  answer.append(idx+1)
  
  if value > 0:
    q.rotate(-(value-1))
  else:
    q.rotate(-value)

for i in answer:
  print(i,end=' ')