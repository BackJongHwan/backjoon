#n = 1000, m = 1000 -> O(n^2)일듯?
import sys
from collections import deque
input = sys.stdin.readline

def bfs(board, visited, result, target_row, target_col):
    bfs_queue = deque([(target_row, target_col, 0)])
    while bfs_queue:
        row, col, step = bfs_queue.popleft()
        result[row][col] = step
        for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
            if(0<= row + dx < n and 0 <= col + dy < m):
                if(board[row + dx][col + dy] == 1 and visited[row + dx][col + dy] == 0):
                    visited[row+dx][col + dy] = 1
                    bfs_queue.append((row + dx, col+dy, step + 1))

n, m = map(int, input().split())
board = []
visted = [[0] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]
for _ in range(n):
    board.append(list(map(int, input().split())))

target_row, target_col = 0, 0
for row in range(n):
    check = 0
    for col in range(m):
        if(board[row][col] == 2):
            target_row, target_col = row, col
            # visted[target_row][target_col] = 1
            result[target_row][target_col] = 0
            check = 1
            break
    if check == 1:
        break
bfs(board, visted, result, target_row, target_col)
for row in range(n):
    for col in range(m):
        if(board[row][col] == 1 and result[row][col] == 0):
            result[row][col] = -1
for i in range(n):
    print(" ".join(map(str, result[i])))