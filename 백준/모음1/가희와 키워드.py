import sys

input = sys.stdin.readline

N, M = map(int,input().split())

keyword = set()
for _ in range(N):
  keyword.add(input().rstrip())

for _ in range(M):
  for i in input().rstrip().split(','):
    if i in keyword:
      N-=1
      keyword.remove(i)
  print(0) if N < 0 else print(N)