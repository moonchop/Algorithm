import sys
from bisect import bisect_left,bisect_right


n=int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))  
m=int(sys.stdin.readline())
arr_check = list(map(int,sys.stdin.readline().split())) 
arr.sort()
result=[]

def binary_search(n):
  a = bisect_left(arr,n)
  b = bisect_right(arr,n)
  return b-a
for i in arr_check:
  print(binary_search(i),end=' ')

# def first(arr,target,start,end):
#   if start > end:
#     return None
#   mid = (start+end) // 2
#   if target == arr[mid] and arr[mid-1] < target:
#     return mid
#   elif target <= arr[mid]:
#     return first(arr,target,start,mid-1)
#   else:
#     return first(arr,target,mid+1,end)

# def last(arr,target,start,end):
#   if start > end:
#     return None
#   mid = (start+end) // 2
#   if target == arr[mid] and arr[mid+1] > target:
#     return mid
#   elif target < arr[mid]:
#     return last(arr,target,start,mid-1)
#   else:
#     return last(arr,target,mid+1,end)
  
  
# for i in arr_check:
#   first_index = first(arr,i,0,n-1) 
#   if first_index == None:
#     print(0,end=' ') 
#     continue
#   last_index = last(arr,i,0,n-1)
#   print(last_index-first_index,end=' ')
  