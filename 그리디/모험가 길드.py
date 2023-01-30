import sys

n = int(sys.stdin.readline())

arr = map(int,sys.stdin.readline().split())

count=0
result=0

for i in arr:
    count +=1
    if count >= i:
        result+=1
        count=0
    
print(result)