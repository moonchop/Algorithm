import sys

input = sys.stdin.readline

N = int(input())
color_list = list(input().rstrip())

stack = []

def color_check(color_target):
    answer = 1
    for color in color_list:
        if color==color_target:
            if not stack:
                answer += 1
                stack.append(color_target)
        else:
            stack=[]
    return answer

# if color_list[0]=='B':
#     for color in color_list:
#         if color=='R':
#             if not stack:
#                 answer += 1
#                 stack.append('R')
#         else:
#             stack=[]

#     print(answer)
    
# else:
#     for color in color_list:
#         if color=='B':
#             if not stack:
#                 answer += 1
#                 stack.append('B')
#         else:
#             stack=[]

if color_list[0]=='B':
    print(color_check('R'))
else:
    print(color_check('B'))