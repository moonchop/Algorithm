import sys

input = sys.stdin.readline

N = int(input())
answer = 0
tips = []

for i in range(N):
    tips.append(int(input()))
    
tips.sort(reverse=True)
    
for i in range(N):
    if tips[i]-i > 0:
        answer += (tips[i]-i)
print(answer)
