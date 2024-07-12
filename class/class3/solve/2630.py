import sys
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    num_list = list(map(int, input().split()))
    board.append(num_list)
#using stack, pop
'''
white = []
blue = []
num_blue = 0
num_white = 0
if(board[0][0] == 1):
    blue.append((0, 0, n))
else:
    white.append((0, 0, n))
while white or blue:
    if  blue:
        x, y, size = blue.pop()
        check = 0
        if(size == 1):
            num_blue += 1
            continue
        for i in range(x, x + size):
            for j in range(y, y + size):
                if(board[i][j] == 0):
                    check = 1
                    break
            if(check == 1):
                break
        if(check == 0):
            num_blue += 1
            continue
        size = size // 2
        for dx, dy in [(0, 0), (size, 0), (0, size), (size, size)]:
            if(board[x + dx][y + dy] == 1):
                blue.append((x + dx, y + dy, size))
            else:
                white.append((x + dx, y + dy, size))
    if  white:
        x, y, size = white.pop()
        if(size == 1):
            num_white += 1
            continue
        check = 0
        for i in range(x, x + size):
            for j in range(y, y + size):
                if(board[i][j] == 1):
                    check = 1
                    break
            if(check == 1):
                break
        if(check == 0):
            # print(x, y, size)
            num_white += 1
            continue
        size = size // 2
        for dx, dy in [(0, 0), (size, 0), (0, size), (size, size)]:
            if(board[x + dx][y + dy] == 1):
                blue.append((x + dx, y + dy, size))
            else:
                white.append((x + dx, y + dy, size))
print(num_white)
print(num_blue)
'''
#using recursion, divide and concuper..
num_white = 0
num_blue = 0 
def divide(x, y, size):
    global num_white, num_blue
    color = board[x][y]
    if(size != 1):
        for i in range(x, x + size):
            for j in range(y, y + size):
                if(board[i][j] != color):
                    for dx, dy in ((0, 0), (size // 2, 0), (0,size // 2), (size // 2, size // 2)):
                        divide(x + dx, y + dy, size//2)
                    return
    if(color == 1):
        num_blue +=1
    else:
        num_white += 1
divide(0,0, n)
print(num_white)
print(num_blue)