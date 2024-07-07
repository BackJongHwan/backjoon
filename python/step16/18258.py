# n is 10^6 -> O(n)
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    cmd = list(input().split())
    if(cmd[0] == "push"):
        queue.append(cmd[1])
    elif(cmd[0] == 'pop'):
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif(cmd[0] == 'size'):
        print(len(queue))
    elif(cmd[0] == 'empty'):
        if queue:
            print(0)
        else:
            print(1)
    elif(cmd[0] == 'front'):
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif(cmd[0] == 'back'):
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    else:
        print("wrong input!")