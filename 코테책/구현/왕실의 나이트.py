import sys

#1
location=str(sys.stdin.readline().rstrip())
location.split(' ')
a,b=location
transfer = {
  "a":"1",
  "b":"2",
  "c":"3",
  "d":"4",
  "e":"5",
  "f":"6",
  "g":"7",
  "h":"8"
}
#2
steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

#3
a=int(transfer[a])
b=int(b)
x,y=a,b
count=0

for step in steps:
  x=a+step[0]
  y=b+step[1]
  if x < 1 or y < 1 or x > 8 or y > 8:
    continue
  print(x,y)
  count+=1
  
print(count)

##repeat
#1.8이상일 때는(최대크기 벗어남) 체크 못했었음

##init
#1.입력을 받았을 때, 좌표로 변환하여 현재 위치 파악
#2.이동할 수 있는 모든 경우의 수를 배열에 담기
#3.배열을 반복문으로 돌면서 1,1을 무조건 넘기는 모든 경우의 수 카운트