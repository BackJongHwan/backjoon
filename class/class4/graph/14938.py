# dijkstra-> 수색범위 내의 노드의 아이템 개수만 + 
# 모든 node에 대해 가능하므로 floyid algorithm
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
n_list = list(map(int, input().split()))
graph = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]  + graph[k][j])

result = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if(graph[i][j] <= m):
            temp += n_list[j]
    #         print(j + 1)
    # print(temp)
    result = max(result, temp)
print(result)