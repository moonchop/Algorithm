import sys

input = sys.stdin.readline

N, K = map(int,input().split())
arr = list(input().rstrip())
answer = 0

for i,v in enumerate(arr):
    if v == 'H':
        for j in range(1,K+1):
            if i+j < N and arr[i+j] == 'P':
                answer+=1
                arr[i+j] = ''
                arr[i] = ''
                break
                
    elif v == 'P':
        for j in range(1,K+1):
            if i+j < N and arr[i+j] == 'H':
                answer+=1
                arr[i+j] = ''
                arr[i] = ''
                break
print(answer)