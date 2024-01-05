import sys

input = sys.stdin.readline

N,K = map(int,input().split())

primes=[]
isPrimes = [False,False] + [True]*(N-1)
answer=0

for i in range(2,N+1):
    for j in range(i,N+1,i):
      if isPrimes[j] == False:
        continue
      isPrimes[j] = False
      K-=1
      if K==0:
        answer = j

      

print(answer)
