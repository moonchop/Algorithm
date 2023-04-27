import sys


n,m = map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
  arr.append(list(map(int,sys.stdin.readline().split())))

min_arr=[] 
for row in arr:
  min_arr.append(min(row))
  
print(max(min_arr))