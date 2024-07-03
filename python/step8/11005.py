n, b = map(int, input().split())
sum = []
temp = 0
while n > 0:
    temp = n % b
    n = n // b
    if( 9 < temp):
        temp2 = chr(temp - 10 + ord('A'))
        sum.append(temp2)
    else:
        sum.append(str(temp))
sum = sum[::-1]
print("".join(sum))
