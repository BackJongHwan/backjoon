def is_prime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    if(n == 1):
        return False
    return True 

test = int(input())
sum = 0
arr = list(map(int, input().split()))
for n in arr:
    if(is_prime(n)):
        sum +=1
print(sum)

