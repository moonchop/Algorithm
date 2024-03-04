import sys

input = sys.stdin.readline

N, X = map(int,input().split())
visitor = list(map(int,input().split()))

count = 1
temp = sum(visitor[:X])
max_val = temp

if max(visitor) == 0:
    print("SAD")
else:
    for i in range(N-X):
        temp += visitor[X+i]
        temp -= visitor[i]

        if max_val < temp:
            count = 1
            max_val = temp
        elif max_val == temp:
            count += 1
    print(max_val)
    print(count)
