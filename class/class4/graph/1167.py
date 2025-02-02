# Node의 개수가 10^5 Edge는 tree니까 Edge의 개수가 N - 1

import sys
from queue import Queue
input = sys.stdin.readline

n = int(input())

tree = {i : [] for i in range(1, n + 1)}
for _ in range(n):
    temp = list(map(int ,input().split()))
    node = temp[0]
    for i in range(1, len(temp) - 1, 2):  # -1은 마지막의 `-1` 제외
        child, weight = temp[i], temp[i + 1]
        tree[node].append((child, weight))  # 인접 리스트에 추가
# print(tree)

def bfs(start):
    # print(start)
    visited = [False] * (n + 1)
    q = Queue()
    q.put((start, 0))
    end_node = start
    result_len = 0
    visited[start] = True
    while not q.empty():
        curr_node, curr_cost = q.get()
        # print(curr_node, curr_cost)
        for next_node, cost in tree[curr_node]:
            # 방문하지 않은 노드라면
            if not visited[next_node]:
                q.put((next_node, curr_cost + cost))
                visited[next_node] = True
                if result_len < curr_cost + cost:
                    result_len = curr_cost + cost
                    end_node = next_node
    return end_node, result_len

temp, _ = bfs(1)
_, result = bfs(temp)
print(result)
        
