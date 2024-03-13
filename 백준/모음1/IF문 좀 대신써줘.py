import sys

input = sys.stdin.readline

word = list(input().rstrip())
count_0 = word.count('0') // 2
count_1 = word.count('1') // 2

result = ''


for i in range(len(word)):
    if count_1 == 0: break
    if word[i] == '1':
        count_1 -= 1
        word[i]='2'

for i in range(len(word)-1, -1, -1):
    if count_0 == 0: break
    if word[i] == '0':
        count_0 -= 1
        word[i]='2'

print(''.join(''.join(word).split('2')))


# word = word[::-1]       
# for i in range(len(word)):
#     if count_0 == 0: break
#     if word[i] == '0':
#         count_0 -= 1
#         word.pop(i)
    
# print(''.join(word[::-1]))