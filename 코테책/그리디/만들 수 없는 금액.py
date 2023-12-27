import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

target=1
for x in arr:
    if target < x:
        break
    target += x
print(target)