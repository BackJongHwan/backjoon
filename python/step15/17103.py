# test = 10^2 체를 이용함
# n = 10^6 --> O(n)
arr = [1] * ((10 ** 6) + 1)
arr[1] = 0
for i in range(2, len(arr)):
    if(arr[i] == 1):
        k = i
        j = 2
        while (k * j) < len(arr):
            arr[k * j] = 0
            j += 1
test = int(input())
for _ in range(test):
    n = int(input())
    result = 0
    for i in range(1, (n // 2 + 1)):
        if(arr[i] == 1 and arr[n - i] == 1):
            result += 1
    print(result)
