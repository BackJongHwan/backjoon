# node = 10^4 edge = 10^5
import sys
input = sys.stdin.readline

# 입력받아서 graph만들기
V,E = map(int, input().split())
graph = {i : [] for i in range(1, V + 1)}
for _ in range(E):
    u, v, cost = map(int ,input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

parent = [-1] *(V + 1)

# 1을 root로 하는 tree 만들기
result = 0
# 1에서 node까지의 거리
distance = [float('inf')] *(V + 1)
distance[1] = 0

def make_tree(node, par, cost):
    anserstor = []
    temp = par
    while temp != -1:
        anserstor.append(temp)
        temp = parent[temp]
    for child, cost_child in graph[node]:
        if child not in anserstor:
            make_tree(child, node, cost + cost_child)
    if(cost < distance[node]):
        parent[node] = par
        result += cost
        distance[node] = cost
make_tree(1, 1, 0)
print(result)