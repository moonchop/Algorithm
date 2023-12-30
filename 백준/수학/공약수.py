import sys
# from math import gcd
input = sys.stdin.readline

N = int(input())
input_arr = list(map(int,input().split()))

# input_arr.sort()
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

def gcd(a,b):
    while b!=0:
      a = a % b
      a, b = b, a
    return a
  
input_arr.sort()
  
gcd_num = input_arr[0]

for i in input_arr[1:]:
  gcd_num = gcd(gcd_num,i)

divisor = set()

for i in range(1,int(gcd_num**0.5)+1):
  if gcd_num % i == 0:
    divisor.add(i)
    divisor.add(gcd_num // i)


for i in sorted(divisor):
  print(i)

