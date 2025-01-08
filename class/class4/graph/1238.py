# floyd alogrithm -> O(N^3)
# n <= 1000 이기에 O(N^3)은 안 됨
# 모든 곳에서 x까지의 최솟값 -> using bfs -> 다익스트라 알고리즘을 이용하는데 뒤집어진 그래프 이용
# x -> 모든 곳 까지의 최솟값 -> dijstra algoritm 
# O((V + E) logV) -> 인접리스트 + 우선순위 큐 O(V^2) -> 인접행렬

import sys
from queue import Queue
input = sys.stdin.readline

# 입력받아서 graph 만들기
n, m, x = map(int, input().split())
graph = [[float("inf")] * n for _ in range(n)]
reverse_graph = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
    reverse_graph[i][i] = 0
for _ in range(m):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    graph[start][end] = min(graph[start][end], cost)
    reverse_graph[end][start] = min(reverse_graph[end][start], cost)
x -= 1

'''
# 플로이드 알고리즘 적용 -> O(N^3) 이기에 N<=500이어야함
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
x -= 1
result = 0  
for i in range(n):
    temp = graph[i][x] + graph[x][i]
    result = max(result, temp)
print(result)
'''
'''
# BFS 이용하여 x까지의 거리 찾기
to_x = []
def bfs(start):
    if(start == x):
        return 0
    q = Queue()
    distance = float("inf")
    q.put((0, start))
    visited = [False] * n
    visited[start] = True
    while not q.empty():
        # start에서까지의 최소거리
        curr_distance, curr_node = q.get()
        # path가 있고 아직 방문하지 않은 노드
        for i in range(n):
            if graph[curr_node][i] != float("inf") and not visited[i]:
                # 만약 x로의 path가 있다면 짧은 거리를 선택함
                if(i == x):
                    distance = min(distance, curr_distance + graph[curr_node][i])
                else:
                    visited[i] = True
                    curr_distance += graph[curr_node][i]
                    q.put((curr_distance, i))
    return distance
for i in range(n):
    to_x.append(bfs(i))
'''

# 다익스트라 알고리즘을 이용함

def dijkstra(graph):
    distance = [float("inf")] * n
    distance[x] = 0
    visited = [False] * n
    for _ in range(n):
        # 가장 짧은 거리를 가진 node 선택
        curr_node = 0
        min_value = float("inf")
        for idx in range(n):
            if not visited[idx]:
                if(min_value > distance[idx]):
                    curr_node = idx
                    min_value = distance[idx]
        curr_distance = distance[curr_node]
        # print(curr_node, curr_distance)
        visited[curr_node] = True
        # 그 노드에서 거리 택하기
        for i in range(n):
            if graph[curr_node][i] != float("inf"):
                distance[i] = min(distance[i], curr_distance + graph[curr_node][i])
    return distance
x_to = dijkstra(graph)
to_x = dijkstra(reverse_graph)

# print(x_to)
# 결과 출력
# print(to_x)
# print(x_to)
result = 0
for i in range(n):
    result = max(result, to_x[i] + x_to[i])
print(result)