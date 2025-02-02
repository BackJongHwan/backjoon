#dp
from queue import Queue
q = Queue()
n = int(input())
r, g, b = map(int ,input().split())
q.put(r)
q.put(g)
q.put(b)
# print(r, g, b)
for _ in range(n-1):
    r1, g1, b1 = map(int, input().split())
    r_min = q.get()
    g_min = q.get()
    b_min = q.get()
    # print(red, green, blue)
    r_min2 = min(g_min + r1, b_min + r1)
    g_min2 = min(b_min + g1, r_min + g1)
    b_min2 = min(r_min + b1, g_min + b1)
    q.put(r_min2)
    q.put(g_min2) 
    q.put(b_min2)
r_min = q.get()
g_min = q.get()
b_min = q.get()
# print(r_min, g_min, b_min)
print(min(r_min, g_min, b_min))