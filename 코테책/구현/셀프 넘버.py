num_list = [0]*10001

def construct(n):
  total = int(n) + sum(list(map(int,n)))
  if total <= 10000:
    num_list[total]=1

for i in range(1,10001):
  construct(str(i))
  
for i in range(1,10001):
  if num_list[i]==0:
    print(i)

