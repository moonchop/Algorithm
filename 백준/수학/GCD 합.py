import sys
from itertools import combinations
import math
input = sys.stdin.readline

N = int(input())


for _ in range(N):
  arr = list(map(int,input().split()))[1:]
  answer = 0  
  for i in combinations(arr,2):
    gcd = math.gcd(i[0],i[1])

    answer += gcd
  print(answer)