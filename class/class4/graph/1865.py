# floyd 사용해서 그냥 하려고 했는데 O(N^3)으로 안 됨
# 인접리스트로 하는 것이 일반적이고 인접행렬을 한다고 해도 시간복잡도가 O(N^3) 

import sys
input = sys.stdin.readline
INF = 10**9
# graph 입력받기 -> adjecent list 이용 -> 이것도 플로이드 알고리즘을 이용한다면 O(N^3) 불가능
tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[float("inf")] * n for _ in range(n)]
    edges = []
    # 간선을 입력받음   
    for _ in range(m):
        s, e, t = map(int ,input().split())
        edges.append((s-1, e-1, t)) 
        edges.append((e-1, s-1, t))
    for _ in range(w):
        s, e, t = map(int ,input().split())
        edges.append((s-1, e-1, -t))

    def bellman_ford(n, edges):
        distance = [INF] * n
        distance[0] = 0
        for _ in range(n-1):
            for u, v, w in edges:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                return True
        return False
    check = bellman_ford(n, edges)
    if check:
        print("YES")
    else:
        print("NO")

    