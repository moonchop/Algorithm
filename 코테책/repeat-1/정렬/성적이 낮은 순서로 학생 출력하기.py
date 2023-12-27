import sys

n = int(sys.stdin.readline())
arr=[]
for _ in range(n):
  a,b= map(str,sys.stdin.readline().split())
  arr.append((a,int(b)))

arr= sorted(arr,key= lambda x:x[1])

for i in arr:
  print(i[0],end=' ')