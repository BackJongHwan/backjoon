import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    result = 0
    m, n, k = map(int, input().split())
    board = [[0] * n for i in range(m)]
    visited_set = set()
    for _ in range(k):
        x, y = map(int,input().split())
        board[x][y] = 1
        visited_set.add((x, y))
    while visited_set:
        result += 1
        stack = [] 
        stack.append(visited_set.pop())
        while stack:
            position = stack.pop()
            visited_set.discard(position)
            if(position[0] + 1, position[1]) in visited_set:
                stack.append((position[0] + 1, position[1]))
            if(position[0] - 1, position[1]) in visited_set:
                stack.append((position[0] - 1, position[1]))
            if(position[0], position[1] + 1) in visited_set:
                stack.append((position[0], position[1] + 1))
            if(position[0], position[1] - 1) in visited_set:
                stack.append((position[0], position[1] - 1))
    print(result)
