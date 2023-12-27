import sys

n = int(sys.stdin.readline())
store_arr= list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
want_arr = list(map(int,sys.stdin.readline().split()))

def binary_search(target,start,end):
  if start > end:
    return 'no'
  mid = (start+end) // 2
  if store_arr[mid] == target:
    return 'yes'
  elif store_arr[mid] > target:
    return binary_search(target,start,mid-1)
  else:
    return binary_search(target,mid+1,end)
  

for i in want_arr:
  print(binary_search(i,0,len(store_arr)-1),end=' ')

