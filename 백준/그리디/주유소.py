import sys

input = sys.stdin.readline

N = int(input())

distance = list(map(int,input().split()))
cost = list(map(int,input().split()))
temp = sys.maxsize
answer = 0

for i in range(N-1):
    if cost[i] >= cost[i+1] and cost[i] < temp:
        answer += cost[i]*distance[i]
    else:
        temp = min(temp,cost[i])
        answer += temp*distance[i]
        
print(answer)