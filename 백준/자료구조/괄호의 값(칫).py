word = input()

s = []
result = 0
n = 1

for i in range(len(word)):
  if word[i] == '(':
    s.append('(')
    n*=2
  elif word[i] == '[':
    s.append('[')
    n*=3
  elif word[i]==')':
    if not s or s[-1] != '(':
      result = 0
      break
    if word[i-1]=='(':
      result += n
    s.pop()
    n //= 2
  elif word[i]==']':
    if not s or s[-1] != '[':
      result = 0
      break
    if word[i-1]=='[':
      result += n
    s.pop()
    n //= 3

if s:
  result=0
  
print(result)