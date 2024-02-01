import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    for index,value in enumerate(graph[i]):
        graph[i][index] = value + min(graph[i-1][(index+1)%3],graph[i-1][(index+2)%3])

print(min(graph[-1]))
    