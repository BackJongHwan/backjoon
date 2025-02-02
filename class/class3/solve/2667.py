import sys
input = sys.stdin.readline
def dfs(board, visited, row, col):
    if(board[row][col] == 1 and visited[row][col] == 0):
        visited[row][col] = 1
        result =1 
        for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
            if(0<= row + dx < n and 0<= col + dy < n and board[row + dx][col + dy] == 1):
                result += dfs(board,visited, row + dx, col + dy)
        return result 
    else:
        return 0

n = int(input())
visited = [[0] * n for _ in range(n)]
board = []
for _ in range(n):
    input_str = input().strip()
    board.append([int(char) for char in input_str])
count = 0
apart_list = []
for row in range(n):
    for col in range(n):
        if(board[row][col] == 1 and visited[row][col] == 0):
            count += 1
            apart_list.append(dfs(board, visited, row, col))
apart_list.sort()
print(count)
for i in range(len(apart_list)):
    print(apart_list[i])

