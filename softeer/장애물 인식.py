import sys

n = int(sys.stdin.readline())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

answers = []
count = 0


def dfs(x, y):
    global count
    if x >= n or y >= n or x < 0 or y < 0:
        return 0

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x-1, y)
        return count
    return 0


for i in range(n):
    for j in range(n):
        result = dfs(i, j)
        if result != 0:
            answers.append(result)
            count = 0
print(len(answers))
answers.sort()
for i in answers:
    print(i)
