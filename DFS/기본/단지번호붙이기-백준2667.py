import sys

n = int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

count=0
count_array=[]
def dfs(x,y):
    global count
    if x < 0 or x >=n or y < 0 or y>=n:
        return False
    if graph[x][y]==1:
        count+=1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

results=0

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            results+=1
            count_array.append(count)
            count=0
print(results)
count_array.sort()
for i in count_array:
    print(i)