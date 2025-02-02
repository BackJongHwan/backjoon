import sys
from collections import deque
input = sys.stdin.readline
#D, S, L, R
#D -> num * 2 % 10000
#S -> num - 1 if num == 0 num = 9999
#L -> Lotate -> d1 d2 d3 d4 => d2 d3 d4 d1
#R -> Lotate -> d1 d2 d3 d4 => d4 d1 d2 d3

def D(num):
    num *= 2
    return num % 10000

def S(num):
    num -= 1
    if(num == -1):
        num = 9999
    return num

def L(num):
    return (num % 1000) * 10 + num // 1000

def R(num):
    return (num % 10) * 1000 + num // 10
def minimal(a, b, visited):
    Q = deque([(a, '')])
    while Q:
        num, cmd = Q.popleft()
        if num == b:
            return cmd
        dNum = D(num)
        if not visited[dNum]:
            visited[dNum] = True
            Q.append((dNum, cmd + 'D'))
        sNum = S(num)
        if not visited[sNum]:
            visited[sNum] = True
            Q.append((sNum, cmd + 'S'))
        lNum = L(num)
        if not visited[lNum]:
            visited[lNum] = True
            Q.append((lNum, cmd + 'L'))
        rNum = R(num)
        if not visited[rNum]:
            visited[rNum] = True
            Q.append((rNum, cmd + 'R'))

test = int(input())
for _ in range(test):
    a, b = map(int ,input().split())
    visited = [False] * 10001
    result = minimal(a, b, visited)
    print(result)