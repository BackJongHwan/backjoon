# O(N^2)가능
# dp풀기

n = int(input())
num_list = list(map(int, input().split()))
# dp[0] is increasing, dp[1] is decreasing
# value, len
increasing_dp = [0] * n
decreasing_dp = [0] * n

increasing_dp[0] = 1
decreasing_dp[0] = 1

for i in range(1, n):
    # increasing 먼저
    for j in range(i):
        if(num_list[j] < num_list[i]):
            increasing_dp[i] = max(increasing_dp[i], increasing_dp[j])
    increasing_dp[i] += 1
for i in range(1, n):
    for j in range(i):
        if(num_list[j] > num_list[i]):
            decreasing_dp[i] = max(increasing_dp[j], decreasing_dp[i], decreasing_dp[j])
    decreasing_dp[i] += 1
max_val1 = max(increasing_dp)
max_val2 = max(decreasing_dp)
print(max(max_val1, max_val2))


'''
k로 두고 증가하는 거랑 감소하는 거랑 더해서~~!!

'''