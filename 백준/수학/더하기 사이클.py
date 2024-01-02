import sys

input = sys.stdin.readline

N = int(input())
new_N = (10*(N % 10)) + (((N // 10) + (N % 10))%10)
count=1

while N != new_N:
  a = new_N // 10
  b = new_N % 10
  new_N = (10*b) + ((a+b)%10)
  count+=1
  
print(count)