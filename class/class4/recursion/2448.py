n = int(input())
'''

총 개수 -> 2 * i
1 -> 1
2 -> 3
3 -> 5

minimal tree -> 1, 3, 5
  *
 * *
*****
마지막 줄 크기 -> 2 * n - 1
'''
board = [[' '] * (2 * n-1) for _ in range(n)]

def recursive(row, col, size):
    if(size == 3):
        board[row][col] ='*'
        board[row+1][col-1] = '*'
        board[row+1][col + 1] = '*'
        for k in range(5):
            board[row+2][col - 2 + k] = '*'
        return
    # print(row, col)
    board[row][col] = '*'
    recursive(row, col, size // 2)
    recursive(row + size // 2, col - size //2, size//2)
    recursive(row + size // 2, col + size//2, size//2)

recursive(0,n-1, n)
# print tree
for i in range(n):
    for j in range(2*n-1):
        if(board[i][j]=='*'):
            print('*', end='')
        else:
            print(' ', end='')
    print()
