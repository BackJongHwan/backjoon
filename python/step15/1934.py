#O(n)

#using method
'''
import math
test = int(input())
for _ in range(test):
    a, b = map(int,input().split())
    print(math.lcm(a,b))
'''

def gcd(a, b):
    while b != 0:
        a, b = b , a % b
    return a
test = int(input())
for _ in range(test):
    a, b = map(int,input().split())
    print(a * b //gcd(a, b))