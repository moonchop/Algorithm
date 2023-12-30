import sys

input = sys.stdin.readline

K = int(input())

arr_input = list(map(int,input().split()))

answer = [[] for _ in range(K)]




def bfs(arr,depth):
  mid = len(arr)//2
  answer[depth].append(arr[mid])
  
  if len(arr) == 1:
    return
  
  bfs(arr[:mid],depth+1)
  bfs(arr[mid+1:],depth+1)
  
bfs(arr_input,0)
  
for i in answer:
  print(*i)