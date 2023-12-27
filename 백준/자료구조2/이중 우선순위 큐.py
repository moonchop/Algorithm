import heapq, sys

T = int(sys.stdin.readline())

for _ in range(T):
  K = int(sys.stdin.readline())
  max_heap=[]
  min_heap=[]
  visited = [False] * K
  for i in range(K):
    a,b = sys.stdin.readline().split()
    b=int(b)
    if a == 'I':
      heapq.heappush(min_heap,(b,i))
      heapq.heappush(max_heap,(-b,i))
    else:
      if b==1 and max_heap:
        visited[heapq.heappop(max_heap)[1]] = True
        # max_popped = -heapq.heappop(max_heap)
        # min_heap.remove(max_popped)
      elif b==-1 and min_heap:
        visited[heapq.heappop(min_heap)[1]] = True
        # min_popped = heapq.heappop(min_heap)
        # max_heap.remove(-min_popped)
    while max_heap and visited[max_heap[0][1]] == True:
      heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0][1]] == True:
      heapq.heappop(min_heap)
      
  if max_heap and min_heap:
    print(f'{-heapq.heappop(max_heap)[0]} {heapq.heappop(min_heap)[0]}')
  else:
    print('EMPTY')
