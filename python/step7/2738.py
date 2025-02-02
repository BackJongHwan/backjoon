m, n = map(int, input().split())
a = []
b=[]
for i in range(m):
    new_list = list(map(int, input().split()))
    a.append(new_list)
for i in range(m):
    new_list = list(map(int, input().split()))
    b.append(new_list)
result = []
for i in range(m):
    result.append([])
    for j in range(n):
        result[i].append([])
        result[i][j] = a[i][j] + b[i][j]
for i in range(m):
    for j in range(n):
        print(result[i][j], end = " ")
    print()