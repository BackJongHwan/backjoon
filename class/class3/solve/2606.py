# vertex (n = 10^2)
# edge -> n^2 -> 10^4
# O(V + E)
# O(nlong)??

def dfs(graph, start, visited):
    visited[start] = 1
    for neighbor in range(len(graph[start])):
        if graph[start][neighbor] == 1 and not visited[neighbor]:
            dfs(graph, neighbor, visited)

n = int(input())
num_edge = int(input())
adj_matrix = []
for i in range(n):
    adj_matrix.append([0] * n)
for i in range(num_edge):
    vertex1, vertex2 = map(int,input().split())
    adj_matrix[vertex1 - 1][vertex2 - 1] = 1
    adj_matrix[vertex2 - 1][vertex1 - 1] = 1
visited = [0] * n
#using DFS using stack
'''
visited[0] = 1
stack = [0]
while stack:
    num = stack.pop()
    for i in range(n):
        if(adj_matrix[num][i] == 1):
            if(visited[i] == 0):
                visited[i] = 1
                stack.append(i)
'''
#using DFS using recursive
dfs(adj_matrix, 0, visited)
cnt = -1
for i in range(n):
    cnt += visited[i]
print(cnt)