import sys

input = sys.stdin.readline

word = input().rstrip()

a_count = word.count('a')

word *=2

min_val = sys.maxsize
for i in range(len(word) - (a_count-1)):
    min_val = min(min_val,word[i:i+a_count].count('b'))
print(min_val)