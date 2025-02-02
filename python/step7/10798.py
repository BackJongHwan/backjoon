import sys
mat = []
max_len = 0
for i in range(5):
    mat.append(list(sys.stdin.readline().rstrip()))
    if(max_len < len(mat[i])):
        max_len = len(mat[i])
for i in range(max_len):
    for j in range(5):
        try:
            print(mat[j][i], end="")
        except IndexError:
            continue
print()