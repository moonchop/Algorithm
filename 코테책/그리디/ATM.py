import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
result=0
for i in range(1,n+1):
  result+=sum(arr[:i])
  
print(result)