import sys

a, b = map(int, sys.stdin.readline().split())

if a == b:
    print('same')
elif a > b:
    print('A')
else:
    print('B')
