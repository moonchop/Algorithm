n=int(input())

d = 300001 * [0]

# i를 2로 나눠서 1이 되는 최소 연산값
for i in range(2,n+1):
  d[i] = d[i-1]+1
  if i%5==0:
    d[i] = min(d[i],d[i//5]+1)
  if i%3==0:
    d[i] = min(d[i],d[i//3]+1)
  if i%2==0:
    d[i] = min(d[i],d[i//2]+1)

print(d[n])

