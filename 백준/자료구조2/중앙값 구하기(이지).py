import sys,math
input = sys.stdin.readline


T = int(input())
for _ in range(T):
  M = int(input())
  arr = []
  answer=[]
  for _ in range(math.ceil(M/10)):
    temp = list(map(int,input().split()))
    for i,v in enumerate(temp):
      arr.append(v)
      if (i+1) % 2 != 0:  
        arr.sort()
        mid = arr[len(arr)//2]
        answer.append(mid)
        
        
  print(len(answer))
  for i in range(len(answer)):
    print(answer[i],end=' ')
    if (i+1) % 10 == 0:
      print()