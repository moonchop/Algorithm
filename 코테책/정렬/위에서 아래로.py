import sys

n = int(sys.stdin.readline())
arr=[]
# for i in range(n):
#     arr.append(sys.stdin.readline().strip())
arr = [sys.stdin.readline().strip() for _ in range(n)]

arr=sorted(arr,reverse=True)

print(arr)
