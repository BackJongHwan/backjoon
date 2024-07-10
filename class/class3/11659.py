# n, m = 10^5 -> O(nlogn)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
prefix_sum = []
for i in range(n):
    if(i == 0):
        prefix_sum.append(num_list[i])
    else:
        prefix_sum.append(num_list[i] + prefix_sum[i - 1])
for _ in range(m):
    i, j = map(int ,input().split())
    result = 0
    if(i == 1):
        result = prefix_sum[j - 1]
    else:
        result = prefix_sum[j - 1] - prefix_sum[i - 2]
    print(result)