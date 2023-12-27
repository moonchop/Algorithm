from collections import Counter
N = int(input())
arr=[]
for _ in range(N):
  arr.append(int(input()))

average = round(sum(arr)/N)
asc_arr = sorted(arr)
midian = asc_arr[(N//2)]
mode_arr = [0]*8001
mode_index_arr=[]
mode=0
# mode = Counter(asc_arr).most_common()
# if len(mode) == 1:
#   mode = mode[0][0]
# else:
#   if mode[0][1] == mode[1][1]:
#     mode = mode[1][0]
#   else:
#     mode = mode[0][0]

for i in arr:
  mode_arr[i+4000] +=1
mode_max_value = max(mode_arr)

for i in range(len(mode_arr)):
  if mode_arr[i] == mode_max_value:
    mode_index_arr.append(i-4000)
mode_index_arr.sort()

if len(mode_index_arr) ==1:
  mode = mode_index_arr[0]
else:
  mode = mode_index_arr[1]

range_value = 0
range_value = asc_arr[N-1]-asc_arr[0]

print(average)
print(midian)
print(mode)
print(range_value)