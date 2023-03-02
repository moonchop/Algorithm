import sys

n = int(sys.stdin.readline())

sums=0
results=[]
location = list(map(int,sys.stdin.readline().split()))

location.sort()

print(location[n//2-1] if n%2==0 else location[n//2])


