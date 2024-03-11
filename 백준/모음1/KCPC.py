import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  n,k,t,m = map(int,input().split())
  # 팀수, 문제수, 내팀 id, 로그 수
  count = [0]*(n+1)
  submit_time = [0]*(n+1)
  result = [[0] * (k+1) for _ in range(n+1)]
  for index in range(m):
    i,j,s = map(int,input().split())
    # 팀id, 문제번호, 점수
    result[i][j] = max(result[i][j], s)
    count[i]+=1
    submit_time[i] = index
    
  team_info = []
  # (팀id, 최종점수,제출횟수,마지막 제출시간)
  for i in range(1,n+1):
    team_info.append((i,sum(result[i]),count[i], submit_time[i]))
    
  for i,v in enumerate(sorted(team_info,key=lambda x:(-x[1],x[2],x[3])),start=1):
    if v[0] == t:
      print(i)
    
