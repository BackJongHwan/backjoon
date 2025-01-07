# floyd alogrithm -> O(N^3)
# n <= 1000 이기에 O(N^3)은 안 됨
# 모든 곳에서 x까지의 최솟값.. 
# x -> 모든 곳 까지의 최솟값 -> dijstra algoritm

# 입력받아서 graph 만들기
n, m, x = map(int, input().split())
graph = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
for _ in range(m):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    graph[start][end] = min(graph[start][end], cost)

'''
# 플로이드 알고리즘 적용
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