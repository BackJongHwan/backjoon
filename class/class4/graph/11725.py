import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
resultDict = dict()
visited = [False] * n
adj_list = {i: [] for i in range(n)}
for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    adj_list[node1 - 1].append(node2 -1)
    adj_list[node2 - 1].append(node1 - 1)
queue = deque([0])
visited[0] = True
while queue:
    node = queue.popleft()
    for i in adj_list[node]:
        if not visited[i]:
            visited[i] = True
            resultDict[i] = node
            queue.append(i)
for i in range(1, n):
    print(resultDict[i] + 1)