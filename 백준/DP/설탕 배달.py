import sys

input = sys.stdin.readline

N = int(input())

min_val = sys.maxsize

for i in range(N//5,-1,-1):
    if 5*i == N:
        min_val = i
        break
    three = (N-(5*i)) % 3
    if three == 0:
        min_val = min(min_val, (N-(5*i))//3+i)
        break

if min_val == sys.maxsize:
    print(-1)
else:
    print(min_val)