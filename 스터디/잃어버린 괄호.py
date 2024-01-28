import sys

input = sys.stdin.readline

input_arr = list(input().rstrip())

arr=[]
answer=0
temp = ''

for i in input_arr:
  if i=='+' or i=='-':
    arr.append(temp)
    arr.append(i)
    temp=''
  else:
    temp+=i
else:
  arr.append(temp)

is_minus = False
for i in range(len(arr)):
  if arr[i] == '-':
    is_minus = True
  elif arr[i]=='+':
    pass
  elif is_minus:
    answer -= int(arr[i])
  else:
    answer += int(arr[i])

print(answer)
    
    
  