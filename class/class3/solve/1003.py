# n = 40
test = int(input())
result = []
result.append((1, 0))
result.append((0, 1))
for i in range(2, 41):
    result.append((result[i - 2][0] + result[i - 1][0], result[i-2][1] + result[i-1][1]))
for _ in range(test):
    n = int(input())
    print(result[n][0], result[n][1])