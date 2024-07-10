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