import sys

n,m = map(int,sys.stdin.readline().split())
n_arr=[]
m_arr=[]

for _ in range(n):
  n_arr.append(sys.stdin.readline().rstrip())
for _ in range(m):
  m_arr.append(sys.stdin.readline().rstrip())

def is_include(word):
  for i in n_arr:
    if word == i:
      return True
  return False 

result =0
for i in m_arr:
  if is_include(i) == True:
    result+=1
    
print(result)