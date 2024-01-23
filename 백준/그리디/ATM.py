import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

count = 0
answer = 0

for i in arr:
    answer += count+i
    count = count+i
print(answer)