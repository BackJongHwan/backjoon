# graph
# maybe 다익스트라 -> 우선순위 큐를 사용하면 더 좋다.
# using adjecent matrix + for loop
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# visited = [False] * n
# distance = [float('inf')] * n
# graph = [[float('inf')] * n for _ in range(n)]
# # print(graph)
# for i in range(n):
#     graph[i][i] = 0
# for _ in range(m):
#     start, end, cost = map(int, input().split())
#     start -= 1
#     end -= 1
#     graph[start][end] = min(graph[start][end],cost)
# # print(graph)
# a, b = map(lambda x : int(x) - 1, input().split())
# distance[a] = 0
# for _ in range(n):
#     min_distance = float('inf')
#     min_node = -1
#     # 방문하지 않는 노드 중 거리가 가장 가까운 것
#     for i in range(n):
#         if not visited[i] and distance[i] < min_distance:
#             min_distance = distance[i]
#             min_node = i
#     # 모두 방문했거나 경로가 없는 것
#     if min_node == -1:
#         break
#     visited[min_node] = True

#     for neighbor in range(n):
#         # min_node 와 adjecent한 node cost 계산 
#         if graph[min_node][neighbor] != float('inf') and not visited[neighbor]:
#             new_distance = distance[min_node] + graph[min_node][neighbor]
#             if new_distance < distance[neighbor]:
#                 distance[neighbor] = new_distance
# print(distance[b])

# using adjecent list and heap queue
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {i: {} for i in range(n)}  # 모든 노드를 초기화
for _ in range(m):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    if end not in graph[start] or cost < graph[start][end]:
        graph[start][end] = cost
a, b = map(lambda x: int(x) - 1 , input().split())

def dijkstra(start):
    distance = {node: float('inf') for node in graph} 
    distance[start] = 0
    pq = []
    heapq.heappush(pq,(0, start)) #heap에 node, cost집어 넣기

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distance[current_node]:
            continue
        if current_node in graph:
            # 인접한 node들
            for neighbor, weight in graph[current_node].items():
                new_dist = current_dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    return distance

distance = dijkstra(a)
print(distance[b])


