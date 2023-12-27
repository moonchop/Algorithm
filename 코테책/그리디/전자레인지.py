import sys

n = int(sys.stdin.readline())

T=[300,60,10]
result=[]
for i in T:
  result.append(n//i)
  n%=i
  
if n!=0:
  print(-1)
else:
  for i in result:
    print(i,end=' ')