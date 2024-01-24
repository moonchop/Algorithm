# import sys

# input = sys.stdin.readline

# N = int(input())

# distance = list(map(int,input().split()))
# cost = list(map(int,input().split()))

# i=0
# j=1
# answer = 0

# while i < N-1 or j < N-1:
#   if cost[i] >= cost[j]:
#     answer += distance[i]*cost[i]
#     i+=1
#     j=i
#   else:
#     answer+=cost[i]*distance[j-1]
#     j+=1
  
# print(answer)