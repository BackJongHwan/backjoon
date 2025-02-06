# node = 10^4 edge = 10^5
import sys
input = sys.stdin.readline

# 입력받아서 graph만들기
# Kruskal algorithm

# Prim algorith
import heapq

V,E = map(int, input().split())
graph = {i : [] for i in range(1, V + 1)}
edges = []
for _ in range(E):
    u, v, cost = map(int ,input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))
    edges.append((cost, u, v))
def prim(start, V, graph):
    mst_weight = 0
    min_heap = []
    visited = [False] * (V+1)
    heapq.heappush(min_heap, (0, start))
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += weight
        for v, cost in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (cost, v))
    return mst_weight 
def kruskal(edges):
    edges.sort()
    mst_weight = 0
    k = 0
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_weight += cost
            k += 1
        if k == V-1:
            break
    return mst_weight

rank = [1] *(V + 1)
parent = [-1] *(V+1)
for i in range(1 , V  + 1):
    parent[i] = i
def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rootU != rootV:
        if rank[rootU] > rank[rootV]:
            parent[rootV] = rootU
        elif rank[rootU] < rank[rootV]:
            parent[rootU] = rootV
        else:
            parent[rootV] = rootU
            rank[rootU] += 1

# x의 root찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


result = prim(1, V, graph)
result2 = kruskal(edges)
# print(result)
print(result2)