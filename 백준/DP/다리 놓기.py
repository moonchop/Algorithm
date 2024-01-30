import sys, math


input =  sys.stdin.readline

N = int(input())
for _ in range(N):
    a,b = map(int,input().split())

    temp = 1
    for i in range(b,(b-a),-1):
        temp*=i


    print( temp // math.factorial(a) )
