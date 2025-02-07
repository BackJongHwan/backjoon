# 스도쿠 -> backtracking인가?
import sys
input = sys.stdin.readline
# 9x9 보드를 0으로 초기화
board = [[0] * 9 for _ in range(9)]
# 각 칸마다 개별적인 {1~9} 집합을 가지도록 설정
element_set = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)] for _ in range(9)]

fixed = [[False] * 9  for _ in range(9)]
result = 0
for i in range(9):
    str = input().strip()
    for j in range(9):
        board[i][j] = int(str[j])
        if board[i][j] != 0:
            fixed[i][j] = True
            result += 1
# print(board)
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            element_set[i][j].clear()
            element_set[i][j].add(board[i][j])
            # 같은 row에 해당하는 것들
            for col in range(9):
                if col != j: 
                    element_set[i][col].discard(board[i][j])
            # 같은 col에 해당하는 것들
            for row in range(9):
                if row != i:
                    element_set[row][j].discard(board[i][j])
            # 같은 box에 해당하는 것들
            temp_row = (i // 3) * 3
            temp_col = (j // 3) * 3
            for row in range(temp_row, temp_row + 3):
                for col in range(temp_col, temp_col + 3):
                    if row != i and col != j:
                        element_set[row][col].discard(board[i][j])
# print(element_set)
def backtracking():
    global result
    if(result == 81):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            print()
        return True
        # 빈 칸 찾기
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in element_set[i][j]:  # 가능한 숫자 탐색
                    if is_valid(i, j, num):  # 유효한 숫자인지 확인
                        board[i][j] = num
                        result += 1

                        if backtracking():
                            return True  # 성공하면 즉시 종료

                        # 되돌리기 (백트래킹)
                        board[i][j] = 0
                        result -= 1
                return False  # 가능한 숫자가 없으면 되돌아가기
    return False
# 스도쿠 숫자가 유효한지 검사하는 함수
def is_valid(x, y, num):
    for i in range(9):
        if board[x][i] == num or board[i][y] == num:
            return False

    temp_row = (x // 3) * 3
    temp_col = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[temp_row + i][temp_col + j] == num:
                return False
    return True
# 스도쿠 해결 시작
backtracking()
