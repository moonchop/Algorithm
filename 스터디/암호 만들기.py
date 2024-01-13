import sys
from itertools import permutations

input = sys.stdin.readline

L,C = map(int,input().split())
arr = list(map(str,input().split()))


mo_cnt = 1
ja_cnt = 2
answer=[]
visited = [False] * C


def isMo(c):
  if c in ['a','e','i','o','u']:
    return True
  return False

def dfs(word,mo_cnt,ja_cnt):
  if len(word) == L and mo_cnt < 1 and ja_cnt < 1:
    answer.append(word)
    return
  
  
  for i in range(C):
    if not visited[i]:
      if len(word) == 0:
        visited[i] = True
        dfs(word+arr[i],mo_cnt-1,ja_cnt) if isMo(arr[i]) else dfs(word+arr[i],mo_cnt,ja_cnt-1) 
      else:
        visited[i] = True
        if word[-1] <= arr[i]:
          dfs(word+arr[i],mo_cnt-1,ja_cnt) if isMo(arr[i]) else dfs(word+arr[i],mo_cnt,ja_cnt-1) 
      visited[i] = False
  
dfs('',mo_cnt,ja_cnt)  

for i in sorted(answer):
  print(i)

