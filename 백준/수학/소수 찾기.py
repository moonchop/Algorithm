import sys

input = sys.stdin.readline

answer =0

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


N = int(input())
input_arr = list(map(int,input().split()))
for i  in input_arr:
  answer += int(isPrime2(i))

  
print(answer)