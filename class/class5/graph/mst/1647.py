# N = 10^5 M = 10^6
import sys
input = sys.stdin.readline


V, E = map(int, input().split())
edges=[]
for _ in range(E):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))
num_set = V
parent = [i for i in range(V + 1)]
rank = [1] *(V + 1)
def kruskal():
    global num_set
    if num_set <= 2:
        return 0
    mst_weight = 0
    edges.sort()
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            num_set -= 1
            mst_weight += cost
        if num_set == 2:
            break
    return mst_weight
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rank[rootU] > rank[rootV]:
        parent[rootV] = rootU
    elif rank[rootU] < rank[rootV]:
        parent[rootU] = rootV
    else:
        parent[rootV] = rootU
        rank[rootU] += 1
result = kruskal()
print(result)