import sys

m, n, k = map(int, sys.stdin.readline().split())

menu_str = list(map(str, sys.stdin.readline().split()))
user_str = list(map(str, sys.stdin.readline().split()))

from_str = ''.join(menu_str)
to_str = ''.join(user_str)

if len(from_str) > len(to_str):
    from_str, to_str = to_str, from_str

print('secret' if from_str in to_str else 'normal')
