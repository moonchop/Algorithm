import sys
import math

input = sys.stdin.readline

a,b = map(int,input().split())

def gcd(a,b):
  while b > 0:
    a = a % b
    a,b = b,a
  return a


print(gcd(a,b))
print(math.lcm(a,b))