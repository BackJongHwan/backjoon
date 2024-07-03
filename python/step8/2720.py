num_case = int(input())
for _ in range(num_case):
    n = int(input())
    result = [0, 0, 0, 0]
    result[0] = n // 25
    n %= 25
    result[1] = n // 10
    n %= 10
    result[2] = n // 5
    n %= 5
    result[3] = n
    for i in range(4):
        print(result[i], end = " ")
    print()