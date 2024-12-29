# using dp, memory가 제한적인 상황 -> sliding window방식 이전의 max, min만 기억하기
'''
import sys
input = sys.stdin.readline
n = int(input())
min_dp = [ [float('inf')] * 3 for _ in range(n)]
max_dp = [ [0] * 3 for _ in range(n)]
matrix = [[0] * 3 for _ in range(n)]
for i in range(n):
    matrix[i][0], matrix[i][1], matrix[i][2] = map(int ,input().split())
    if(i == 0):
        min_dp[i][0], min_dp[i][1], min_dp[i][2] =  matrix[i][0], matrix[i][1], matrix[i][2]
        max_dp[i][0], max_dp[i][1], max_dp[i][2] =  matrix[i][0], matrix[i][1], matrix[i][2]
for i in range(1, n):
    min_dp[i][0] = min(min_dp[i-1][0], min_dp[i-1][1]) + matrix[i][0]
    min_dp[i][1] = min(min_dp[i-1][0], min_dp[i-1][1], min_dp[i-1][2]) + matrix[i][1]
    min_dp[i][2] = min(min_dp[i-1][1], min_dp[i-1][2]) + matrix[i][2]

    max_dp[i][0] = max(max_dp[i-1][0], max_dp[i-1][1]) + matrix[i][0]
    max_dp[i][1] = max(max_dp[i-1][0], max_dp[i-1][1], max_dp[i-1][2]) + matrix[i][1]
    max_dp[i][2] = max(max_dp[i-1][1], max_dp[i-1][2]) + matrix[i][2]
print(max(max_dp[n-1][0], max_dp[n-1][1], max_dp[n-1][2]), min(min_dp[n-1][0], min_dp[n-1][1], min_dp[n-1][2]))
'''
import sys
input = sys.stdin.readline
n = int(input())
min_value = [float('inf')] * 3
max_value = [0] * 3
for i in range(n):
    val1, val2, val3 = map(int ,input().split())
    if(i == 0):
        min_value[0], min_value[1], min_value[2] = val1, val2, val3
        max_value[0], max_value[1], max_value[2] = val1, val2, val3
        continue
    temp1 = min(min_value[0], min_value[1]) + val1
    temp2 = min(min_value[0], min_value[1], min_value[2]) + val2
    temp3 = min(min_value[1], min_value[2]) + val3
    min_value[0], min_value[1], min_value[2] = temp1, temp2, temp3

    temp1 = max(max_value[0], max_value[1]) + val1
    temp2 = max(max_value[0], max_value[1], max_value[2]) + val2
    temp3 = max(max_value[1], max_value[2]) + val3
    max_value[0], max_value[1], max_value[2] = temp1, temp2, temp3
print(max(max_value), min(min_value))
    