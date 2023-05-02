import sys

n = str(sys.stdin.readline().rstrip())

word = list(n)

result = ''.join(sorted(word,reverse=True))

print(result)