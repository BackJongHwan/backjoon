#n = 10^5, k = 10^5 using dp
n, k = map(int, input().split())
if(n >= k):
    print(n - k)
else:
    dp = [float("inf")] * (k + 2)
    dp[n] = 0
    for i in range(0, n):
        dp[i] = n - i
    # i가 바뀌면 i -1도 바뀌어야 한다
    for i in range(k + 2):
        temp = dp[i]
        if(i > 0):
            dp[i] = min(dp[i], dp[i-1] + 1)
        if(i % 2 == 0):
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if(i != k + 1):
            dp[i] = min(dp[i], dp[i + 1] + 1)
        if(temp != dp[i]):
            if(i > 0):
                dp[i-1] = min(dp[i-1] , dp[i] + 1 )
    print(dp[k])