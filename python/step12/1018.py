def coloring(board):
    temp1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
    temp2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
    num1 = 0
    num2 = 0
    for i in range(8):
        for j in range(8):
            if(board[i][j] != temp1[i][j]):
                num1 +=1
            if(board[i][j] != temp2[i][j]):
                num2 +=1
    return (min(num1, num2))


m, n = map(int, input().split())
arr = []
min_value = 0
for _ in range(m):
    row = input()
    arr.append(list(row))
for i in range(m - 7):
    for j in range(n - 7):
        board = [row[j: j + 9] for row in arr[i: i + 9]]
        value = coloring(board)
        if(i == 0 and j == 0):
            min_value = value
        else:
            if(min_value > value):
                min_value = value
print(min_value)