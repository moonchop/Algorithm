import sys

n=int(sys.stdin.readline())

n=1000-n
result=0
change_list=[500,100,50,10,5,1]
# while n > 0:
#   if n >=500:
#     n-=500
#   elif n >=100:
#     n-=100
#   elif n >=50:
#     n-=50
#   elif n >=10:
#     n-=10
#   elif n >=5:
#     n-=5
#   elif n >=1:
#     n-=1
#   result+=1
# print(result)

for i in change_list:
  result+= (n//i)
  n%=i
print(result)