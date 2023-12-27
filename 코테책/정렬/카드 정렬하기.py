import sys
from heapq import heappush, heappop

count=0
result=0
arr=[]
n = int(sys.stdin.readline())

# for _ in range(n):
#   arr.append(int(sys.stdin.readline()))
# arr.sort()

# while len(arr) != 1:
#   a = arr.pop(arr.index(min(arr)))
#   b = arr.pop(arr.index(min(arr)))
#   arr.append(a+b)
#   result+=(a+b)
#   arr.sort()
# print(result)

heap=[]
for _ in range(n):
  heappush(heap,int(sys.stdin.readline()))
  
while len(heap)!=1:
  a=heappop(heap)
  b=heappop(heap)
  result+=(a+b)
  heappush(heap,a+b)
  
print(result)

