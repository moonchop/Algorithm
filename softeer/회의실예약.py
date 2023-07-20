import sys

n, m = map(int, sys.stdin.readline().split())

meetRooms = {}

for _ in range(n):
    meetRooms[sys.stdin.readline().rstrip()] = [True]*19

for _ in range(m):
    meetRoom, from_time, to_time = map(str, sys.stdin.readline().split())
    for i in range(int(from_time), int(to_time)+1):
        meetRooms[meetRoom][i] = False

available_time = {}


for key in meetRooms.keys():
    a = 0
    b = 0
    for i in range(9, 19):
        if meetRooms[key][i] == True:
            if a == 0:
                if meetRooms[key][i-1] == False:
                    a = i-1
                else:
                    a = i
            else:
                b = i
        elif meetRooms[key][i] == False:
            if a != 0 and b != 0:
                if key not in available_time:
                    available_time[key] = []
                available_time[key].append((a, b))
                a = 0
                b = 0

        if i == 18:
            if meetRooms[key][i] == True:
                if key not in available_time:
                    available_time[key] = []
                available_time[key].append((a, b))

print(available_time)
# dict,[[True]*25]로 초기화한다.
#  for(a,b+1)로 false로 만든다.

# -9를 통해 배열에 저장하고, 반복문을 돈다.
# a,b에 저장하면서 만약 false일때, 길이가 1이라면 전에 시간을 추가한다.
# 길이가 0이라면 아무것도안한다.
# true일 때, 길이가 1이라면 false를 만날때까지 아무것도안하고, 만나면 그 전에꺼를 b에 추가한다.
# 길이가 0이라면 a에 바로 추가한다.
