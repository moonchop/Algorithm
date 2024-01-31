import sys

input = sys.stdin.readline

N = int(input())
meeting = []
answer = 0

for _ in range(N):
    a, b = map(int,input().split())
    meeting.append((a,b))

meeting.sort(key=lambda x: (x[1], x[0]))
check=0
for i in meeting:
    if check <= i[0]:
        answer +=1
        check = i[1]
print(answer)

