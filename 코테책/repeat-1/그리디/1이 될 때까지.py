import sys

n,k = map(int,sys.stdin.readline().split())
count=0
while(n!=1):
  if n%k == 0:
    n/=k
  else:
    n-=1
  count+=1
  
print(count)
# 1. if N%k==0이라면 N /= k
# 2. 아니라면 N-1
# 3. count++
# 4. N==1이라면 break
