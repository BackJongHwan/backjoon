import sys
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[float('inf')] * n for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c
v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1
dict_1 = {}
dict_v1 = {}
dict_v2 = {}
# 1 -> v1 경로
# 1 -> v2 경로


# v1 -> N 경로
# v1 -> v2 경로

# v2 - > N 경로

# 1 -> v1 -> v2 -> N
    # 1 -> v1 경로 중간에 v2가 있는 경우
    # 없는 경우
# 1 -> v2 -> v1 -> N
    # 1 -> v2 경로 중간에 v1이 있는 경우
    # 없는 경우