import sys

input = sys.stdin.readline

A,B,C,M = map(int,input().split())

hour = 0 
crt_tired = 0
crt_work = 0

while hour < 24:
  if crt_tired + A > M:
    crt_tired -= C
    if crt_tired < 0:
      crt_tired = 0
  else:
    crt_work += B
    crt_tired += A
  hour+=1
  
print(crt_work)
print(hour)