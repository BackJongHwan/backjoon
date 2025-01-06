import sys
input = sys.stdin.readline


n = int(input())

graph = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

m = int(input())

# graph 입력받아서 채우기
for _ in range(m):
    a, b, c = map(int ,input().split())
    a -= 1
    b -= 1
    if(c < graph[a][b]):
        graph[a][b] = c

# 플로이드 알고리즘을 이용하여 모든 노드에 대해 최소값 구하기
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# graph 출력
for i in range(n):
    for j in range(n):
        if(graph[i][j] == float("inf")):
            print(0, end= " ")
        else:
            print(graph[i][j], end=" ")
    print()