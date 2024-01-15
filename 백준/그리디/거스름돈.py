import sys

input = sys.stdin.readline

N = int(input())

result = sys.maxsize

for i in range(N//5+1):
  five= 5*i
  if (N-five) % 2 == 0:
    result = min(result,i+int((N-five)//2))

if result == sys.maxsize:
  print(-1)

else:
  print(result)