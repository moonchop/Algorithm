import sys
data=[]
N,M = list(map(int,sys.stdin.readline().split()))
for i in range(N):
  data.append(list(map(int,sys.stdin.readline().split())))

min_arr=[]
for raw in data:
  min_arr.append(min(raw))
  
print(max(min_arr))
#데이터가 많아지면 큰 배열이 메모리를 차지한다.
#그래서 변수에 최대값을 항상 최신화 해주는 방향으로 코드 개선함.

#개선 코드
import sys
result=0
N,M = list(map(int,sys.stdin.readline().split()))
for i in range(N):
  data = list(map(int,sys.stdin.readline().split()))
  min_value = min(data)
  result = max(result,min_value)
print(result)



##init
# 1.각 행의 최소값을 배열로 뽑는다
# 2.max를 통해 그 중에 가장 큰 값을 출력한다.
