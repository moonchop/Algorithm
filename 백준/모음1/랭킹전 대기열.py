import sys

input = sys.stdin.readline

p, m = map(int,input().split())
room_arr = []

a,b = input().rstrip().split()
room_arr.append([(int(a),b)])

for _ in range(p-1):
  level, name = input().rstrip().split()
  for room in room_arr:
    if len(room) < m and abs(room[0][0]-int(level)) < 11:
      room.append((int(level),name))
      break
  else:
    room_arr.append([(int(level),name)])

for room in room_arr:
  print('Started!') if len(room) == m else print('Waiting!')
  for player in sorted(room,key=lambda x:x[1]):
    print(f'{player[0]} {player[1]}')
  

# # input
# 3 2
# 15 a
# 3 b
# 1 c

# # answer
# Waiting!
# 15 a
# Started!
# 3 b
# 1 c