import re

expression = input()
print(sum(map(int, (expression.split('+')))))
expression = re.split('([-|+])',expression)
result=0
result=int(expression[0])
isMinus=False
for i in range(1,len(expression)-1):
  if expression[i] == '-':
    i+=1
    result-=int(expression[i])
    isMinus=True
  elif expression[i] == '+':
    i+=1
    if isMinus==True:
      result-=int(expression[i])
    else:
      result+=int(expression[i])

print(result)
