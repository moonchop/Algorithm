import sys

word = sys.stdin.readline().rstrip()
word = list(word)
word.sort()
for i in range(len(word)):
    if word[i].isalpha():
        result = "".join(word[i:]) + str(sum(list(map(int,word[:i]))))
        break
    
print((result))
