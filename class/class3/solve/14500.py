import sys
from collections import deque
input = sys.stdin.readline
def BFS(row, col):
    result = 0
    Q = deque([(row, col, row, col, board[row][col], 0)])
    while Q:
        pre_row, pre_col, row, col, value, pos = Q.popleft()
        if(pos == 3):
            result = max(result,value)
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if(0<= row + dx < n and 0 <= col + dy < m):
                if(row + dx != pre_row or col + dy != pre_col):
                    Q.append((row, col, row + dx, col + dy, value + board[row + dx][col + dy], pos + 1))
    return result
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int ,input().split())))
result2 = 0
for row in range(n):
    for col in range(m):
            result2 = max(result2,BFS(row, col))
#ㅜ shape
for col in range(m-1):
    for row in range(n-2):
        value = board[row][col] + board[row + 1][col] + board[row + 1][col + 1] + board[row + 2][col]
        result2 = max(result2, value)
# ㅗ sahpe
for col in range(1, m):
    for row in range(n-2):
        value = board[row][col] + board[row + 1][col] + board[row + 1][col - 1] + board[row + 2][col]
        result2 = max(result2, value)
# ㅏ shape
for row in range(n-1):
    for col in range(m - 2):
        value = board[row][col] + board[row][col+1] + board[row + 1][col + 1] + board[row][col + 2]
        result2 = max(result2, value)
# ㅓ shape
for row in range(1, n):
    for col in range(m - 2):
        value = board[row][col] + board[row][col+1] + board[row - 1][col + 1] + board[row][col + 2]
        result2 = max(result2, value)
print(result2)