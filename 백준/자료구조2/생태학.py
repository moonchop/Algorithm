import sys
from collections import Counter


# arr = []
# dict = {}
# answer=[]
# count=0

# while True:
#   try:
#     input_ = sys.stdin.readline().rstrip()
#     if not input_:
#       break
#     else:
#       count+=1
#       if input_ in dict:
#         dict[input_] += 1
#       else:
#         dict[input_] = 1
#   except:
#     break


# for key,value in (dict.items()):
#   counted = round(value / count * 100)
#   answer.append(f'{key} {counted:.4f}')

# for i in sorted(answer):
#   print(i)

arr=[]
while True:
  try:
    input_ = sys.stdin.readline().rstrip()
    if not input_:
      break
    else:
      arr.append(input_)
  except:
    break

for item in (sorted(Counter(arr).items())):
  print(f'{item[0]} {item[1]/len(arr)*100:.4f}')