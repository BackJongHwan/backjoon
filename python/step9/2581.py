def is_prime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    if(n == 1):
        return False
    return True 


m = int(input())
n = int(input())
sum = 0
min = 0
for i in range(m, n+1):
    if(is_prime(i)):
        sum += i
        if(min == 0):
            min = i
if(sum == 0):
    print(-1)
else:
    print(sum)
    print(min)