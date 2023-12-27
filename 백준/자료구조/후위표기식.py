input_ = input()
stack=[]
answer=''

for i in list(input_):
  if i.isalpha():
    answer+=i
  else:
    if i == '/' or i == '*':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        answer+=stack.pop()
      stack.append(i)
    elif i == '+' or i == '-':
      while stack and stack[-1] !='(':
        answer+=stack.pop()
      stack.append(i)
    elif i == '(':
      stack.append(i)
    elif i == ')':
      while stack and stack[-1] !='(':
        answer+=stack.pop()
      stack.pop()  
      
while stack:
  answer+=stack.pop()
  
print(answer)
    
# /*에 대한 우선순위 -> stack[-1]이 * /일때 pop
# +-에 대한 우선순위 -> !=( 때까지 pop
# (에 대한 우선순위 -> append
# )에 대한 우선순위 -> !=( 때까지 pop