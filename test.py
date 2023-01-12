import sys


def binary(array,target,start,end):
  if start > end:
    return None
  mid=(start+end)//2
  
  if mid == target:
    return mid
  elif target < array[mid]:
    return binary(array,target,start,mid-1)
  else:
    return binary(array,target,mid+1,end)


n,target = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

result = binary(array,target,0,n-1)
if result ==None:
  print("XXXXX")
else:
  print(result)