import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
dict=defaultdict(int)

for _ in range(N):
    name,extend = input().rstrip().split('.')
    dict[extend]+=1
    
for i in (sorted(list(dict.items()))):
    print(i[0], i[1])