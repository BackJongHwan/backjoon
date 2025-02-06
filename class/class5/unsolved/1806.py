# N = 10^5
# sum >= S
import sys
input = sys.stdin.readline
n, s = map(int ,input().split())
nums = list(map(int , input().split()))
# print(nums)
sums = [0] * (n + 1)
sums[1] = nums[0]
for i in range(n):
    sums[i + 1] = sums[i] + nums[i]
if sums[n] < s:
    print(0)
else:
    