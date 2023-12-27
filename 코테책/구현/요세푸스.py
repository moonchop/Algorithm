n, k = map(int,input().split())

result=[]
arr = [i for i in range(1,n+1)]
index=k-1

while len(arr) > 0:
  # if index > len(arr)-1:
  index = index%len(arr)
  result.append(arr.pop(index))
  index+=(k-1)

print("<"+", ".join(str(num) for num in result)+">")
