import sys
from collections import deque

input = sys.stdin.readline


max_val = ''
min_val = ''
visited = [False]*10

N = int(input())
sign_arr = list(input().split())

def check_sign(a,b,sign):
  return a < b if sign == '<' else a > b


def dfs(n_str):
  global max_val,min_val
  for i in range(10):
    
    if N+1 == len(n_str):
      if len(min_val)==0:
        min_val = n_str
      else:
        max_val = n_str
      return
    if not visited[i]:
      if len(n_str)==0 or check_sign(int(n_str[-1]),i,sign_arr[len(n_str)-1]):
        visited[i] = True
        dfs(n_str + str(i))
        visited[i] = False        
    

dfs('')
print(max_val)
print(min_val)