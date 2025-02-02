# N, M <= 8
# backtracking + BFS? => all right!

import sys
from queue import Queue

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    temp = list(map(int , input().split()))
    matrix.append(temp)
result = []

def backtracking(k, start):
    if(k == 3):
        result.append(bfs(matrix))  # BFS 수행
        return
    for idx in range(start, n * m):
        i, j = divmod(idx, m)  # 1차원 인덱스를 2차원 좌표로 변환
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            backtracking(k + 1, idx + 1)
            matrix[i][j] = 0
def bfs(matrix):
    value = 0
    visited = [[False] * m for _ in range(n)]
    q = Queue()
    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == 2):
                q.put((i, j))
                visited[i][j] = True
    temp = []
    while not q.empty():
        row, col = q.get()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
        for d_row, d_col in directions:
            n_row, n_col = row + d_row, col + d_col
            if 0 <= n_row < n and 0 <= n_col < m:
                if not visited[n_row][n_col] and matrix[n_row][n_col] == 0:
                    visited[n_row][n_col] = True
                    matrix[n_row][n_col] = 2
                    temp.append((n_row, n_col))
                    q.put((n_row, n_col))
    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == 0):
                value += 1
    for row, col in temp:
        matrix[row][col] = 0
    return value
backtracking(0, 0)
print(max(result))