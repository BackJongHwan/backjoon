import sys
from collections import deque
input = sys.stdin.readline
N, M, Q = map(int ,input().split())
def bfs(start,graph):
     


graph = [[float('inf')] * N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0 

for _ in range(M):
    u, v = map(int ,input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1
for i in range(N):
    bfs(i, graph)

for _ in range(Q):
    s, e = map(int ,input().split())
    print(graph[s-1][e-1])