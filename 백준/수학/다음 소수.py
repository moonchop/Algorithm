import sys

input = sys.stdin.readline

def isPrime(num):
  if num ==0 or num==1:
    return False
  for i in range(2,int(num**(1/2)+1)):
    if num % i == 0:
      return False
  return True

N = int(input())

for _ in range(N):
  n = int(input())
  while True:
    if isPrime(n):
      print(n)
      break
    n+=1
    