import sys,math

input = sys.stdin.readline

n = 0.1
max_value = ''
min_value = ''
word = input().rstrip()

n = 1/10
count=0

for i in word:
  if i=='M':
    count += 1
  else:
    if count > 0:
      max_value += str((10**count)*5)
      min_value += str((10**count)+5)
    else:
      max_value += '5'
      min_value += '5'
    count = 0
if count > 0:
  max_value += '1'*count
  min_value += str(10**(count-1))
print(max_value)
print(min_value)



'''
1. 큰것
  M면 *10
  K면 *50
2. 작은것
  M면 *10
  K면 n을 answer+=하고, 5도 +=하고, n초기화 후 넘어가자

MMM
111
100  
'''
