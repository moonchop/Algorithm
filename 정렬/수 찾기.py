import sys

n=int(sys.stdin.readline())
n_arr = list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
m_arr = list(map(int,sys.stdin.readline().split()))

n_arr.sort()

def binary_search(target,start,end):
  if start > end:
    return False
  
  mid = (start+end) // 2
  
  if target == n_arr[mid]:
    return True
  elif target > n_arr[mid]:
    return binary_search(target,mid+1,end)
  else:
    return binary_search(target,start,mid-1)


for i in m_arr:
  # print(0 ifbinary_search(i,0,n-1))
  print(1 if binary_search(i,0,n-1) else 0 )
  # print(1 if i in n_arr else 0)