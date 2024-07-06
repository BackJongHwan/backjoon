#O(logn)
import math
def is_prime(n):
    k = math.sqrt(n)
    i = 2 
    while i <= k:
        if(n % i == 0):
            return False
        i +=1
    return True

def find_prime(n):
    k = n
    while (is_prime(k) == False):
        k +=1
    return k 
test = int(input())
for _ in range(test):
    n = int(input())
    if(n <= 2):
        result = 2
    else: 
        result = find_prime(n)
    print(result)
