import sys

coordi = sys.stdin.readline().rstrip()
x = ord(coordi[:1])-96
y = int(coordi[1:])

arr = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]
count=0
for i in arr:
  nx= x+i[0]
  ny= y+i[1]
  
  if nx < 1 or ny < 1:
    continue
  count+=1
print(count)
# 1. 경우의 수는 총 8가지
# 2. 1번을 모두 비교하면서 0되면 count안함
# 3. 단, nx,ny로 임시 값을 저장하고, count할지 안할지 결정