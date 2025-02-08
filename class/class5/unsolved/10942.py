# palindrome
# n = 10^3 M = 10^6
# 내부가 palindrome인 것을 이용하는 거군..

import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
m = int(input().strip())
palindrome = [[0] * n for _ in range(n)]

# start, end가 같으면 palindrome
for i in range(n):
    palindrome[i][i] = 1
# 길이 2인 문자열의 경우
for i in range(n-1):
    if nums[i] == nums[i + 1]:
        palindrome[i][i + 1] = 1
# 길이 3 이상인 경우 (DP)
for length in range(3, n+1):  # 길이 3부터 n까지
    for start in range(n - length - 1):
        end = start + length - 1
        if nums[start] == nums[end] and palindrome[start + 1][end - 1] == 1:
            palindrome[start][end] = 1
# print(palindrome)
for _ in range(m):
    s, e = map(int, input().split())
    s,e = s-1, e -1
    print(palindrome[s][e])