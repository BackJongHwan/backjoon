import sys
from collections import deque
input = sys.stdin.readline

def bfs(board, n, m):
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    step = 1
    bfs_queue = deque([(0, 0, 1)])
    result = 0
    while bfs_queue:
        row, col, step = bfs_queue.popleft()
        if(row == n - 1 and col == m - 1):
            result = step
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if(0<= row + dx < n and 0<= col + dy < m and board[row + dx][col + dy] == 1):
                if(visited[row +dx][col + dy] == 0):
                    visited[row +dx][col + dy] = 1
                    bfs_queue.append((row + dx, col + dy, step + 1))
    return result
n, m = map(int ,input().split())
board = []
for _ in range(n):
    input_str = input().strip()
    num_list = [int(char) for char in input_str] 
    board.append(num_list)
count = bfs(board, n, m)
print(count)