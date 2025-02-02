def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n  # 각 위치에서의 LIS 길이를 저장하는 배열
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
n = int(input())
arr = list(map(int ,input().split()))
result = longest_increasing_subsequence(arr)
print(result)