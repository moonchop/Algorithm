import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    array.append(sum(list(map(int, sys.stdin.readline().split()))))

for i in range(n):
    print(f"Case #{i+1}: {array[i]}")
