#dp-(bottom up)
'''
test = int(input())
result = [1, 1, 1]
for i in range(3, 101):
    result.append(result[i -3] + result[i -2])
for _ in range(test):
    n = int(input())
    print(result[n-1])
'''
#dp - top down
def dp(n, result):
    if(n <= 3):
        return 1
    if(result[n] != -1):
        return result[n]

    result[n] = dp(n-3, result) + dp(n-2, result)

    return result[n]
test = int(input())

result = [-1] * 101
for _ in range(test):
    n = int(input())
    ans = dp(n, result)
    print(ans)