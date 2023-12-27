import sys

n,m,k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort(reverse=True)
count=0
for i in range(1,m+1):
  
  if i%k==1 and i > k:
    count+=arr[1]
    continue
  count+=arr[0]
  
print(count)

# 내림차순으로 배열을 sort
# 1. M만큼 반복문 돌리고
# 2. i % k == 1 && i > k 일 때, 배열의 두번째를 더한다.
