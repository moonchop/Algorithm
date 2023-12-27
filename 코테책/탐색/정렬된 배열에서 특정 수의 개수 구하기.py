# import sys

# n,x = map(int,sys.stdin.readline().split())
# array = list(map(int,sys.stdin.readline().split()))


# def first(array,target,start,end):
#   if start > end:
#     return None
#   mid=(start+end)//2
#   if array[mid-1] < target and target == array[mid]:
#     return mid
#   elif array[mid] < target:
#     return first(array,target,mid+1,end)
#   else:
#     return first(array,target,start,mid-1)
    
# def last(array,target,start,end):
#   if start > end:
#     return None
#   mid=(start+end)//2
#   if array[mid+1] > target and target == array[mid]:
#     return mid
#   elif array[mid] <= target:
#     return last(array,target,mid+1,end)
#   else:
#     return last(array,target,start,mid-1)


# a=first(array,x,0,n-1)
# if a==None:
#   print(-1)
# else:
#   b=last(array,x,0,n-1)
#   print(b-a+1)
  
  
import sys
from bisect import bisect_left, bisect_right
n,x = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

def count_by_range(array,n):
  right_index = bisect_right(array,n)
  left_index = bisect_left(array,n)

  return right_index-left_index

count = count_by_range(array,x)
print(count)