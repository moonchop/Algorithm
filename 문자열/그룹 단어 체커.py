import sys

n = int(sys.stdin.readline())
words = []
dupe ={}
for _ in range(n):
  words.append(sys.stdin.readline().rstrip())

def isWordCheck(word): 
  dupe={}
  dupe[word[0]]=1
  for i in range(1,len(word)):
    
    if word[i] == word[i-1]:
      if word[i] not in dupe:
        dupe[word[i]] = 1
        
    else:
      if word[i] in dupe:
        return False
      else:
        dupe[word[i]] = 1
  return True

result=0
for word in words:
  if isWordCheck(word) == True:
    result+=1
  
print(result)

# 1. n과 n-1이 같을 때:
#   배열에 문자 추가, 있으면 추가 안함.
# 2. n과 n-1이 같지 않을떄:
#   배열에 알파벳이 있으면 바로 return False
#   없으면 추가한다.