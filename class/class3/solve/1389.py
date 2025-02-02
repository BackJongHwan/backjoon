from collections import deque
import sys
input = sys.stdin.readline
#using bfs
'''
def bfs(n, v):
    visited = [0] * n
    visited[v] = 1
    d = deque([(v, 0)])
    result = 0
    a = 0
    while d:
        k = d.popleft()
        result += k[1]
        for i in range(n):
            if(adj_list[i][k[0]] == 1):
                if(visited[i] == 0):
                    visited[i] = 1
                    step = k[1] + 1
                    d.append((i, step))
    return result

n, edge = map(int, input().split())
adj_list = [[0] * n for _ in range(n)]
for _ in range(edge):
    v1, v2 = map(int ,input().split())
    v1 -= 1
    v2 -= 1
    adj_list[v1][v2] = 1
    adj_list[v2][v1] = 1
num_list = []
for i in range(n):
    num_list.append((bfs(n, i), i + 1))
result = min(num_list)
print(result[1])
'''

#using floyd-warshell algorithm
n, edge = map(int, input().split())
graph = [[float("Inf")] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(i == j):
            graph[i][j] = 0

for _ in range(edge):
    v1, v2 = map(int ,input().split())
    v1 -= 1
    v2 -= 1
    graph[v1][v2] = 1
    graph[v2][v1] = 1
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
min_value = float("Inf")
for row in range(n):
    count = 0
    for col in range(n):
        count += graph[row][col]
    if(count < min_value):
        min_value = count
        result = row
print(result + 1)