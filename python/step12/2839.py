n = int(input())
min_value = 0
succ = 0
for i in range(0, (n // 5) + 1):
    result = 0
    result += i
    temp = n - i * 5
    if(temp % 3 == 0):
        result += temp // 3
        min_value = result
        succ += 1
if(succ == 0):
    print(-1)
else:
    print(min_value)