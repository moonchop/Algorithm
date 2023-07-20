import sys

w, n = map(int, sys.stdin.readline().split())

store_arr = []
curr_sum = 0
result = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    store_arr.append((a, b))

store_arr.sort(key=lambda x: x[1], reverse=True)

for i in store_arr:
    if w <= curr_sum + i[0]:
        result += (w-curr_sum)*i[1]
        break
    else:
        curr_sum += i[0]
        result += i[0]*i[1]

print(result)
