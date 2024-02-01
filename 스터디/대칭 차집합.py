import sys

input = sys.stdin.readline

a_n, b_n = map(int,input().split())
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))

# print(len(list(a-b)) + len(list(b-a)))
print(len(a^b))