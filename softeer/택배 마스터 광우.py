import sys
from itertools import permutations

n,m,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr_permu = permutations(arr,n)


result=sys.maxsize

for rail in arr_permu:
  elem = list(rail)
  exc_count=0
  temp=0
  i=0
  total=0
  while exc_count != k :
    if temp+elem[i] <=m:
      temp+=elem[i]
      i+=1
      i%=n
    else:
      total+=temp
      temp=0
      exc_count +=1
  result = min(result,total)
print(result)