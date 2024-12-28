n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
print(matrix)