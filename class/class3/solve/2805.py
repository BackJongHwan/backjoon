# n=10^6 -> O(n)
# m = 10^9
def result(trees, m, left, right):
    mid = (left + right) // 2
    if(left > right):
        return mid
    sum = 0
    for i in range(len(trees)):
        if(trees[i] - mid > 0):
            sum += trees[i] - mid
    if(sum < m):
        return result(trees, m, left, mid - 1)
    elif(sum > m):
        return result(trees, m, mid + 1, right)
    else:
        return mid

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
min_h = 1 
max_h = max(trees)
h = result(trees, m, 1, max_h)
print(h)