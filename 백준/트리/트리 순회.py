import sys

input = sys.stdin.readline

N = int(input())
visited = [False] * (N+1)
graph = {}

for _ in range(N):
  root, left, right = input().split()
  graph[root] = [left,right]




def preorder(root):
  if root != '.':
    print(root,end='')
    preorder(graph[root][0])
    preorder(graph[root][1])

def inorder(root):
  if root != '.':
    inorder(graph[root][0])
    print(root,end='')
    inorder(graph[root][1])

def postorder(root):
  if root != '.':
    postorder(graph[root][0])
    postorder(graph[root][1])
    print(root,end='')



(preorder('A'))
print()
(inorder('A'))
print()
(postorder('A'))