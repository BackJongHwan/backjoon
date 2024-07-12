#m = 3 * 10^6 -> O(n)
import sys
input = sys.stdin.readline

s = set()
m = int(input())
for _ in range(m):
    cmd = list(input().split())
    if(cmd[0] == "add"):
        s.add(int(cmd[1]))
    elif(cmd[0] == "remove"):
        if int(cmd[1]) in s: 
            s.remove(int(cmd[1]))
    elif(cmd[0] == "check"):
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
    elif(cmd[0] == "toggle"):
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    elif(cmd[0] == "all"):
        for i in range(20):
            s.add(i + 1)
    elif(cmd[0] == "empty"):
        s.clear()
    else:
        print("Error")
        break
