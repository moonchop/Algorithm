
N, M = map(int,input().split())

pockemons_alpha = {}
pockemons_num = {}
to_finds = [] 
answer = []

for i in range(1,N+1):
  input_ = input()
  pockemons_num[str(i)] = input_
  pockemons_alpha[input_] = i
for i in range(M):
  find = input()
  if find.isalpha():
    answer.append(pockemons_alpha[find])
  else:
    answer.append(pockemons_num[find])

    
for i in answer:
  print(i)
  
  
  
