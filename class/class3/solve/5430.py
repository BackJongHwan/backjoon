# t = 100 = 10^2
# p = 10^5
# n = 10^5
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    error = 0
    left = True
    cmd = input().rstrip()
    size = int(input())
    arr_str = (input().rstrip())[1:-1]
    arr_temp = arr_str.split(',')
    arr = []
    #O(n)
    for i in range(size):
        arr.append(int(arr_temp[i]))
    arr_deque = deque(arr)
    #O(p * n)
    for i in range(len(cmd)):
        if(cmd[i] == 'R'):
            if left:
                left = False
            else:
                left = True
        else:
            if(len(arr_deque) == 0):
                error = 1
                break
            else:
                if left:
                    arr_deque.popleft()
                else:
                    arr_deque.pop()
        if error:
            break
    if error:
        print("error")
    else:
        result = list(arr_deque)
        if left:
            print("[",end="")
            print(",".join(map(str, result)), end="")
            print("]")
        else:
            result.reverse()
            print("[",end="")
            print(",".join(map(str, result)), end="")
            print("]")