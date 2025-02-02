# N, M <= 100 O(N^3) 가능
# 많아야 50초 걸림
# BFS 50번 돌리기
# (0, 0)에서 시작해서 BFS 돌리고 각 block마다 check하고 없애기

import sys
from queue import Queue
input = sys.stdin.readline

n, m = map(int , input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cheese = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cheese += 1
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs():
    q = Queue()
    # if visited is True then this place is external air
    visited = [[False] * m for _ in range(n)]
    q.put((0, 0))
    while not q.empty():
        row, col = q.get()
        for dx, dy in directions:
            d_row = dx + row
            d_col = dy + col
            if 0<= d_row < n and 0<= d_col< m and not visited[d_row][d_col]:
                # 치즈로 막혀있지 않다면
                if board[d_row][d_col] != 1:
                    visited[d_row][d_col] = True
                    q.put((d_row, d_col))
    return visited
# 외부와 접촉한 cheese를 삭제
def remove(board, air, cheese):
    for row in range(n):
        for col in range(m):
            if board[row][col] == 1:
                sum = 0
                for dx, dy in directions:
                    d_row = row + dx
                    d_col = col + dy
                    if air[d_row][d_col]:
                        sum += 1
                if(sum > 1):
                    board[row][col] = 0
                    cheese -= 1
    return board, cheese
result = 0
while(cheese > 0):
    result += 1
    # air는 외부 공기가 있는 곳임
    air = bfs()
    board, cheese = remove(board,air, cheese)
print(result)