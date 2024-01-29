import sys

input = sys.stdin.readline

A, B = map(int,input().split())
answer = 1

while True:
    if B == A:
        break
    elif B < A:
        answer = -1
        break
    
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        answer = -1
        break
    answer += 1
    
print(answer)