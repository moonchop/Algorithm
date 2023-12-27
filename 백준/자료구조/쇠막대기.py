

input_ = input()
input_ = input_.replace('()','*')

n=0
answer=0

arr = list(input_)
for i in arr:
  if i=='(':
    answer+=1
    n+=1
  elif i==')':
    n-=1
  elif i=='*':
    answer+=n
    
print(answer)
