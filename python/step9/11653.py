n = int(input())
k = 2
if(n != 1):
    while True:
        if(n == 1):
            break
        if(n % k == 0):
            n /= k
            print(k)
        else:
            k += 1

