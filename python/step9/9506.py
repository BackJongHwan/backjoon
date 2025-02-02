def perfect(n):
    result = []
    for i in range(1, n):
        if(n % i == 0):
            result.append(i)
    sum = 0
    for i in result:
        sum += i
    if(sum != n):
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} = ", end = "")
        for i in result[0:len(result) - 1]:
            print(f"{i} + ",end="")
        print(result[-1], end="")
        print()

while True:
    n = int(input())
    if(n == -1):
        break
    else:
        perfect(n)

