import sys


n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    input_data = sys.stdin.readline().split()
    arr.append((input_data[0],int(input_data[1])))
# arr = [sys.stdin.readline().split() for _ in range(n)]

def setting(data):
    return data[1]

arr = sorted(arr,key=setting)
for i in arr:
    print(i[0],end=' ')