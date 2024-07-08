n = int(input())
tshirt_list = list(map(int,input().split()))
t, p = map(int, input().split())
max_tshirt = 0
for num in tshirt_list:
    if(num % t == 0):
        max_tshirt += num // t 
    else:
        max_tshirt += num // t + 1
print(max_tshirt)
print(n // p, n % p)