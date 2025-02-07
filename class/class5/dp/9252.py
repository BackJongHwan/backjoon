# 2D dp이용하는 거 였는데
str1 = input()
str2 = input()

dp = [[[0, ""] for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if(str1[i-1] == str2[j-1]):
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            dp[i][j][1] = dp[i-1][j-1][1] + str1[i-1]
        else:
            if(dp[i-1][j][0] > dp[i][j-1][0]):
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1] = dp[i-1][j][1]
            else:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][1] = dp[i][j-1][1]

print(dp[len(str1)][len(str2)][0])
print(dp[len(str1)][len(str2)][1])