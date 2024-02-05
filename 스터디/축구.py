import sys,math
input = sys.stdin.readline

a_ = int(input())
b_ = int(input())

a,b = 0,0
arr = [2,3,5,7,11,13,17]
for i in range(7):
    a+= math.comb(18,arr[i]) * ((a_/100)**arr[i] * (1 - (a_/100))**(18-arr[i]))
    b+= math.comb(18,arr[i]) * ((b_/100)**arr[i] * (1 - (b_/100))**(18-arr[i]))
    
print(round((a+b) - a*b,20))


# 2,3,5,7,11,13,17
