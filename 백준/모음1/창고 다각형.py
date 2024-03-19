import sys

input = sys.stdin.readline

max_idx = 0
max_val = 0
answer = 0

N = int(input())
arr = [0 for _ in range(1001)]

for _ in range(N):
  a,b = map(int,input().split())
  arr[a] = b
  if max_val < b:
    max_val = b
    max_idx = a

cursor = 0
for i in range(max_idx+1):
  cursor = max(cursor,arr[i])
  answer += cursor
  
cursor = 0
for i in range(1000,max_idx,-1):
  cursor = max(cursor,arr[i])
  answer += cursor
print(answer)