import sys

stack=[]
temp=[]
result=[]
sentence = sys.stdin.readline().rstrip()

def reverse_word(word):
  word.reverse()  
  return ''.join(word)

for i in (sentence):
  if i == '<':
    if temp:
      result.append(reverse_word(temp))
      temp=[]
    stack.append(i) 
    result.append(i)
  elif i== '>':
    stack.pop()
    result.append(i)
  elif not stack and i==' ':
    if temp:
      result.append(reverse_word(temp))
      result.append(' ')
      temp=[]    
  else:
    result.append(i) if stack else temp.append(i)

if temp:
  result.append(reverse_word(temp))
  print(''.join(result))
else:
  print(''.join(result))


