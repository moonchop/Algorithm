import sys,math

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

def is_prime(n):
  for i in range(2,int(n**(1/2)+1)):
    if n%i == 0:
      return False
  return True

    
primes = list(set([i for i in arr if is_prime(i)]))


gcd = math.gcd(*primes)
mul_prime = math.prod(primes)


if len(primes) > 0:
  print(mul_prime//gcd)
else:
  print(-1)
