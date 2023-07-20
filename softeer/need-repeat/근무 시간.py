from datetime import datetime
import sys

total_sec = 0
for _ in range(5):
    a, b = map(str, sys.stdin.readline().split())
    total_sec += (datetime.strptime(b, "%H:%M") -
                  datetime.strptime(a, "%H:%M")).total_seconds()

print(int(total_sec/60))
