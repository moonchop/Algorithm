import sys
import math

input = sys.stdin.readline

N = int(input())

def gcd(a,b):
  while b > 0:
    a = a % b
    a,b = b,a
  return a

def lcm(a,b):
  gcd_num = gcd(a,b)
  return gcd_num * ( a//gcd_num) *  (b//gcd_num)
for _ in range(N):
  a,b = map(int,input().split())
  print(lcm(a,b))
