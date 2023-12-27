from itertools import combinations


word = input()

location = []
temp=[]
answer=[]

for i in range(len(word)):
  if word[i] == '(':
    temp.append(i)
  elif word[i] == ')':
    location.append((temp.pop(),i))


for i in range(1,len(location)+1):
  combi_list = combinations(location,i)

  for combi in (combi_list):
    print(combi)
    copy_word = list(word)
    for elem in (combi):
      copy_word[elem[0]]= ""
      copy_word[elem[1]]= ""
    answer.append((''.join(copy_word)))
    
    

for i in sorted(list(answer)):
  print(i)