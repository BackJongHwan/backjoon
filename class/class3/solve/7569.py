import sys
from collections import deque
input = sys.stdin.readline
num_col, num_row, h = map(int ,input().split())
box = [[] for _ in range(h)]
for i in range(h):
    for _ in range(num_row):
        box[i].append(list(map(int ,input().split())))
num_tomato = 0
tomato_queue = deque([])
''' using visited
visited = [[] for _ in range(h)] 
for i in range(h):
    for _ in range(num_row):
        visited[i].append([0] * num_col)
for height in range(h):
    for row in range(num_row):
        for col in range(num_col):
            if(box[height][row][col] == 0):
                num_tomato += 1
            elif(box[height][row][col] == 1):
                tomato_queue.append((height, row, col, 0))
                visited[height][row][col] = 1
if(num_tomato == 0):
    print(0)
else:
    result = 0
    while tomato_queue:
        # print(num_tomato)
        height, row, col, day = tomato_queue.popleft()
        result = day
        if(box[height][row][col] == 0):
            num_tomato -= 1
            if(num_tomato == 0):
                break
        for dh, drow, dcol in ([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0 , 1), (0, 0, -1)]):
            if(0<=height + dh < h and 0<= row + drow < num_row and 0<= col + dcol < num_col):
                if(box[height + dh][row + drow][col + dcol] == 0):
                    if(visited[height + dh][row + drow][col + dcol] == 0):
                        visited[height + dh][row + drow][col + dcol] = 1
                        tomato_queue.append((height + dh, row + drow, col + dcol, day + 1))
    if(num_tomato == 0):
        print(result)
    else:
        print(-1)
'''
#not using visited
