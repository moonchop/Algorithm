import sys

n = int(sys.stdin.readline())
words=[]


for _ in range(n):
  words.append(sys.stdin.readline().rstrip())
words = list(set(words))


words.sort(key=len)
e = sorted(words,key=lambda x:[len(x),x])

for word in e:
  print(word)