input_ = input()

input_ = input_.replace('[]','3')
input_ = input_.replace('()','2')



s=[]
n=1
result=0

for i in range(len(list(input_))):
    if input_[i] == '(':
      s.append('(')
      n*=2
    elif input_[i] == '[':
      s.append('[')
      n*=3
    elif input_[i] == '2':
      n*=2
      result += n
      n//=2
    elif input_[i] == '3':
      n*=3
      result += n
      n//=3
    elif input_[i] == ')':
      if not s or s[-1] != '(':
        result=0
        break
      s.pop()
      n//=2
    elif input_[i] == ']':
      if not s or s[-1] != '[':
        result=0
        break
      s.pop()
      n//=3

if s:
  result = 0
print(result)