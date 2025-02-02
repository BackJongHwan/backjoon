mat = []
for _ in range(100):
    mat.append([0] * 100)
num_paper = int(input())
for _ in range(num_paper):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            mat[i][j] = 1
num = 0
for i in range(100):
    for j in range(100):
        if(mat[i][j] == 1):
            num+=1
print(num)

