n,k = map(int,input().split())
coin_list = []
result=0

for _ in range(n):
  coin_list.append(int(input()))
coin_list.sort(reverse=True)

for coin in coin_list:
  if k < coin:
    continue
  result+=(k//coin)
  k%=coin
  
print(result)