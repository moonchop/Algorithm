import sys

input = sys.stdin.readline

N = int(input())

w_arr= [int(input()) for _ in range(N)] 
w_arr.sort(reverse=True)
w_max = 0
temp=[]

for i in w_arr:
  temp.append(i)
  w_max = max(w_max,i * len(temp))
print(w_max)