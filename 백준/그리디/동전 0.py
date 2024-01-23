import sys

input = sys.stdin.readline

N,K = map(int,input().split())
coin_arr = [int(input()) for _ in range(N)]
coin_arr.sort(reverse=True)

answer = 0

for coin in coin_arr:
    answer += (K//coin)
    K %= coin
    
print(answer)