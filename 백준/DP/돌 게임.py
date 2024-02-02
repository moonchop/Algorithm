import sys

input = sys.stdin.readline

N = int(input())

count = 0


count += N//3
N %= 3

count += N

if count % 2 != 0:
    print('SK')
else:
    print('CY')


