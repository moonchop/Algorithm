import sys

n, m = map(int,sys.stdin.readline().split())
array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

d = [10001] * (m+1)

d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
