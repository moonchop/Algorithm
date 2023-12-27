import sys

sentences=[]

while True:
  sentence = sys.stdin.readline().rstrip()
  if sentence == '.':
    break
  sentences.append(sentence)


stack=[]
def isGood(sentence):
  stack=[]
  for i in (list(sentence)):
    if i in ['(','[']:
      stack.append(i)
    elif i in [']',')']:
      if len(stack)==0:
        return 'no'
      poped = stack.pop()
      if poped == '[' and i ==']' or poped == '(' and i ==')':
        pass
      else:
        return 'no'
    
  return 'yes' if not stack else 'no'

for sentence in sentences:
  print(isGood(sentence))
