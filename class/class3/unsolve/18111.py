import sys
input = sys.stdin.readline


n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    ground.append(list(map(int ,input().split())))
max_h = 0
for i in range(n):
    for j in range(m):
        if(ground[i][j] > max_h):
            max_h = ground[i][j]
result = []
while max_h > 0:
    