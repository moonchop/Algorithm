import sys

input = sys.stdin.readline

N,M  = map(int,input().split())

A_arr = input().split()
B_arr = input().split()

print(*sorted((A_arr+B_arr),key=lambda x:int(x)))
