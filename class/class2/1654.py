# k = 10^4 n = 10^6
# O(N)?? IDK
import sys
input = sys.stdin.readline
lan_list = []
k, n = map(int,input().split())
lan_list = [int(input()) for i in range(k)]
left = 1 
right = max(lan_list)
middle = 0
while left <= right:
    a = 0
    middle = (left + right) // 2
    print(middle)
    for num in lan_list:
        a += (num  // middle)
    if(a >= n):
        left = middle + 1
    else:
        right = middle - 1
print(right)