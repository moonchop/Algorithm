import re
alphabet_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word=input()

result=0

for alphabet in alphabet_list:
    result+=len(re.findall(alphabet,word))
    word=word.replace(alphabet,' ')

print(result+len(''.join(word.split(' '))))