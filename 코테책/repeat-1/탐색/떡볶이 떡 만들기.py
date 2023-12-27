import sys

n, m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result=0

def binary_search(start,end):
  global result
  if start > end:
    return None
  cut_sum=0
  mid = (start+end)//2
  for i in range(n):
    if arr[i] > mid:
      cut_sum+=arr[i]-mid

  if cut_sum < m:
    return binary_search(start,mid-1)
  else:
    result=mid
    return binary_search(mid+1,end)
  
binary_search(0,max(arr))
print(result)