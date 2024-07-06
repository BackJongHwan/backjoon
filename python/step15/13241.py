def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a, b = map(int,input().split())
#only a <= b
if(a > b):
    a, b = b, a
print(a * b //gcd(a,b))
