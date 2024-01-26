import sys

input = sys.stdin.readline

N = int(input())
color_list = list(input().rstrip())

answer = 1
stack = []

if not 'R' in color_list or not 'B' in color_list:
    answer = 1

else:
    for color in color_list:
        if color=='R':
            if not stack:
                answer += 1
                stack.append('R')
        else:
            stack=[]

if color_list[0] == 'R':
    
    print(answer-1)

else:
    print(answer)


# RRBRRBBBRR