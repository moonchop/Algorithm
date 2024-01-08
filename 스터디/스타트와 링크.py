import sys
from itertools import combinations,permutations

input = sys.stdin.readline

# N = int(input())
# arr=[]
# abilities = []

# for _ in range(N):
#     arr.append(list(map(int,input().split())))
    
# for i in (combinations([x for x in range(N)],2)):
#     a,b = i[0],i[1]
#     if a == b:
#         continue
#     abilities.append(arr[a][b]+arr[b][a])
    
# abilities.sort()
# mid = len(abilities)//2-1
# print(abilities)
# print(min(abs(abilities[mid]-abilities[mid-1]),abs(abilities[mid]-abilities[mid+1])))

