#adjcent한게 명시적으로 들어나 있으므로 굳이 adj_matrix, adj_list가 필요없음!

import sys
sys.setrecursionlimit(10 ** 6)  # Increase recursion limit if necessary
input = sys.stdin.readline
num_row, num_col = map(int, input().split())

def dfs(campus, visited, row, col):
    if 0<= row < num_row and 0<= col < num_col:
        if campus[row][col] != 'X' and not visited[row][col]:
            visited[row][col] = 1
            dfs(campus, visited, row + 1, col)
            dfs(campus, visited, row - 1, col)
            dfs(campus, visited, row , col + 1)
            dfs(campus, visited, row, col - 1)

campus = []
visited = [[0] * num_col for i in range(num_row)]
for _ in range(num_row):
    campus.append(list(input()))
pos = (0, 0)
p_list = []
for row in range(num_row):
    for col in range(num_col):
        if(campus[row][col] == 'X'):
            continue
        if(campus[row][col] == 'I'):
            pos = (row, col)
        elif(campus[row][col] == 'P'):
            p_list.append((row, col))
dfs(campus, visited, pos[0],pos[1] )
num = 0
for (row, col) in p_list:
    if visited[row][col] == 1:
        num+=1
if num == 0:
    print("TT")
else:
    print(num)