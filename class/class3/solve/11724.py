import sys
input = sys.stdin.readline
def dfs(visited, vertices, adj_matrix, n , v):
    vertices.remove(v)
    for i in range(n):
        if(adj_matrix[i][v] == 1):
            if visited[i] == 0:
                visited[i] = 1
                if i in vertices:
                    dfs(visited, vertices, adj_matrix, n, i)

n, m = map(int,input().split())
adj_matrix = [[0] * n for i in range(n)] 
for _ in range(m):
    v1, v2 = map(int, input().split())
    adj_matrix[v1 - 1][v2 -1] = 1
    adj_matrix[v2 - 1][v1 - 1] = 1
vertices = []
for i in range(n):
    vertices.append(i)
num = 0
visited = [0] * n
while vertices:
    dfs(visited, vertices, adj_matrix, n, vertices[0])
    num += 1
print(num)