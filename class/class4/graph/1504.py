import sys
import heapq
input = sys.stdin.readline
def dijkstra(start, n):
    distance = [float('inf')] * n
    previous = [-1] * n
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while(pq):
        current_dist, current_node = heapq.heappop(pq)
        if distance[current_node] < current_dist:
            continue
        for neighbor, weight in graph.get(current_node, []): 
            new_dist = current_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(pq,  (new_dist, neighbor))
    return distance, previous
def make_path(previous, start, end):
    path = []
    at = end
    while at != -1:
        path.append(at)
        at = previous[at]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return []
n, e = map(int, input().split())
graph = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if a not in graph:
        graph[a] = []
    graph[a].append((b, c))
    # Add edge b -> a
    if b not in graph:
        graph[b] = []
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
# print(graph)
v1 -= 1
v2 -= 1
find = False
# 1
distance_1, previous_1 = dijkstra(0, n)
    # 1 -> v1 경로
path_1_v1 = make_path(previous_1, 0, v1)
    # 1 -> v2 경로
path_1_v2 = make_path(previous_1, 0, v2)

# v1
distance_v1, previous_v1 = dijkstra(v1, n)
    # v1 -> N 경로
path_v1_n = make_path(previous_v1, v1, n-1)
    # v1 -> v2 경로
path_v1_v2 = make_path(previous_v1, v1, v2)
# v2
distance_v2, previous_v2 = dijkstra(v2, n)
    # v2 - > N 경로
path_v2_n = make_path(previous_v2, v2, n-1)

# 1 -> N까지의 최소경로에 v1, v2가 있을 경우
# path_1_n = make_path(previous_1, 0, n-1)
# if path_1_n:
#     if v1 in path_1_n and v2 in path_1_v2:
#         find = True
#         print(distance_1[n-1])
result = float("inf")
'''
if path_1_v1:
# 1 -> v1 -> v2 -> N
    # 1 -> v1 경로 중간에 v2가 있는 경우
    if v2 in path_1_v1:
        if path_v1_n:
            find = True
            result = min(result, distance_1[v1] + distance_v1[n-1])
    else:
        if path_v1_v2 and path_v2_n:
            find = True
            result = min(result, distance_1[v1] + distance_v1[v2] + distance_v2[n-1])
if path_1_v2:
# 1 -> v2 -> v1 -> N
    # 1 -> v2 경로 중간에 v1이 있는 경우
    if v1 in path_1_v2:
        find = True
        result = min(result, distance_1[v2] + distance_v2[n-1])
    # 없는 경우
    else:
        if path_v1_v2 and path_v1_n:
            find = True
            result = min(result, distance_1[v2] + distance_v2[v1] + distance_v1[n-1])
if result == float('inf'):
    print(-1)
else:
    print(result)
'''
# Path 1 -> v1 -> v2 -> N
if path_1_v1 and path_v1_v2 and path_v2_n:
    result = min(result, distance_1[v1] + distance_v1[v2] + distance_v2[n - 1])
# Path 1 -> v2 -> v1 -> N
if path_1_v2 and path_v1_v2 and path_v1_n:
    result = min(result, distance_1[v2] + distance_v2[v1] + distance_v1[n - 1])

print(-1 if result == float('inf') else result)