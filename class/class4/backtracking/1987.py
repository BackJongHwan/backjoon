# backtracking을 이용하는 거 같네요

import sys
input = sys.stdin.readline

def idx_get(char):
    return ord(char) - ord('A')

def backtracking(row, col, visited, cost):
    check = False
    if row > 0:
        if not visited[idx_get(matrix[row-1][col])]:
            visited[idx_get(matrix[row-1][col])] = True
            check = True
            backtracking(row-1, col, visited, cost + 1)
            visited[idx_get(matrix[row-1][col])] = False
    if col > 0:
        if not visited[idx_get(matrix[row][col-1])]:
            visited[idx_get(matrix[row][col-1])] = True
            check = True
            backtracking(row, col-1, visited, cost + 1)
            visited[idx_get(matrix[row][col-1])] = False
    if row < r-1:
        if not visited[idx_get(matrix[row + 1][col])]:
            visited[idx_get(matrix[row + 1][col])] = True
            check = True
            backtracking(row + 1, col, visited, cost + 1)
            visited[idx_get(matrix[row + 1][col])] = False
    if col < c - 1:
        if not visited[idx_get(matrix[row][col+1])]:
            visited[idx_get(matrix[row][col+1])] = True
            check = True
            backtracking(row, col+1, visited, cost + 1)
            visited[idx_get(matrix[row][col+1])] = False
    if not check:
        result.append(cost)
        return
r, c = map(int, input().split())
matrix = []
for _ in range(r):
    data = list(input().strip())
    matrix.append(data)
    
visited = [False] * 26
result = []
visited[idx_get(matrix[0][0])] = True
backtracking(0, 0, visited, 1)
print(max(result))