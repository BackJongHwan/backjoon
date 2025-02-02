t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    count = 1
    temp = x - 1
    x -= temp
    y -= temp
    count += temp
    while y <= 0:
        y += n
    num = 1 
    year = 0
    check = 1
    while True:
        if(num == y):
            break
        year += 1
        num += m
        while num > n:
            num -= n
        if num == 1:
            check = 0
            break
    if check == 0:
        print(-1)
    else:
        print(count + year * m)