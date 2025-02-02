n = int(input())
temp = 2 
for _ in range(n):
    temp *= 2
    temp -= 1
result = temp **2
print(result)