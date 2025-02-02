#LCS의 경우 뭐였더라. two pointer, sliding window? -> 2차원 dp
# 0인 배열을 활용해야하는 문제
s1 = input()
s2 = input()
len_row = len(s1)
len_col = len(s2)
dp = [[0] * (len_col + 1) for _ in range(len_row + 1)]
for i in range(1, len_row + 1):
    for j in range(1, len_col + 1):
        # 이전 문자열까지의 즉 S1', S2''s longest string에 1을 더함
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # s1', s2' 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print(dp)
print(dp[len_row][len_col])
# check1 = False
# check2 = False
# # row
# for i in range(len_row):
#     if check1:
#         dp[i][0] = 1
#     if s1[i] == s2[0]:
#         check1 = True
#         dp[i][0] = 1

# for i in range(len_col):
#     if check2:
#         dp[0][i] = 1
#     if s1[0] == s2[i]:
#         check2 = True
#         dp[0][i] = 1
# # print(dp)
# row = 1
# col = 1
# while(True):
#     if(row == len_row or col == len_col):
#         break 
#     if(s1[row] == s2[col]):
#         dp[row][col] = max(dp[row][col - 1] , dp[row-1][col]) + 1
#     else:
#         dp[row][col] = max(dp[row-1][col], dp[row][col-1])
#         check1 = False
#         for i in range(row+ 1, len_row):
#             if check1:
#                 dp[i][col] = max(dp[i-1][col], dp[i][col-1])
#                 continue
#             if(s1[i] == s2[col]):
#                 check1 = True
#                 dp[i][col] = max(dp[i-1][col], dp[i][col-1]) + 1
#                 continue
#             dp[i][col] = max(dp[i-1][col], dp[i][col-1])
#         check2 = False
#         for j in range(col + 1, len_col):
#             if check2:
#                 dp[row][j] = max(dp[row][j-1], dp[row-1][j])
#                 continue
#             if(s1[row] == s2[j]):
#                 check2 = True
#                 dp[row][j] = max(dp[row][j-1], dp[row-1][j])+ 1
#                 continue
#             dp[row][j] = max(dp[row][j-1], dp[row-1][j])
#     # print(dp)
#     row += 1
#     col += 1
# # # 남는 row    
# check1 = False 
# if(row < len_row):
#     while(row < len_row):
#         if check1:
#             dp[row+1][col] = dp[row][col]
#             row += 1
#             continue
#         if(s1[row + 1] == s2[col]):
#             check1 = True
#             dp[row+1][col] = dp[row][col] + 1
#             row += 1
#             continue
#         else:
#             dp[row+1][col] = dp[row][col]
#             row+=1
# # # 남는 col
# check1 = False
# if(col < len_col ):
#     while(col < len_col):
#         if check1:
#             dp[row][col + 1] = dp[row][col]
#             col += 1
#             continue
#         if(s1[row] == s2[col + 1]):
#             check1 = True
#             dp[row][col + 1] = dp[row][col] + 1
#             col += 1
#             continue
#         else:
#             dp[row][col + 1] = dp[row][col]
#             col +=1
# # print(dp)
# print(dp[row-1][col-1])