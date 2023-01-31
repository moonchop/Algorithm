import sys

n = str(sys.stdin.readline().rstrip())

if sum(list(map(int,list(n)))[len(n)//2:]) == sum(list(map(int,list(n)))[:len(n)//2]):
    print("LUCKY")
else:
    print("READY")