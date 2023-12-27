import sys,heapq,math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  M = int(input())
  left=[]
  right=[]
  arr_input = []
  for _ in range(math.ceil(M/10)):
    arr_input += (map(int,input().split()))
  
  mid = arr_input[0]
  answer=[mid]
  for i,v in enumerate(arr_input[1:]):
    if mid < v:
      heapq.heappush(right,v)
    else:
      heapq.heappush(left,-v)
    if (i+1) % 2 == 0:
      if len(left) > len(right):
        heapq.heappush(right,mid)
        mid = -heapq.heappop(left)
      elif len(left) < len(right):
        heapq.heappush(left,-mid)
        mid = heapq.heappop(right)
      answer.append(mid)
      
  print(len(answer))
  for i in range(len(answer)):
    print(answer[i],end=' ')
    if (i+1) % 10 == 0:
      print()