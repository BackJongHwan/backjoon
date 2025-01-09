import sys
from queue import Queue
input = sys.stdin.readline

# graph 입력받기
n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    data = input()
    for j in range(m):
        matrix[i][j] = int(data[j])

# bfs start
# 벽을 뚫었는지 안 뚫었는지 알기위해 q에 False, True로 구분함
# 벽을 뚫었으면 True로 구분됨
q = Queue()
vistied = [[False] * m for _ in range(n)]
vistied[0][0] = True
visitd_wall = [[False] * m for _ in range(n)]
visitd_wall[0][0] = True
q.put((0, 0, False, 1))
result = 0
check = False
while not q.empty():
    row, col, flag, step  = q.get()
    if(row == n-1 and col == m-1):
        check = True
        result = step
        break
    # 네 방향으로 갈 수 있음
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in direction:
        d_row = row + dx
        d_col = col + dy
        if 0<= d_row < n and 0<= d_col < m:
            if not vistied[d_row][d_col]:
                # 이미 벽을 뚫었을 때
                if flag:
                    # 벽을 뚫고나서 방문 한 곳이 아닐 때 
                    if not visitd_wall[d_row][d_col]:
                        if matrix[d_row][d_col] == 0:
                            visitd_wall[d_row][d_col] = True
                            q.put((d_row, d_col,flag, step+1))
                # 벽을 아직 안 뚫었을 때
                else:
                    if matrix[d_row][d_col] == 1:
                        vistied[d_row][d_col] = True
                        q.put((d_row, d_col, True, step+1))
                    else:
                        vistied[d_row][d_col] = True
                        q.put((d_row, d_col, flag, step+1))
if check:
    print(result)
else:
    print(-1)