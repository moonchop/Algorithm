import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
arr=[]
abilities = []
min_val = sys.maxsize

for _ in range(N):
    arr.append(list(map(int,input().split())))
    
combi = list(combinations([x for x in range(N)],N//2))
for i in range(len(combi)//2):
    start,link = 0,0
    for c in combinations(combi[i],2):
      start += (arr[c[0]][c[1]] + arr[c[1]][c[0]])
    for c in combinations(combi[len(combi)-1-i],2):
      link += (arr[c[0]][c[1]] + arr[c[1]][c[0]])
    min_val = min(min_val,abs(start-link))
    
print(min_val)





