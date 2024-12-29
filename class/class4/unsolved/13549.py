from queue import Queue
n, k = map(int ,input().split())
dp = [float('inf')] * (k + 2)
q = Queue()
q.put((k, 0))
visited = [False] * (k+2)

while(True):
    value, idx = q.get()
    if(value == n):
        print(idx)
        break
    if visited[value]:
        continue
    visited[value] = True
    if(value % 2 == 1):
        if not visited[]