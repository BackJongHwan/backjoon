import sys
import heapq
input = sys.stdin.readline

# make graph
num_v, e = map(int, input().split())
start = int(input())
graph = {}
for i in range(1, num_v + 1):
    graph[i] = {}
for _ in range(e):
    u, v, w = map(int, input().split())
    if v not in graph[u]:
        graph[u][v] = w
    else:
        if(graph[u][v] > w):
            graph[u][v] = w

# dijkstra algorithm
def dijkstra(start):
    distance = [float('inf')] * (num_v+1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if graph[current_node]:
            node_list = list(graph[current_node].items())
            for neighbor, weight in node_list:
                # print(weight, neighbor)
                # print(current_node, neighbor)
                # print(graph[current_node])
                new_dist = current_dist + weight
                if(new_dist < distance[neighbor]):
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    return distance

distance = dijkstra(start)
for i in range(1, num_v + 1):
    if(distance[i] == float('inf')):
        print("INF")
    else: 
        print(distance[i])
