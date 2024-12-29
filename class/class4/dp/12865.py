# n = 100 -> O(N^3)
# backtracing -> 시간초과
# dp -> 각각의 상황에서 item을 넣을 지 말지
import sys
input = sys.stdin.readline

# def backtracking(items, idx, cost, value):
#     if(cost > k):
#         return
#     values.append(value)
#     for i in range(idx, n):
#         backtracking(items, i + 1, cost + items[i][0], value + items[i][1])

        
n, k = map(int, input().split())
items = []
# values =[] 
for _ in range(n):
    w, v = map(int ,input().split())
    items.append((w, v))

dp = [0] * (k + 1)

for weight, value in items:
    for curr_weight in range(k, weight -1, -1):
        dp[curr_weight] = max( dp[curr_weight], dp[curr_weight - weight] + value)

print(dp[k])
# backtracking(items, 0, 0, 0)
# print(max(values))