import sys

#input
N,M,K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

#1.정렬
arr.sort(reverse=True)

#2.인덱스 선택
a,b=arr[0:2]
sum=0
count=0
state=0

#3,4,5
def iterate(num):
  global sum
  global count
  global state
  for _ in range(K):
    print(count,num)
    if count == M:
      return
    sum+=num
    count+=1
  state+=1

while(count < M):
  if state%2 == 0:
    iterate(a)
  else:
    sum+=b
    state+=1
    count+=1
print(sum)


##init
# 1.오름차순으로 정렬
# 2. 1,2번째 인덱스를 선택


