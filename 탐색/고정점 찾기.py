import sys
from bisect import bisect_right,bisect_left


n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))


result=-1

for i in range(n):
  if arr[i]==bisect_left(arr,i):
    result = arr[i]
print(result)