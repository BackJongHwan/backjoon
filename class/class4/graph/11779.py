# 경로를 포함해야하는 알고리즘
# N <= 10^3, M = 10^5
# 벨만포드? -> O(N * M) -> 너무 느림
# dijktra algorithm  -> good choice
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
# 인접 리스트를 이용
# 리스트 초기화
graph = {}
for i in range(1, n+1):
    graph[i] = {}
    
# 인접리스트 입력받기
for _ in range(m):
    start, end, cost = map(int, input().split())
    if end in graph[start]:
        graph[start][end] = min(graph[start][end], cost)
    else:
        graph[start][end] = cost
start, end = map(int, input().split())
# print(graph)

# path를 저장하는 방식
'''
def dijkstra(start, end):
    pq = []
    # path = []
    distance = [float("inf")] * (n + 1)
    distance[start] = 0
    path = [[] for _ in range(n+1)]
    path[start] = [start]
    # print(path)
    heapq.heappush(pq,  (0, start, path[start]))
    while True:
        current_distance, current_node, curr_path = heapq.heappop(pq)
        print(curr_path)
        if(current_node == end):
            path[end] = curr_path
            break
        for next_node, dest in graph[current_node].items():
            # print(next_node, dest)
            if dest + current_distance < distance[next_node]:
                distance[next_node] = dest + current_distance
                path[next_node] = path[current_node] + [next_node]
                heapq.heappush(pq, (distance[next_node], next_node, path[next_node]))
    return distance[end], path[end]
'''

# path를 previous를 이용한 방식
def dijkstra2(start, end):
    pq = []
    distance = [float("inf")] * (n + 1)
    distance[start] = 0
    previous = [-1] * (n + 1)
    heapq.heappush(pq, (0, start))
    while pq:
        curr_dist, curr_node = heapq.heappop(pq) 
        if curr_node == end:
            break
        if curr_dist > distance[curr_node]:
            continue
        for next_node, cost in graph[curr_node].items():
            new_dist = cost + curr_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                previous[next_node] = curr_node
                heapq.heappush(pq, (new_dist, next_node))
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        curr = previous[curr]
    path.reverse()
    return distance[end],path
distance, path = dijkstra2(start, end)
print(distance)
print(len(path))
print(" ".join(map(str, path)))
