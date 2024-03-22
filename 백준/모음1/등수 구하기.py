import sys
from collections import defaultdict

input = sys.stdin.readline

N, new, P = map(int,input().split())
if N == 0:
  print(1)
else:
  arr = list(map(int,input().split()))
  
  if N >= P and arr[-1] >= new:
    print(-1)
  else:
    for i in range(N):
      if arr[i] <= new:
        print(i+1)
        break
    else:
      print(N+1)
