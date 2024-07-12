import sys
from collections import deque
input = sys.stdin.readline

def dfs(size, n, adj_matrix,visited):
    if(visited[n] == 1):
        return
    visited[n] = 1
    print(n + 1, end=" ")
    for i in range(size):
        if(adj_matrix[n][i] == 1):
                dfs(size, i , adj_matrix, visited)
def bfs(size, n, adj_matrix, visited):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        v = q.popleft()
        print(v + 1, end=" ")
        for i in range(size):
            if(adj_matrix[v][i] == 1):
                if (visited[i] == 0):
                    q.append(i)
                    visited[i] = 1
n, m, v = map(int, input().split())
adj_matrix = [[0] * (n) for i in range(n)]
visited = [0] * n
for _ in range(m):
    v1, v2 = map(lambda x : int(x) - 1, input().split())
    adj_matrix[v1][v2] = 1
    adj_matrix[v2][v1] = 1
dfs(n, v - 1, adj_matrix,visited)
print()
visited = [0] * n
bfs(n, v - 1, adj_matrix, visited)
print()