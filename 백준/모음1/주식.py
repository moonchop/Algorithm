import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
  n = int(input())
  price_arr = list(map(int,input().split()))
  max_value = 0
  answer = 0 
  for i in reversed(price_arr):
    if i > max_value:
      max_value = i
    else:
      answer += max_value-i
  print(answer)
'''
1 2 8 3 5
작으면 answer += max_value-i
크면 max_value 업데이트
'''