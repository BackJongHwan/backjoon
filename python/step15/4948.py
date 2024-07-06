import sys
input = sys.stdin.readline
#using check
arr = [1] * ((123456 * 2) + 1)
arr[1] = 0
for idx in range(2, len(arr)):
    if((arr[idx]) == 1):
        k = idx
        j = 2 
        while k * j < len(arr):
            arr[k * j] = 0
            j += 1



while True:
    n = int(input())
    if(n == 0):
        break
    result = 0
    for i in range(n + 1, (2 * n) + 1):
        if(arr[i] == 1):
            result+=1
    print(result)