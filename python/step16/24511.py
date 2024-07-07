# n = 10^6 , m <= 10^6  ----> O(n)
import sys
input = sys.stdin.readline

n = int(input())
structure = list(map(int, input().split()))
qs_list = list(map(int, input().split()))  
m  = int(input())
c = list(map(int, input().split()))
stack = []
for i in range(n):
    if(structure[i] == 0):
        stack.append(qs_list[i])
k= 0
ans = []
while stack and k < m:
    ans.append(stack.pop())
    k += 1
i = 0
while k < m:
    ans.append(c[i])
    i += 1
    k += 1
print(" ".join(map(str, ans)))