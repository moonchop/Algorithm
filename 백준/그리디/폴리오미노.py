import sys

input = sys.stdin.readline

word = input().rstrip()
count=0
answer=''

# for i in word:
#   if i == 'X':
#     count+=1
#   elif i == '.':
#     if count == 2:
#       answer+='BB'
#       count = 0
#     elif count == 1 or count > 2:
#       answer=-1
#       break
#     answer+='.'
  
#   if count==4:
#     answer+='AAAA'
#     count=0
  

# if count == 2:
#   answer+='BB'
# elif count == 1 or count > 2:
#   answer=-1

# print(answer)


# 개선

word = word.replace('XXXX','AAAA')
word = word.replace('XX','BB')
print(-1) if 'X' in word else print(word)