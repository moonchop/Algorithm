arr=[3,1,6,2,4,7,10,9]

count = [0]*(max(arr)+1)

for i in range(len(arr)):
  count[arr[i]] += 1
  
for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=' ')