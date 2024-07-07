# n = 10^3 -> O(n^2)
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ballon = deque(enumerate(map(int, input().split())))
result = []

while ballon:
    idx, paper= ballon.popleft()
    result.append(idx + 1)
    if paper > 0:
        ballon.rotate(-(paper - 1))
    else:
        ballon.rotate(-paper)


print(' '.join(map(str, result)))