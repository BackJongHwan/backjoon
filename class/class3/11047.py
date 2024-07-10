# n = 10 k = 10^8
#A = 10^6
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = []
for _ in range(n):
    a = int(input())
    if(a <= k):
        coin_list.append(a)
result = 0
for coin in range(len(coin_list) - 1, -1, -1):
    num = k // coin_list[coin]
    k -= num * coin_list[coin]
    result += num
    if(k == 0):
        break
print(result)