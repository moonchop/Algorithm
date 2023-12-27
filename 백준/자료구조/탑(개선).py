num_ = int(input())
nums = list(map(int,input().split(' ')))

answer=[0 for _ in range(num_)]

stack=[]


for i in range(num_):
    while stack:
        if stack[-1][1] > nums[i]:
            answer[i] = stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append((i,nums[i]))
    
for i in answer:
    print(i,end=' ')    