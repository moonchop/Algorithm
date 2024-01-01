import sys

input = sys.stdin.readline

N = int(input())
i=2
answer = []

while N != 1:
  if N % i == 0:
    answer.append(i)
    N //= i
    i=2
    continue
  i+=1

for answer in answer:
  print(answer)
