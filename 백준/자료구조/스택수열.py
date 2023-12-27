

n = 1
idx = 0

stack = []
answer = []
arr = []
check = []

n_ = int(input())
for i in range(n_):
  arr.append(int(input()))
  
while len(check) != len(arr):
  if n > n_:
    if stack[-1] != arr[idx]:
      answer=[]
      break
    check.append(stack.pop())
    idx += 1
    answer.append('-')
  else:
    if len(stack) != 0 and stack[-1] == arr[idx]:
        check.append(stack.pop())
        idx += 1
        answer.append('-')
    else:
        stack.append(n)
        n+=1
        answer.append('+')

if len(answer) == 0:
  print('NO')
else:
  for i in answer:
    print(i)
    
    
    
    
