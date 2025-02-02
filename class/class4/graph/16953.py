#b보다 크면 추가안함 이 방식 bfs방식임V
from queue import Queue
q = Queue()
a, b = map(int ,input().split())
q.put((a, 0))
min = a
check = 0
while(True):
    if(q.empty()):
        print(-1)
        break
    num, idx = q.get()
    if(num < b):
    # print(num, idx)
        q.put((num *2, idx + 1))
        q.put((num * 10 + 1, idx + 1))
    if(num == b):
        print(idx + 1)
        break