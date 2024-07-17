from collections import deque

def bfs(n, v):
    visited = [0] * n
    visited[v] = 1
    d = deque([(v, 0)])
    result = 0
    a = 0
    while d:
        k = d.popleft()
        result += k[1]
        for i in range(n):
            if(adj_list[i][k[0]] == 1):
                if(visited[i] == 0):
                    visited[i] = 1
                    step = k[1] + 1
                    d.append((i, step))
    return result


n, edge = map(int, input().split())
adj_list = [[0] * n for _ in range(n)]
for _ in range(edge):
    v1, v2 = map(int ,input().split())
    v1 -= 1
    v2 -= 1
    adj_list[v1][v2] = 1
    adj_list[v2][v1] = 1
num_list = []
for i in range(n):
    num_list.append((bfs(n, i), i + 1))
result = min(num_list)
print(result[1])