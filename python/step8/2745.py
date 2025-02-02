n, b = input().split()
b = int(b)
a = n[::-1]
sum = 0
for i in range(len(a)):
    if( 'A'<= a[i] <= 'Z'):
        sum += (ord(a[i]) - ord('A') + 10) * (b ** i)
    else:
        sum += (ord(a[i]) -ord('0')) * (b**i)
print(sum)