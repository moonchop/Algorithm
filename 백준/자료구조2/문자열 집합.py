N,M = map(int,input().split())

target_arr = []
arr={}
answer=0

for _ in range(N):
  arr[input()] = True
  
for _ in range(M):
  target_arr.append(input())
  
for i in target_arr:
  if i in arr:
    answer+=1
    
print(answer)