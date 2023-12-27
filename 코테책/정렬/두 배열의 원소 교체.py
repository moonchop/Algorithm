import sys

n,k = map(int,sys.stdin.readline().split())

print(n,k)
arr_1=[]
arr_2=[]

arr_1 = list(map(int,sys.stdin.readline().split()))
arr_2 = list(map(int,sys.stdin.readline().split()))

arr_1=sorted(arr_1)
arr_2=sorted(arr_2,reverse=True)

for i in range(k):
    if arr_1[i] < arr_2[i]:
        arr_1[i],arr_2[i] = arr_2[i],arr_1[i]
    else:
        break
    
print(sum(arr_1))