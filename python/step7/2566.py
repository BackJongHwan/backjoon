matrix = []
for _ in range(9):
    matrix.append(list(map(int, input().split())))
max = 0
a, b = 0, 0
for i in range(9):
    for j in range(9):
        if(max <= matrix[i][j]):
            max = matrix[i][j]
            a, b = i + 1, j + 1
print(max)
print(a, b)