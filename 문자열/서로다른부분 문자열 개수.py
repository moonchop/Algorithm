import sys

word = sys.stdin.readline().rstrip()

result=[]
for i in range(1,len(word)+1):
  for j in range((len(word)+1)-i):
    result.append(word[j:(j+i)])
    
print(len(list(set(result))))