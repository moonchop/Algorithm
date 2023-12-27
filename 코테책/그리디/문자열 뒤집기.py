import sys

n = (sys.stdin.readline().rstrip())
count1=0
count2=0
prev=9
for i in range(0,len(n)):
    num = int(n[i])
    if num==0:
        if prev != num:
            count1+=1
    else:
        if prev != num:
            count2+=1
    prev=num
    
print(min(count1,count2))
