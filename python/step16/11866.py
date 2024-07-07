#n, k = 10^3
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(i)
idx = - 1
print('<', end = '')
while arr:
    idx += k
    idx = idx % len(arr)
    if(len(arr) != 1):
        print(arr[idx] + 1, end=', ')
    else:
        print(str(arr[idx] + 1) +'>')
    arr.remove(arr[idx])
    idx -= 1