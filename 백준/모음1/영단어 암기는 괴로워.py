import sys
from collections import defaultdict

input = sys.stdin.readline

N,M = map(int,input().split())
dict = defaultdict(int)

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        dict[word]+=1
for i in sorted(list(dict.items()),key=lambda x:(-x[1],-len(x[0]),x[0])):
    print(i[0])