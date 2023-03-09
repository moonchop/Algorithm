import sys
from bisect import bisect_left


n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))


result=-1

for i in range(n):
  print(arr[i],bisect_left(arr,arr[i]))
  if arr[i]==bisect_left(arr,arr[i]):
    result = arr[i]
print(result)

# def binary_search(arr,start,end):
#   if start > end:
#     return None
#   mid = (start+end)//2
#   if mid == arr[mid]:
#     return mid
#   elif mid >= arr[mid]:
#     return binary_search(arr,mid+1,end)
#   else:
#     return binary_search(arr,start,mid-1)
    
# print(binary_search(arr,0,n-1))