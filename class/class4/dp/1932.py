# dp + tree => O(N^2)
# data structure -> 
n = int(input())
dp = [0] * (n + 1)
for _ in range(n):
    num_list = list(map(int ,input().split()))
    for i in range(len(num_list)):
        # index 처리를 잘 하자
        if i == 0:
            num_list[i] = dp[i] + num_list[i]  # 가장 왼쪽
        elif i == len(num_list) - 1:
            num_list[i] = dp[i-1] + num_list[i]  # 가장 오른쪽
        else:
            num_list[i] = max(dp[i-1], dp[i]) + num_list[i]
    for i in range(len(num_list)):
        dp[i] = num_list[i]
print(max(dp))