import sys, copy

input = sys.stdin.readline

N = int(input())
arr=[]
word=''
answer = 0

for _ in range(N):
    arr.append((list(input().rstrip())))
word = arr[0]

for i in range(1,N):
    if abs(len(arr[i])-len(word)) > 1:
        continue
    count=0
    for char in word:
        if char in arr[i]:
            arr[i].remove(char)
        else:
            count+=1
    if len(arr[i]) < 2 and count < 2:
        answer+=1      
print(answer)
# DOLL
# DOG