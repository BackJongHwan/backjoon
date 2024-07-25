#n = 100 O(N^3)
import sys
from collections import deque
input = sys.stdin.readline
'''
def BFS_normal(graph, visited, n):
    queue = deque()
    check = 0
    result = 0
    while True:
        while queue:
            row, col, color = queue.popleft()
            visited[row][col] = 1
            check += 1
            for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
                if 0<= row + dx < n and 0<= col + dy < n:
                    if  graph[row + dx][col + dy] == color and visited[row + dx][col + dy] == 0 :
                        visited[row +dx][col + dy] = 1
                        queue.append((row + dx, col + dy, color))
        if(check == n * n):
            break
        else:
            result += 1
            insert = 0
            for row in range(n):
                for col in range(n):
                    if(visited[row][col] == 0):
                        queue.append((row, col, graph[row][col]))
                        insert = 1
                        break
                if(insert):
                    break
    return result
def BFS(graph, visited, n):
    queue = deque()
    check = 0
    result = 0
    while True:
        while queue:
            row, col, color = queue.popleft()
            visited[row][col] = 1
            check += 1
            for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
                if 0<= row + dx < n and 0<= col + dy < n:
                    if color == 2:
                        if graph[row + dx][col + dy] == color and visited[row + dx][col + dy] == 0 :
                            visited[row +dx][col + dy] = 1
                            queue.append((row + dx, col + dy, color))
                    else:
                        if graph[row + dx][col + dy] == 0 or graph[row + dx][col + dy] == 1:
                            if visited[row + dx][col + dy] == 0 :
                                visited[row +dx][col + dy] = 1
                                queue.append((row + dx, col + dy, color))
        if(check == n * n):
            break
        else:
            result += 1
            insert = 0
            for row in range(n):
                for col in range(n):
                    if(visited[row][col] == 0):
                        queue.append((row, col, graph[row][col]))
                        insert = 1
                        break
                if(insert):
                    break
    return result
'''
def dfs(row, col):
    visited[row][col] = True
    color = graph[row][col]
    for dx, dy in [(1, 0), (-1,0), (0, 1), (0, -1)]:
        nx, ny = row + dx, col + dy
        if 0<= nx < n and 0<= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == color:
                dfs(nx, ny)
def dfs2(row, col):
    visited[row][col] = True
    color = graph[row][col]
    for dx, dy in [(1, 0), (-1,0), (0, 1), (0, -1)]:
        nx, ny = row + dx, col + dy
        if 0<= nx < n and 0<= ny < n:
            if visited[nx][ny] == False:
                if color == 2:
                    if graph[nx][ny] == color:
                        dfs2(nx, ny)
                else:
                    if graph[nx][ny] != 2:
                        dfs2(nx, ny)
n = int(input())
red = 0
green = 1 
blue = 2
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
for i in range(n):
    str_input = input().rstrip()
    j = 0
    for char in str_input:
        if(char == "R"):
            graph[i][j] = 0
        elif(char == 'B'):
            graph[i][j] = 2
        else:
            graph[i][j] = 1
        j+=1
'''
result1 = BFS_normal(graph, visited1, n)
result2 = BFS(graph, visited2, n)
print(result1, result2)
'''
result1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            result1 += 1
result2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs2(i, j)
            result2 += 1
print(result1, result2)