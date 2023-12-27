import sys
from itertools import combinations
from collections import Counter

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

total_cnt = len(list(combinations(arr,2)))
dup_dict = dict(Counter(arr))

for i in dup_dict:
    if dup_dict.get(i) >=2:
        total_cnt -= len(list(combinations((dup_dict.get(i)*[0]),2)))

print(total_cnt)