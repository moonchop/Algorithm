import sys

n = int(sys.stdin.readline())

graph=[]
for _ in range(n):
  [name,kor,eng,math] = sys.stdin.readline().strip().split()
  graph.append([name,int(kor),int(eng),int(math)])

graph.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in graph:
  print(i[0])