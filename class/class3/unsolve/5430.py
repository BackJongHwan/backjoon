# t = 100 = 10^2
# p = 10^5
# n = 10^5

import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    error = 0
    cmd = input().rstrip()
    size = int(input())
    arr_str = (input().rstrip())[1:-1]
    arr_temp = arr_str.split(',')
    arr = []
    for i in range(size):
        arr.append(int(arr_temp[i]))
    for i in range(len(cmd)):
        if(cmd[i] == 'R'):
            arr.reverse()
        else:
            if(len(arr) == 0):
                error = 1
                break
            else:
                arr.pop(0)
        if error:
            break
    if error:
        print(error)
    else:
        print(arr)