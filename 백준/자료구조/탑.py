

num_ = input()
nums = list(map(int,input().split(' ')))

answer=[]
stack=[]

for i in range(len(nums)):
  while stack:
    if stack[-1][1] < nums[i]:
      stack.pop()
      if len(stack) == 1 and stack[-1][1] < nums[i]:
        answer.append(0)
        break
    else:
      answer.append(stack[-1][0]+1)
      break
  if len(stack)==0:
    answer.append(0)
  stack.append((i,nums[i]))
  

for i in answer:
  print(i,end=' ')