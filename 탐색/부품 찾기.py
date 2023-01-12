import sys

##집합 자료형 이용
# n = sys.stdin.readline().rstrip()
# array_n = list(map(int,sys.stdin.readline().split()))

# m = sys.stdin.readline().rstrip()
# array_m = list(map(int,sys.stdin.readline().split()))

# union = list(set(array_n) & set(array_m))

# print(len(union) > 0 if "yes" else "no")

##이진 탐색
def binary(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    # if target == 9:
    #     print(array[mid],target,start,end)
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return binary(array,target,start,mid-1)
    else:
        return binary(array,target,mid+1,end)

n = int(sys.stdin.readline())
array_n = list(map(int,sys.stdin.readline().split()))
array_n.sort()
m = int(sys.stdin.readline())
array_m = list(map(int,sys.stdin.readline().split()))

for i in array_m:
    # print("i",i)
    result = binary(array_n,i,0,n-1)
    if result == None:
        print("no")
    else: print("yes")

##계수 정렬
