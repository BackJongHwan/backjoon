#n = 10^6 -> O(n)
from collections import deque
import sys
input = sys.stdin.readline

deck = deque()
n = int(input())
for _ in range(n):
    cmd = list(input().split())
    if(cmd[0] == '1'):
        deck.appendleft(int(cmd[1]))
    elif(cmd[0] == '2'):
        deck.append(int(cmd[1]))
    elif(cmd[0] == '3'):
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif(cmd[0] == '4'):
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif(cmd[0] == '5'):
        print(len(deck))
    elif(cmd[0] == '6'):
        if not deck:
            print(1)
        else:
            print(0)
    elif(cmd[0] == '7'):
        if deck:
            print(deck[0])
        else:
            print(-1)
    else:
        if deck:
            print(deck[-1])
        else:
            print(-1)
