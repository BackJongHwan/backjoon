import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0] * n for _ in range(n)]
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp[0][0] = matrix[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + matrix[i][0]
    dp[0][i] = dp[0][i-1] + matrix[0][i]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = matrix[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
# print(dp)
for _ in range(m):
    x1, y1, x2, y2 = map(lambda x : int(x) - 1, input().split())
    if x1 > 0 and y1 > 0:
        result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    elif x1 > 0:
        result = dp[x2][y2] - dp[x1-1][y2]
    elif y1 > 0:
        result = dp[x2][y2] - dp[x2][y1-1]
    else:
        result = dp[x2][y2]
    print(result)