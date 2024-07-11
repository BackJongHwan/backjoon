# n = 5 * 10^4 
# O(nlogn)

import sys
input = sys.stdin.readline
'''
n = int(input())
k = int(n ** 0.5)
num_list = set() 
for i in range(1, k + 1):
    num_list.add(i ** 2)
#O(n) -> root(n)  * root(n)
num_two_list  = set() 
for i in num_list:
    for j in num_list:
        num_two_list.add(i + j)
if n in num_list:
    print(1)
elif n in num_two_list:
    print(2)
else:
    found = False
    #O(root(n))
    for i in num_list:
        if (n - i) in num_two_list:
            print(3)
            found = True
            break
    if not found:
        print(4)
'''
#using dp...
'''
n = int(input())
k = int(n ** 0.5)
result = [4] * (n + 1)
result[0] = 0
squares = [i ** 2 for i in range(1, k + 1)]

for i in range(1, n + 1):
    for num in squares:
        if i < num:
            break
        result[i] = min(result[i] , result[i - num] + 1)
        if(result[i] == 1):
            break
print(result[n])
'''
#using bfs
from collections import deque
def bfs(n):
    if(n == 1):
        return 1
    k = int(n ** 0.5)
    squares = [i ** 2 for i in range(1, k + 1)]
    level = 0
    q = deque([n])
    visited = set()
    while q:
        level += 1
        for _ in range(len(q)):
            current_value = q.popleft()
            for num in squares:
                value = current_value - num
                if(value < 0):
                    break
                elif(value == 0):
                    return level
                else:
                    if value not in visited:
                        visited.add(value)
                        q.append(value)
    return level

n = int(input())
result = bfs(n)
print(result)