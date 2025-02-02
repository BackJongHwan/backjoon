# n <= 100000
# using dp
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0] * n for _ in range(2)] 
    # print(dp)
    num_list = []
    for _ in range(2):
        list_ = list(map(int, input().split()))
        num_list.append(list_)
    if(n == 1):
        # print(num_list)
        print(max(num_list[0][0], num_list[1][0]))
        continue 
    if(n == 2):
        print(max(num_list[0][0] + num_list[1][1], num_list[1][0] + num_list[0][1]))
        continue
    dp[0][0] = num_list[0][0]
    dp[1][0] = num_list[1][0]
    dp[0][1] = num_list[1][0] + num_list[0][1]
    dp[1][1] = num_list[0][0] + num_list[1][1]
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + num_list[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + num_list[1][i]
    print(max(dp[0][n-1], dp[1][n-1]))