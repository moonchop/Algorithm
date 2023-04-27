import sys

input = sys.stdin.readline()

n,k = map(int,input.split())

arr_A = list(map(int,sys.stdin.readline().split()))
arr_B = list(map(int,sys.stdin.readline().split()))

arr_A.sort()
arr_B.sort(reverse=True)

for i in range(k):
  if arr_A[i] >= arr_B[i]:
    break
  arr_A[i] = arr_B[i]

print(sum(arr_A))