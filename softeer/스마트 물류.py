import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().strip())

result=0

for i in range(n):
  if arr[i] == 'P':
    for L in range(k,0,-1):
      if i-L >= 0:
        if arr[i-L] == "H":
          arr[i-L] = "X"
          arr[i] = "X"
          result+=1
          break
    if arr[i] == 'P':
      for R in range(1,k+1):
        if i+R < n:
          if arr[i+R] == "H":
            arr[i+R] = "X"
            arr[i] = "X"
            result+=1
            break

print(result)