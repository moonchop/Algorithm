import sys
n,m = map(int,sys.stdin.readline().split())

n_arr = []
m_arr = []

for _ in range(n):
  n_arr.append(sys.stdin.readline().rstrip())
for _ in range(m):
  m_arr.append(sys.stdin.readline().rstrip())

result_arr=list(set(n_arr)&set(m_arr))
result_arr.sort()

print(len(result_arr))
for name in result_arr:
  print(name)
