import sys
from collections import deque
input = sys.stdin.readline

num_col, num_row = map(int, input().split())
graph = [list(map(int , input().split())) for _ in range(num_row)]
queue = deque()
for row in range(num_row):
    for col in range(num_col):
        if(graph[row][col] == 1):
            queue.append((row, col))
while queue:
    row, col = queue.popleft()
    for dx, dy in [(1, 0), (-1,0), (0, 1), (0, -1)]:
        if 0<=row + dx < num_row and 0<= col + dy < num_col:
            if(graph[row + dx][col + dy] == 0):
                graph[row + dx][col + dy] = graph[row][col] + 1
                queue.append((row + dx, col + dy))
tomato = True 
day = 0
for row in range(num_row):
    for col in range(num_col):
        if(graph[row][col] == 0):
            tomato = False
            break
        day = max(day, graph[row][col])
    if tomato == False:
        break
if(tomato == False):
    print(-1)
else:
    print(day - 1)