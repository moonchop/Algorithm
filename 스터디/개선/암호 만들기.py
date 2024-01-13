import sys
from itertools import permutations

input = sys.stdin.readline

L,C = map(int,input().split())
arr = list(map(str,input().split()))


answer=[]
visited = [False] * C

def isWord(word):
  mo_cnt=0
  ja_cnt=0
  for i in word:
    if i in ['a','e','i','o','u']:
      mo_cnt+=1
    else:
      ja_cnt+=1
    if mo_cnt >=1 and ja_cnt>=2:
      return True
  return False
def dfs(word):
  if len(word) == L:
    if isWord(word):
      answer.append(word)
      return
  
  for i in range(C):
    if not visited[i]:
      if len(word) == 0:
        visited[i] = True
        dfs(word+arr[i])
      else:
        visited[i] = True
        if word[-1] <= arr[i]:
          dfs(word+arr[i])
      visited[i] = False
  
dfs('')  

for i in sorted(answer):
  print(i)

