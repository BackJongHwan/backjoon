# 10^6 -> O(n)
import sys

def is_prime(n):
    if(n == 1):
        return False
    k = (n ** 0.5)
    i = 2 
    while i <= k:
        if(n % i == 0):
            return False
        i+=1
    return True
input = sys.stdin.readline
m, n = map(int,input().split())
for i in range(m, n + 1):
    if(is_prime(i)):
        print(i)