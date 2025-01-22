import sys
from queue import Queue
input = sys.stdin.readline

n = int(input())
board = []
shark = {'size': 2, 'eat': 0, 'x': 0, 'y': 0}
for _ in range(n):
    board.append(list(map(int,input().split())))

# size별로 fish의 위치를 저장함..
for i in range(n):
    for j in range(n):
        if(board[i][j] == 9):
            shark['x'] = i
            shark['y'] = j
# 먹을 fish가 있을 때 까지 반복
result = 0
fish = True
dest = [(0,1), (-1, 0), (1, 0), (0, -1)]
while fish:
    second = 0
    q = Queue()
    visited = [[False] * n for _ in range(n)]
    # shark의 size 조정
    if(shark['size'] == shark['eat']):
        shark['size'] += 1
        shark['eat'] = 0
    q.append((shark['x'], shark['y'], second))
    # 먹이를 찾을 때 까지 반복
    while not q.empty():
        x, y, sec = q.pop()
        visited[x][y] = True
        # 먹이를 찾았을 때
        if board[x][y] != 9 and board[x][y] < shark['size']:
            shark['eat'] += 1
            board[x][y] = 0
            shark['x'] = x
            shark['y'] = y
            result += sec
        # 이제 큐에 추가할 것 
        else:
            for dx, dy in dest:
                nx = dx + x
                ny = dy + y 
                if()

    fish = False
print(result)