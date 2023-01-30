import sys

n = (sys.stdin.readline().rstrip())
n_arr=[]
result=0
for char in n:

    n_int = int(char)
    
    if result == 0:
        result+=n_int
        continue
    
    if n_int == 0 or n_int == 1:
        result+=n_int
    else:
        result*=n_int
        
        
print(result)
