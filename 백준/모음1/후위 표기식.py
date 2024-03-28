import sys

input = sys.stdin.readline

form = list(input().rstrip())
stack = []
answer = ''

for i in form:
  if i.isalpha():
    answer += i
  else:
    if i == '*' or i == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        answer += stack.pop()
      stack.append(i)
    elif i == '+' or i == '-':
      while stack and stack[-1] != '(':
        answer += stack.pop()
      stack.append(i)
    elif i == '(':
      stack.append(i)
    else:
      while stack and stack[-1] != '(':
        answer += stack.pop()
      stack.pop()


while stack:
  answer += stack.pop()

print(answer)