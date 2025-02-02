# backtracking
'''
import copy
n = int(input())

board = [[0] * n for _ in range(n)]

# print(board)
# can go queen

def check(board, row, col):
    for j in range(n):
        board[row][j] = 1
    for i in range(n):
        board[i][col] = 1
    for i in range(-n, n):
        if 0 <= row + i < n and 0<= col + i  < n:
            board[row + i][col + i] = 1
    for i in range(-n, n):
        if 0 <= row + i < n and 0<= col - i  < n:
            board[row + i][col - i] = 1
    return board

# k means 지금까지 설정한 queen
def backtracking(k, board, row):
    if(k == n):
        # print("wow")
        result.append(1)
        return
    for j in range(n):
        if(board[row][j] == 0):
            temp = copy.deepcopy(board) 
            board[row][j] = 1
            board = check(board, row, j)
            backtracking(k + 1, board, row + 1)
            board = temp
        # if(j == n -1):
        #     return
result = []
# row를 기준으로 backtracking
for i in range(n):
    temp = copy.deepcopy(board) 
    board[0][i] = 1
    board = check(board, 0, i)
    # print(board)
    backtracking(1, board, 1)
    board = temp
    # print(board)
print(len(result))
'''
n = int(input())
def backtracking(row):
    global result
    if row == n:
        result += 1
        return
    for col in range(n):  # 현재 행의 모든 열에 대해 시도
        if col not in cols and (row - col) not in diag_1 and (row + col) not in diag_2:
            # 현재 열, 대각선에 퀸이 없다면 배치 가능
            cols.add(col)
            diag_1.add(row - col)
            diag_2.add(row + col)
            backtracking(row + 1)  # 다음 행으로 이동
            # 백트래킹: 퀸을 다시 제거
            cols.remove(col)
            diag_1.remove(row - col)
            diag_2.remove(row + col)
cols = set() 
diag_1 =set() 
diag_2 =set() 
result = 0
backtracking(0)
print(result)