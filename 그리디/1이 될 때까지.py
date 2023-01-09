# -*- coding: utf-8 -*- 
import sys

N,K = map(int,sys.stdin.readline().split())

result=0

while(N!=1):
  if(N%K==0):
    N//=K
    result+=1
  else:
    N=N-1
    result+=1
print(result)
    


##init
#1.N%K==0이면 나누고, 아니면 N에서 -1을 한다.
#2.1번의 모든 행위에 count를 증가시켜 최소 횟수를 구한다. 
#3.최소 횟수이므로 나누는 것을 우선순위로 둔다. 