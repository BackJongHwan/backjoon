# using dp

n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)
# visited = [[False] * n for _ in range(n)]
dp = [ [[0, 0, 0] for _ in range(n)] for _ in range(n) ]
dp[0][1][0] = 1

# 첫번째 row만 처리
for col in range(2, n):
    if matrix[0][col] != 1:
        dp[0][col][0] = dp[0][col-1][0]
# print(dp)
# start 2nd row and 3rd col
for row in range(1, n):
    for col in range(2, n):
        if matrix[row][col] == 1:
            continue
        # 위, 왼쪽에  벽이 있을 때
        if(matrix[row-1][col] == 1 and matrix[row][col] == 1):
            continue
        # 위에만 벽이 있을 때
        elif matrix[row-1][col] == 1:
            dp[row][col][0] = dp[row][col-1][0] + dp[row][col-1][2]
        # 왼쪽에만 벽이 있을 때
        elif matrix[row][col-1] == 1:
            dp[row][col][1] = dp[row-1][col][1] + dp[row-1][col][2]
        # 둘다 벽이 없을 때
        else:
            dp[row][col][0] = dp[row][col-1][0] + dp[row][col-1][2]
            dp[row][col][1] = dp[row-1][col][1] + dp[row-1][col][2]
            dp[row][col][2] = dp[row-1][col-1][0] + dp[row-1][col-1][1] + dp[row-1][col-1][2]
# print(dp)
result = dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2]
print(result)