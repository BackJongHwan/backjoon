# tree diameter -> start any leaf node -> BFS find lognest leaf node
# start this node BFS -> find result

import sys
from queue import Queue
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit(0)
tree = {}
for i in range(1, n + 1):
    tree[i] = {}
# print(tree)
leaf = 0
for i in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent][child] = weight
    tree[child][parent] = weight
    if(i == n-2):
        leaf = child
def bfs(start):
    q = Queue()
    # print(start)
    visited = [False] * (n + 1)
    longest_node, longest_distance = start, 0
    visited[start] = True
    q.put((longest_node, longest_distance))
    while not q.empty():
        current_node, current_distance = q.get()
        neighbors = list(tree[current_node].items())
        # print(neighbors)
        for node, weight in neighbors:
            if visited[node] == False:
                # print(node, weight)
                visited[node] = True
                distance = weight +  current_distance
                # print(node, distance)
                if(distance > longest_distance):
                    longest_distance = distance
                    longest_node = node
                q.put((node, distance))
    return longest_node, longest_distance
node1, _ = bfs(leaf)
_ , result = bfs(node1)
print(result)
