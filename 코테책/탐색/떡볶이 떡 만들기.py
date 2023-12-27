import sys

n,m = map(int,sys.stdin.readline().split())

array = list(map(int,sys.stdin.readline().split()))

# min_val = min(array)
# total=0

# while total != m:
#     array_sum=[]
#     for i in array:
#         if i-min_val > 0:
#             array_sum.append(i-min_val)
#         else: array_sum.append(0)
#     total=sum(array_sum)
#     print(total,m)
#     min_val+=1
# print(min_val-1)

## 개선 버전(이진 탐색)
start=0
end=max(array)
while start <= end:
    mid = (start+end) // 2
    total=0
    for x in array:
        if x > mid:
            total += x-mid
    
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)
        



##init
# 1.이진탐색 -> 최소값 뽑고, 합이 M이 될때까지 자름.