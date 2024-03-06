import sys

input = sys.stdin.readline

N = input().rstrip()
arr = list(N)
count = 0
arr_i = 0

while True:
    count+=1
    for i in (str(count)):
        if i == arr[arr_i]:
            arr_i+=1
            if arr_i == len(arr):
                print(count)
                exit()