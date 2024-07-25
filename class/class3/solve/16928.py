import sys
from collections import deque
input = sys.stdin.readline
def bfs(n, m, ladder, snake):
    dp = [float("inf")] * 101
    dp[1] = 0
    visited = [False] * 101
    visited[1] = True
    queue = deque([1])

    while queue:
        current = queue.popleft()
        visited[current] = True
        for dice in range(1, 7):
            next_pos = current + dice
            if next_pos not in visited:
                if next_pos > 100:
                    continue
                if next_pos in ladder:
                    next_pos = ladder[next_pos]
                elif next_pos in snake:
                    next_pos = snake[next_pos]
            if dp[next_pos] > dp[current] + 1:
                dp[next_pos] = dp[current] + 1
                queue.append(next_pos)
    return dp[100]

n, m = map(int ,input().split())
ladder = {}
snake = {}
for _ in range(n):
    start, end = map(int ,input().split())
    ladder[start] = end
for _ in range(m):
    start, end = map(int ,input().split())
    snake[start] = end
result = bfs(n, m, ladder, snake)
print(result)