import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

answer = [0] * N

for i in range(N):
  count=0
  for j in range(N):
      if count == arr[i] and answer[j] == 0:
        answer[j] = i+1
        break
      elif answer[j]==0:
        count += 1
        
print(*answer)