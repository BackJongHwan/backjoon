# R, C <= 50, T <= 100=10^3
# O(T) * O(diffunsion + wind)
# O(diffunsion), O(wind) -> 10^5 이하 여야함
# queue는 좀 느림


import sys
from queue import Queue
input =sys.stdin.readline

# 입력받기
r, c, t = map(int , input().split())
board = []
for _ in range(r):
    temp = list(map(int ,input().split()))
    board.append(temp)

# 공기 청정기 위치 찾기
clean = 0
for i in range(r):
    if(board[i][0] == -1):
        clean = i
        break
# print(clean)
# 확산
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
def diffusion():
    '''
    temp = [[0] * c for _ in range(r)]
    q = Queue()
    for i in range(r):
        for j in range(c):
            if(board[i][j] > 0):
                q.put((i, j))
    while not q.empty():
        row, col = q.get()
        for d_row, d_col in directions:
            n_row = row + d_row
            n_col = col + d_col
            if 0<= n_row < r and 0<= n_col < c:
                if board[n_row][n_col] != -1:
                    temp[n_row][n_col] += (board[row][col] // 5)
                    temp[row][col] -= (board[row][col] // 5)
    for i in range(r):
        for j in range(c):
            board[i][j] += temp[i][j]
    '''
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                spread_amount = board[i][j] // 5
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < r and 0 <= nc < c and board[nr][nc] != -1:
                        temp[nr][nc] += spread_amount
                        temp[i][j] -= spread_amount
    for i in range(r):
        for j in range(c):
            board[i][j] += temp[i][j]

# 바람 불고나서
def wind():
    # 공기청정기로 들어오는 방향
    for k in range(clean-1, 0, -1):
        board[k][0] = board[k-1][0]
    for k in range(clean+2, r-1):
        board[k][0] = board[k+1][0]
    # 위 아래 벽 타고 오는 방향
    for k in range(c-1):
        board[0][k] = board[0][k+1]
        board[r-1][k] = board[r-1][k+1]
    # 오른쪽 벽 타는 방향
    for k in range(clean):
        board[k][c-1] = board[k+1][c-1]
    for k in range(r-1, clean+1, -1):
        board[k][c-1] = board[k-1][c-1]
    # 오른쪽으로 미는 방향
    for k in range(c-1, 1, -1):
        board[clean][k] = board[clean][k-1]
        board[clean+1][k] = board[clean+1][k-1]
    board[clean][1] = 0
    board[clean+1][1] = 0

def print_board():
    print("print_board")
    for i in range(r):
        for j in range(c):
            print(board[i][j], end= " ")
        print()

for _ in range(t):
    diffusion()
    # print_board()
    wind()
    # print_board()

# 미세먼지 양 구하기
result = 0
for i in range(r):
    for j in range(c):
        result += board[i][j]
print(result + 2)