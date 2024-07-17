

def recursion(row, col):
    if(row == 0 and col == 0):
        return 0
    elif(row == 0 and col == 1):
        return 1
    elif(row == 1 and col == 0):
        return 2
    elif(row == 1 and col == 1):
        return 3
    row_k = 1 
    col_k = 1 
    while (2 * row_k) <= row :
        row_k *= 2 
    while (2 * col_k) <= col:
        col_k *= 2 
    # print(row_k, col_k)
    if(row_k == col_k):
        return (row_k ** 2) * 3 + recursion(row - row_k, col - col_k)
    elif(row_k > col_k):
        return (row_k ** 2) * 2 + recursion(row - row_k, col)
    else:
        return (col_k ** 2) + recursion(row, col - col_k)
n, row, col = map(int,input().split())
result = recursion(row, col)
print(result)