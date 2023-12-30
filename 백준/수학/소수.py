import sys

input = sys.stdin.readline

M = int(input())
N = int(input())

def isPrime(n):
  if n ==1:
    return False

  for i in range(2, n//2+1):
    if n%i==0:
      return False
  return True

def isPrime2(n):
  if n == 1:
    return False
  if n==2:
    return True
  if n%2 == 0:
    return False
  for i in range(3,int(n**0.5)+1,2):
    if n%i ==0:
      return False
  return True


sum_val = 0
min_val = 0

for i in range(M, N+1):
  if isPrime2(i):
    if sum_val == 0:
      min_val = i
    sum_val += i
    
    
    
if sum_val==0:
  print(-1)
else:
  print(sum_val)
  print(min_val)