import sys

n,m = map(int,sys.stdin.readline().split())
weights = list(map(int,sys.stdin.readline().split()))
weights.insert(0,0)

peoples = {}

for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  
  
  if a not in peoples:
    peoples[a] = []
  if b not in peoples:
    peoples[b] = []
  peoples[a].append(b)
  peoples[b].append(a)
  # peoples.setdefault(a, []).append(b)
  # peoples.setdefault(b, []).append(a)

for i in range(1,n+1):
  if i not in peoples:
    peoples[i] = []

def isGreatest(me,other):
  for i in other:
    if weights[me] <= weights[i]:
      return False
  return True

result=0
for i in peoples.keys():
  if len(peoples[i]) == 0:
    result+=1
  else:
    if isGreatest(i,peoples[i]) == True:
      result+=1
print(result)
